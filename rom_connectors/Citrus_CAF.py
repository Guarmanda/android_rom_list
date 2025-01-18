from rom_connectors.utils import get_source_forge_files_rss

# No website, old releases
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/citrus-caf/files/')



