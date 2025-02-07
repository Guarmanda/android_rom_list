from rom_connectors.utils import get_source_forge_files_rss

# They do have a website but links goes on sourceforge and sourceforge is an easyer source
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/projectsakura/files/')