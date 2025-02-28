from rom_connectors.utils import get_source_forge_files_rss

# official, websites links leads there
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/syberiaos/files/')