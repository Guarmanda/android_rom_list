from rom_connectors.utils import get_source_forge_files_rss

# May be official, called 'releases', and website doesn't works correctly anyway
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/droidxui-releases/files/')