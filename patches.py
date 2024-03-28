import os
from tqdm import tqdm
import requests
import shutil
import plistlib
import requests
from subprocess import Popen, PIPE
def install():
    if os.path.exists("/Applications/Roblox.app"):
        print("Roblox is already installed. Re-installing roblox!")
        shutil.rmtree("/Applications/Roblox.app")
    print("Downloading the roblox installer")
    url = "https://www.roblox.com/download/client?os=mac" # If roblox changed the DMG URL then put it here
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("installer.dmg", 'wb') as f:
            pbar = tqdm(total=int(r.headers['Content-Length']))
            pbar.set_description(f"Downloading roblox installer")
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    pbar.update(len(chunk))
    if not os.path.exists("installer.dmg"):
        print("Error while downloading the roblox dmg")
        return
    print("Attempting to mount the DMG")
    os.system("hdiutil attach installer.dmg")
    print("Mounted the DMG")
    print("Launching the installer")
    os.system("open -a /Volumes/RobloxPlayerInstaller/RobloxPlayerInstaller.app")
    print("Press enter once roblox has been installed")
    input()
    print("Cleaning up")
    path = os.path.abspath("installer.dmg")
    print("The DMG path is {}".format(path))
    # --- Code from https://www.alfredforum.com/topic/9684-workflow-to-eject-disk-image-and-trash-dmg-after-software-install/ ---
    dmg_path = None
    info = Popen(["hdiutil", "info", "-plist"], stdout=PIPE).communicate()[0]
    pl = plistlib.readPlistFromString(info)
    for image in pl["images"]:
        for ent in image["system-entities"]:
            if ent.get("mount-point") == path:
                dmg_path = image["image-path"]
                break

    if dmg_path:
        Popen(["hdiutil", "detach", path])
    # ----------------------------------------------------------------------------------------------------------------------------
    print("Deleting the DMG")
    os.remove("installer.dmg")

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