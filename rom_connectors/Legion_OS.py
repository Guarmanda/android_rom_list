
from rom_connectors.utils import get_source_forge_files_rss

# official, a non-official list is also avalaible
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/legionrom/files/')

