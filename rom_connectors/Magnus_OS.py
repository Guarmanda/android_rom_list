from rom_connectors.utils import get_source_forge_files_rss

# might be official, EOL but files quite recent so I still list it
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/magnusos/files/')
