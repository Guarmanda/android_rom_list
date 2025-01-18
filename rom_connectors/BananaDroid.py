from rom_connectors.utils import get_source_forge_files_rss

# not really official, no more website
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/bananadroid/files/')
