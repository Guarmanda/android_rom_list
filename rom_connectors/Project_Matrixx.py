from rom_connectors.utils import get_source_forge_files_rss

# They do have a website but links goes on sourceforge and sourceforge is an easyer source
def getSupportedDevices():
    device_list = get_source_forge_files_rss('https://sourceforge.net/projects/projectmatrixx/files/Android-15/') + get_source_forge_files_rss('https://sourceforge.net/projects/projectmatrixx/files/Android-14/') + get_source_forge_files_rss('https://sourceforge.net/projects/projectmatrixx/files/Android-13/')
    # remove duplicates
    return list(dict.fromkeys(device_list))