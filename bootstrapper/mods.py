import os
import shutil
from tqdm import tqdm

def Install(pack_folder, bootstrapper=False):
    folders = []
    content = os.path.join(pack_folder, 'content')
    if os.path.exists(content):
        folders.append(content)
    platformcontent = os.path.join(pack_folder, 'PlatformContent')
    if os.path.exists(platformcontent):
        folders.append(platformcontent)
    extracontent = os.path.join(pack_folder, 'ExtraContent')
    if os.path.exists(extracontent):
        folders.append(extracontent)

    if bootstrapper == False:
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
        if folder.endswith('PlatformContent'):
            destination = "/Applications/Roblox.app/Contents/Resources/PlatformContent"
            folder_name = "PlatformContent"
        elif folder.endswith('ExtraContent'):
            destination = "/Applications/Roblox.app/Contents/Resources/ExtraContent"
            folder_name = "ExtraContent"
        elif folder.endswith('content'):
            destination = "/Applications/Roblox.app/Contents/Resources/content"
            folder_name = "content"

        print(f"Replacing {folder_name}...")
        # Copy files from source folder to destination folder with tqdm progress bar
        for root, dirs, files in tqdm(os.walk(folder), desc=f"Replacing {folder_name}", unit='files'):
            for file in files:
                src_file = os.path.join(root, file)
                rel_path = os.path.relpath(src_file, folder)
                dest_file = os.path.join(destination, rel_path)
                dest_dir = os.path.dirname(dest_file)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.copy(src_file, dest_file)

    print("Mod installed successfully.")