from rom_connectors.utils import get_source_forge_files_rss

# maybe official but website down and no links to there
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/xdroidoss/files/')