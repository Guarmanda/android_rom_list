from rom_connectors.utils import get_source_forge_files_rss

# maybe official, but no websites and no update since 2022 (2021 for releases)
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/styx-os/files/Athena/release/')