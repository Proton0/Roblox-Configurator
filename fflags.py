from pick import pick
import json
import shutil
def FFlagLaunch():
    title = "Select an FFLag Tweak"
    options = [
        "Reset all FFLag tweaks",
        "Unlock FPS",
        "Unlock FPS + Enable Vulkan",
        "Disable Vulkan",
        "Enable 21 Graphics Slider"
    ]
    option, index = pick(options, title)
    if option == "Reset all FFLag tweaks":
        shutil.rmtree("/Applications/Roblox.app/Contents/MacOS/ClientSettings", ignore_errors=True)
        print("Succesfully deleted all FFLag tweaks")