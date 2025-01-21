# go to /website/the_rom_database and build the website (ng build --base-href /android_rom_list/website/dist/)

import os
import shutil
import subprocess

# if file supported_devices_with_roms.csv doesn't exist, run get_smartphones_infos.py
if not os.path.exists("supported_devices_with_roms.csv"):
    print("Running get_smartphones_infos.py...")
    subprocess.run(["python", "get_smartphones_infos.py"])
    
# delete file in /website/the_rom_database/public/data if exist
if os.path.exists("website/the_rom_database/public/data/supported_devices_with_roms.csv"):
    os.remove("website/the_rom_database/public/data/supported_devices_with_roms.csv")
# move the file to /website/the_rom_database/public/data
print("Moving supported_devices_with_roms.csv to /website/the_rom_database/public/data...")
shutil.move("supported_devices_with_roms.csv", "website/the_rom_database/public/data")

# build the website
print("Building the website...")
os.chdir("website/the_rom_database")
subprocess.check_output('ng build --base-href /android_rom_list/website/dist/', shell=True)

# move the content of /website/the_rom_database/dist/browser to /website/dist
print("Moving the website to /website/dist...") 
if os.path.exists("../dist"):
    shutil.rmtree("../dist")
# make dir
os.mkdir("../dist")
source_dir = "dist/the_rom_database/browser"
target_dir = "../dist"

file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
