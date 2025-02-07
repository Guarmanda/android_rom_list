from rom_connectors.utils import get_source_forge_files_rss

# No website, telegram links goes there
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/projectzephyrus/files/')