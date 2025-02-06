from rom_connectors.utils import get_source_forge_files_rss

# no website, seems official
def getSupportedDevices():
    firstlist =  get_source_forge_files_rss('https://sourceforge.net/projects/orionos/files/A14/') + get_source_forge_files_rss('https://sourceforge.net/projects/orionos/files/A15/')
    # remove duplicates
    return list(set(firstlist))