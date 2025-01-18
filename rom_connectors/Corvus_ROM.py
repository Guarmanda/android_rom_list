from rom_connectors.utils import get_source_forge_files_rss

# No website, rom kinda dead
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/corvus-os/files/')