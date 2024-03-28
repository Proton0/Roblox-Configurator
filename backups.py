import os
from pick import pick
import patches
import shutil

if not os.path.exists("backups"):
    os.mkdir("backups")

def BackupMain():
    options = [
        "Restore from Backup",
        "Launch backup",
        "Take a backup"
    ]
    option, index = pick(options, "Select an option")
    if option == "Take a backup":
        Takebackup()
    if option == "Restore from Backup":
        Restore()
    if option == "Launch backup":
        LaunchBackup()

def Takebackup():
    print("Taking a backup. Please wait!")
    version = patches.GetRobloxVersion("/Applications/Roblox.app/Contents/Info.plist")
    if os.path.exists("backups/" + "Roblox-" + version + ".backup"):
        print("A backup already exists for this version")
        return
    shutil.copytree("/Applications/Roblox.app", f"backups/Roblox-{version}.backup")
    print("Success")

def Restore():
    options = os.listdir("backups")
    option, index = pick(options, "Select a backup to restore to")
    print(f"Restoring from {option}")
    if os.path.exists("/Applications/Roblox.app"):
        shutil.rmtree("/Applications/Roblox.app")
        print("Removed current roblox install")
    shutil.copytree("backups/" + option, "backups/Roblox.app")
    shutil.move("backups/Roblox.app", "/Applications/Roblox.app")
    print("Restore complete")

def LaunchBackup():
    options = os.listdir("backups")
    option, index = pick(options, "Select a backup to launch")
    print(f"Launching {option}")
    os.system(f"backups/{option}/Contents/MacOS/RobloxPlayer")