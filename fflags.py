from pick import pick
import json
import shutil
import os

def CreateClientSettings():
    if not os.path.exists("/Applications/Roblox.app/Contents/MacOS/ClientSettings"):
        os.makedirs("/Applications/Roblox.app/Contents/MacOS/ClientSettings")
    if not os.path.exists("/Applications/Roblox.app/Contents/MacOS/ClientSettings/ClientAppSettings.json"):
        file = open('/Applications/Roblox.app/Contents/MacOS/ClientSettings/ClientAppSettings.json', 'w')
        file.write("{}")
        file.close()

def WriteFFLag(name, value):
    CreateClientSettings()
    print("Reading fflags")
    fflags_file = open("/Applications/Roblox.app/Contents/MacOS/ClientSettings/ClientAppSettings.json", "r")
    print("Loading fflags")
    fflags = json.loads(fflags_file.read())
    fflags_file.close()
    fflags_file = open("/Applications/Roblox.app/Contents/MacOS/ClientSettings/ClientAppSettings.json", "w")
    fflags[name] = value
    fflags_file.write(json.dumps(fflags))
    fflags_file.close()

def FFlagLaunch():
    title = "Select an FFLag Tweak"
    options = [
        "Reset all FFLag tweaks",
        "Unlock FPS",
        "Unlock FPS + Enable Vulkan",
        "Disable Vulkan",
        "Enable 21 Graphics slider",
        "Enable Phase 3 lighting",
        "Disable Phase 3 lighting"
    ]
    option, index = pick(options, title)
    if option == "Reset all FFLag tweaks":
        shutil.rmtree("/Applications/Roblox.app/Contents/MacOS/ClientSettings", ignore_errors=True)
        print("Succesfully deleted all FFLag tweaks")

    if option == "Unlock FPS":
        WriteFFLag("DFIntTaskSchedulerTargetFps", 144)
        print("Unlocked FPS succesfully")

    if option == "Unlock FPS + Enable Vulkan":
        WriteFFLag("DFIntTaskSchedulerTargetFps", 144)
        WriteFFLag("FFlagDebugGraphicsDisableMetal", True)
        WriteFFLag("FFlagDebugGraphicsPreferVulkan", True)
        print("Unlocked FPS and enabled vulkan succesfully")

    if option == "Disable Vulkan":
        WriteFFLag("FFlagDebugGraphicsDisableMetal", False)
        WriteFFLag("FFlagDebugGraphicsPreferVulkan", False)
        print("Disabled vulkan succesfully")


    if option == "Enable 21 Graphics slider":
        WriteFFLag("FFlagFixGraphicsQuality", True)
        WriteFFLag("FFlagCommitToGraphicsQualityFix", True)
        print("Enabled 21 graphics slider")

    if option == "Enable Phase 3 lighting":
        WriteFFLag("FFlagDebugForceFutureIsBrightPhase3", True)
        print("Enabled Phase 3 lighting")

    if option == "Disable Phase 3 lighting":
        WriteFFLag("FFlagDebugForceFutureIsBrightPhase3", False)
        print("Succesfully disabled Phase 3 lighting")
