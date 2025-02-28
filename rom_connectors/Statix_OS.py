from rom_connectors.utils import get_source_forge_files_rss

# maybe official, but didn't find links on websites
def getSupportedDevices():
    return list(set(get_source_forge_files_rss('https://sourceforge.net/projects/statixos/files/10/') + get_source_forge_files_rss('https://sourceforge.net/projects/statixos/files/13-TIRAMISU/') + get_source_forge_files_rss('https://sourceforge.net/projects/statixos/files/pie/')))