from utils import get_source_forge_files_rss

# official
def getSupportedDevices():
    supported_devices = []
    supported_devices = get_source_forge_files_rss('https://sourceforge.net/projects/arrow-os/files/arrow-13.1/official/')
    supported_devices = supported_devices + get_source_forge_files_rss('https://sourceforge.net/projects/arrow-os/files/arrow-12.1/official/')
    supported_devices = supported_devices + get_source_forge_files_rss('https://sourceforge.net/projects/arrow-os/files/arrow-13.0/official/')
    # remove duplicates
    supported_devices = list(dict.fromkeys(supported_devices))
    return supported_devices
print(getSupportedDevices())