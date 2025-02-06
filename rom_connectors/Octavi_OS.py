from rom_connectors.utils import get_source_forge_files_rss

# website down and pointing on xhamster (seriously), so sourceforge is the only way
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/octavi-os/files/')