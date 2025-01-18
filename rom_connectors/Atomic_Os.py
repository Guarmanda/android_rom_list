from rom_connectors.utils import get_source_forge_files_rss

# maybe not official, no website
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/teamdarkness/files/Atomic-OS/')
