from rom_connectors.utils import get_source_forge_files_rss

# official, websites links leads there
def getSupportedDevices():
    return list(set(get_source_forge_files_rss('https://sourceforge.net/projects/spiceos/files/12/') + get_source_forge_files_rss('https://sourceforge.net/projects/spiceos/files/13/')))