from rom_connectors.utils import get_source_forge_files_rss

# maybe official but no website and no update since 2019
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/wave-os/files/rasmalai-4.x/')