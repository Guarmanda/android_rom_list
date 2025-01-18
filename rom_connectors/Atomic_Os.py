
from utils import get_source_forge_files_rss


def getSupportedDevices():
    return get_source_forge_files_rss('https://sourceforge.net/projects/teamdarkness/files/Atomic-OS/')

print(getSupportedDevices())