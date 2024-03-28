from pick import pick
import fflags
import patches
import time
while True:
    version_roblox = patches.GetRobloxVersion("/Applications/Roblox.app/Contents/Info.plist")
    if version_roblox == "Unknown":
        title = "Roblox Configurator 1.0 for MacOS"
    else:
        title = f"Roblox Configurator 1.0 for MacOS (Roblox: {version_roblox})"
    options = [
        "Install Roblox",
        "Uninstall Roblox",
        "FFLag Tweaks",
        "Get roblox version"
    ]

    option, index = pick(options, title)
    try:
        if option == "Install Roblox":
            patches.install()

        if option == "Get roblox version":
            print(patches.GetRobloxVersion("/Applications/Roblox.app/Contents/Info.plist"))

        if option == "FFLag Tweaks":
            fflags.FFlagLaunch()
        time.sleep(5)
    except Exception as e:
        print(f"Error : {e}")