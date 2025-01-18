from rom_connectors.utils import get_source_forge_files_rss

# not all official, but some are (some links on website), rom discontinued
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/aospextended-rom/files/')
