from utils import get_source_forge_files_rss

# official but more devices than the actual website (still, website links redirects there)
def getSupportedDevices():
    firstlist =  get_source_forge_files_rss('https://sourceforge.net/projects/nameless-aosp/files/') + get_source_forge_files_rss('https://sourceforge.net/projects/nameless-clo/files/')
    # remove duplicates
    return list(set(firstlist))

