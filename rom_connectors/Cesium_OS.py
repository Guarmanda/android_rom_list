from rom_connectors.utils import get_source_forge_files_rss

# official, website redirects here
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/cesiumos/files/')
