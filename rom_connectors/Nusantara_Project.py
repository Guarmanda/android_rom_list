from rom_connectors.utils import get_source_forge_files_rss

# Maybe not official, but their website is shity (can't get all devices on one page) and the links points on pling
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/nusantaraproject/files/') 
