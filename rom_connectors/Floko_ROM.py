from rom_connectors.utils import get_source_forge_files_rss

# no updates since 4/5 years. Didn't find any links pointing here from website
# so maybe not official
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/flokorom/files/v3/')