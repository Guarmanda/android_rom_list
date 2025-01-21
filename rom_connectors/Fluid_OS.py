from rom_connectors.utils import get_source_forge_files_rss

# I prefered using sourceforge because website needed to use selenium
# and website links leads to sourceforge 
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/project-fluid/files/')
