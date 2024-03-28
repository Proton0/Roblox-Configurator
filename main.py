from pick import pick
import patches
while True:
    version_roblox = patches.GetRobloxVersion("/Applications/Roblox.app/Contents/Info.plist")
    if version_roblox == "Unknown":
        title = "Roblox Configurator 1.0 for MacOS"
    else:
        title = f"Roblox Configurator 1.0 for MacOS (Roblox: {version_roblox})"
    options = [
        "Install Roblox",
        "Uninstall Roblox",
        "Unlock FPS",
        "Unlock FPS + Enable Vulkan",
        "Get roblox version"
    ]

    option, index = pick(options, title)

    if option == "Install Roblox":
        patches.install()

    if option == "Get roblox version":
        print(patches.GetRobloxVersion())