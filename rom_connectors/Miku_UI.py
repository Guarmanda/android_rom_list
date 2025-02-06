from rom_connectors.utils import get_source_forge_files_rss

# official but more devices than the actual website (still, website links redirects there)
def getSupportedDevices():
    firstlist = get_source_forge_files_rss('https://sourceforge.net/projects/divarelease/files/')
    # for each elem in list, take only first part before '_'
    supported_devices = list({elem.split('_')[0] for elem in firstlist})
    return supported_devices




