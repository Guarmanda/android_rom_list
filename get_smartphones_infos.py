# download this file: https://storage.googleapis.com/play_public/supported_devices.csv
import requests
import pandas as pd
import os

# if file does not exist, download it
if not os.path.exists("supported_devices.csv"):
    donwload = requests.get("https://storage.googleapis.com/play_public/supported_devices.csv")
    with open("supported_devices.csv", "wb") as f:
        f.write(donwload.content)
        
    print("Google CSV file downloaded, it contains brand, market name, codename and model.")


# load the csv
df = pd.read_csv("supported_devices.csv", encoding="utf-16")

# in supported_devices.txt, which is another file, we have the supported devices for each rom like this:
# Advanced_XPerienc_eOs.py: ['sunfish', ...
# We can easily load it too in an object
supported_devices = {}

with open("supported_devices.txt", "r") as f:
    file_content = f.read()  # Rename this variable to avoid overwriting
    for line in file_content.split("\n"):
        if line:
            rom = line.split(":")[0].replace(".py", "").replace("_", " ")
            devices = line.lower().split(":")[1].replace("[", "").replace("]", "").replace('\'', "").split(", ")
            supported_devices[rom] = devices
            
print("Supported devices loaded from supported_devices.txt")

# now we can add a column to the dataframe, with the roms that support each device
df["Supported ROMs"] = ""

df["Retail Branding"] = df["Retail Branding"].str.lower()
df["Marketing Name"] = df["Marketing Name"].str.lower()
df["Device"] = df["Device"].str.lower()
df["Model"] = df["Model"].str.lower()  

for rom, devices in supported_devices.items():
    for device in devices:
        # if the device is in the dataframe, add the rom to the "Supported ROMs" column
        if device in df["Device"].values:
            df.loc[df["Device"] == device, "Supported ROMs"] += rom + " | "
        
        
# remove all devices that have no supported roms
df = df[df["Supported ROMs"] != ""]
df["Supported ROMs"] = df["Supported ROMs"].apply(lambda x: x[:-2])
# remove duplicates
df = df.drop_duplicates(subset=["Retail Branding","Marketing Name","Device","Model","Supported ROMs"])

# for lines where "Retail Branding","Marketing Name","Device" are the same, we can merge the "Model" columns and remove duplicates
df = df.groupby(["Retail Branding", "Marketing Name", "Device", "Supported ROMs"], as_index=False).agg({
    "Model": lambda x: ' / '.join(x)
})

# same for lines where ""Device"","Marketing Name","Model" are the same
df = df.groupby(["Device", "Marketing Name", "Model", "Supported ROMs"], as_index=False).agg({
    "Retail Branding": lambda x: ' / '.join(x)
})

# same for lines where "Retail Branding","Device","Model" are the same
df = df.groupby(["Retail Branding", "Device", "Model", "Supported ROMs"], as_index=False).agg({
    "Marketing Name": lambda x: ' / '.join(x)
})
df = df[["Retail Branding","Marketing Name","Device","Model","Supported ROMs"]]




# save the dataframe to a new csv
df.to_csv("supported_devices_with_roms.csv", index=False)



