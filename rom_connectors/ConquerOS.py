from rom_connectors.utils import get_source_forge_files_rss

# no website, some old but should be stable
def getSupportedDevices():
    supported_devices = get_source_forge_files_rss('https://sourceforge.net/projects/conqueros/files/twelve/') + get_source_forge_files_rss('https://sourceforge.net/projects/conqueros/files/Eleven/stable/') + get_source_forge_files_rss('https://sourceforge.net/projects/conqueros/files/ten/stable/')
    # remove duplicates
    supported_devices = list(dict.fromkeys(supported_devices))
    return supported_devices