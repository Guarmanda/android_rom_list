from rom_connectors.utils import get_source_forge_files_rss

# Ony telegram, links goes on sourceforge
def getSupportedDevices():
    device_list = get_source_forge_files_rss('https://sourceforge.net/projects/project-mistos/files/Android15/') + get_source_forge_files_rss('https://sourceforge.net/projects/project-mistos/files/Android14/')
    # remove duplicates
    return list(dict.fromkeys(device_list))