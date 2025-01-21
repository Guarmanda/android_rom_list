from rom_connectors.utils import get_source_forge_files_rss

# Website has no device links for now. Rom seems pretty new, only one device is on sourceforge.
# a list of official devices is also here (with that only device) https://github.com/Fusion-OS/official_devices/blob/master/devices.md
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/fusion-os/files/')