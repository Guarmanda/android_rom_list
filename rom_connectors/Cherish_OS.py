from rom_connectors.utils import get_source_forge_files_rss

# not really official, the website redirects in another place, and some devices are not supported anymore
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/cherish-os/files/device/')