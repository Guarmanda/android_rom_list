from rom_connectors.utils import get_source_forge_files_rss

# No website, links on XDA goes to sourceforge
def getSupportedDevices():
    device_list = get_source_forge_files_rss('https://sourceforge.net/projects/projectradiant/files/twelve/') + get_source_forge_files_rss('https://sourceforge.net/projects/projectradiant/files/eleven/')
    # remove duplicates
    return list(dict.fromkeys(device_list))