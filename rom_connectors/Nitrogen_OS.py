from rom_connectors.utils import get_source_forge_files_rss

# no website but links on xda leads to sourceforge, so official still
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/nitrogen-project/files/') 
