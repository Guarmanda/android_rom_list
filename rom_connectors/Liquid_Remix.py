from rom_connectors.utils import get_source_forge_files_rss

# might be official, no website, a bit old (2019 last update)
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/liquid-remix/files/')