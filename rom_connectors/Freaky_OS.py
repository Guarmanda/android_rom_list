from rom_connectors.utils import get_source_forge_files_rss

# I prefered using sourceforge because website doesn't contain code names
# and website links leads to sourceforge, 
# which have only a difference of 5 devices with website
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/freakyos/files/')
