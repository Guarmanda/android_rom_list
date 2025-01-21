from rom_connectors.utils import get_source_forge_files_rss

# No website, last update from late 2022
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/eternityosreleases/files/')