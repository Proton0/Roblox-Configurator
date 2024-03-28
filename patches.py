import os
from tqdm import tqdm
import shutil
import plistlib
import requests
import time
from subprocess import Popen, PIPE
import psutil
def KillRoblox():
    for pid in (process.pid for process in psutil.process_iter() if process.name() == "Roblox"):
        os.kill(pid, 0)

def KillRobloxInstaller():
    for pid in (process.pid for process in psutil.process_iter() if process.name() == "RobloxPlayerInstaller"):
        os.kill(pid, 0)

def install():
    if os.path.exists("/Applications/Roblox.app"):
        print("Roblox is already installed. Re-installing roblox!")
        shutil.rmtree("/Applications/Roblox.app")
    if os.path.exists("installer.dmg"):
        os.remove("installer.dmg")
    print("Downloading the roblox installer")
    # --- code from google gemini lol (added osx user-agent cuz roblox keeps downloading the Windows version)
    response = requests.get("https://www.roblox.com/download/client?os=mac", stream=True, allow_redirects=True, headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"})
    if response.status_code != 200:
        print(f"Error downloading file: {response.status_code}")
        return
    total_size = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading installer")
    with open("installer.dmg", 'wb') as file:
        for data in response.iter_content(1024):
            progress_bar.update(len(data))
            if not data:
                break
            file.write(data)
    progress_bar.close()
    # -------------------------------
    if not os.path.exists("installer.dmg"):
        print("Error while downloading the roblox dmg")
        return
    print("Attempting to mount the DMG")
    k = os.system("hdiutil mount installer.dmg")
    if k != 0:
        print(f"Error while mounting the DMG : {k}")
        return
    print("Mounted the DMG")
    # start thread
    print("Launching the installer")
    installer_process = Popen("/Volumes/RobloxPlayerInstaller/RobloxPlayerInstaller.app/Contents/MacOS/RobloxPlayerInstaller")
    completed = psutil.wait_procs([installer_process])
    if completed:
        print("Install completed successfully.")
    else:
        print("Installer timed out or failed.")
        installer_process.kill()
    KillRoblox()
    KillRobloxInstaller()
    print("Cleaning up")
    print("Unmounting the DMG")
    os.system("hdiutil detach /Volumes/RobloxPlayerInstaller")
    print("Deleting the DMG")
    os.remove("installer.dmg")
    KillRobloxInstaller()
    KillRoblox()

def GetRobloxVersion(plist_file):
    try:
        with open(plist_file, 'rb') as fp:
            plist = plistlib.loads(fp.read())
            return plist["CFBundleShortVersionString"]
    except FileNotFoundError as e:
        return "Unknown"
    except Exception as e:
        print(f"Error getting roblox version : {e}")
        return "Unknown"