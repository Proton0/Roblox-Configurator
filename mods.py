import os
from tqdm import tqdm
from pick import pick
import shutil
def InstallUI():
    options = os.listdir("mods")
    title = "Select a pack to install"
    option, index = pick(options, title)
    print(f"Installing pack {option}. Please wait!")
    if os.path.isfile("mods/" + option):
        print("Files are not allowed. Please extract it")
        return
    Install("mods/" + option)

def Install(pack_folder):
    folders = []
    content = pack_folder + '/content'
    if os.path.exists(content):
        folders.append(content)
    platformcontent = pack_folder + '/PlatformContent'
    if os.path.exists(platformcontent):
        folders.append(platformcontent)
    extracontent = pack_folder + '/ExtraContent'
    if os.path.exists(extracontent):
        folders.append(extracontent)

    print(""" --- WARNING --- WARNING --- WARNING
    Using a mod for roblox can cause security issues. Please check the pack and make sure that there is NO malware on it!!!
    Proton0 is NOT responsible for any damages done to your device!
    """)
    if input("Press 'y' to continue").lower() != "y":
        print("Cancelled")
        return

    print("The following folders will be replaced : ")
    for folder in folders:
        print(folder)

    print("Please do not launch roblox!")
    for folder in folders:
        folder_name = os.path.basename(folder)
        destination_folder = os.path.join("/Applications/Roblox.app/Contents/Resources", folder_name)
        if not os.path.exists(destination_folder):
            print(f"Error: {destination_folder} does not exist!")
            continue

        files_to_replace = os.listdir(folder)
        for file_name in tqdm(files_to_replace, desc=f"Installing mod", unit="file"):
            source_file = os.path.join(folder, file_name)
            destination_file = os.path.join(destination_folder, file_name)
            if os.path.exists(destination_file):
                if os.path.isdir(destination_file):
                    shutil.rmtree(destination_file)  # Remove existing directory
                else:
                    os.remove(destination_file)  # Remove existing file
            shutil.move(source_file, destination_folder)

    print("Mod installed successfully.")