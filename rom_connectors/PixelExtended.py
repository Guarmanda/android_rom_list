from rom_connectors.utils import get_source_forge_files_rss

# Website down, dunno if sourceforge is official or not
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/pixelextended/files/') 