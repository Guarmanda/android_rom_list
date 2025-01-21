from rom_connectors.utils import get_source_forge_files_rss

# Verry up to date (android 15), 
# I prefered using sourceforge because website needed to use selenium
# and website links leads to sourceforge where all files are really recent
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/evolution-x/files/')