from rom_connectors.utils import get_source_forge_files_rss

# official, websites links leads there
def getSupportedDevices():
    result = []
    # for i = 1 to 5 inclusive
    for i in range(1, 6):
        # get rss feed
        result += get_source_forge_files_rss(f'https://sourceforge.net/projects/risingos-official/files/{i}.x/GAPPS/') + get_source_forge_files_rss(f'https://sourceforge.net/projects/risingos-official/files/{i}.x/VANILLA/')
    return list(set(result))