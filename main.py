import subprocess

from pick import pick

import backups
import getserver
import fflags

import mods
import patches
import time
while True:
    version_roblox = patches.GetRobloxVersion("/Applications/Roblox.app/Contents/Info.plist")
    if version_roblox == "Unknown":
        title = "Roblox Configurator 1.7 for MacOS"
    else:
        title = f"Roblox Configurator 1.7 for MacOS (Roblox: {version_roblox})"
    options = [
        "Install Roblox",
        "Install Roblox Studio",
        "Uninstall Roblox",
        "FFLag Tweaks",
        "Get roblox version",
        "Launch roblox",
        "Launch roblox and get server ip and port",
        "Get roblox channel",
        "Mods",
        "Backups",
    ]

    option, index = pick(options, title)
    try:
        if option == "Backups":
            backups.BackupMain()
        if option == "Mods":
            mods.InstallUI()
        if option == "Uninstall Roblox":
            patches.UninstallRoblox()
        if option == "Install Roblox Studio":
            patches.install_studio()
        if option == "Get roblox channel":
            getserver.GetRobloxChannel()
        if option == "Launch roblox and get server ip and port":
            getserver.Launch()
        if option == "Launch roblox":
            subprocess.run(["/Applications/Roblox.app/Contents/MacOS/RobloxPlayer"])
        if option == "Install Roblox":
            patches.install()

        if option == "Get roblox version":
            k, b = patches.GetLatestRobloxVersion()
            print(f'Installed: {patches.GetRobloxVersion("/Applications/Roblox.app/Contents/Info.plist")}')
            print(f"Latest : {k}")
            print(f"Latest version hash : {b}")
            if k == patches.GetRobloxVersion("/Applications/Roblox.app/Contents/Info.plist"):
                print("Client is up-to-date!")

        if option == "FFLag Tweaks":
            fflags.FFlagLaunch()
        time.sleep(5)
    except Exception as e:
        print(f"Error : {e}")
        time.sleep(60)