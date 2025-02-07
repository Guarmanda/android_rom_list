from rom_connectors.utils import get_source_forge_files_rss

# Ony telegram, links goes on sourceforge
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/projectpixelage/files/')
