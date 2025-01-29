from utils import get_source_forge_files_rss

# official but more devices than the actual website (still, website links redirects there)
def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/malluos/files/')