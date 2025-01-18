
from utils import get_sourceforge_devices


def getSupportedDevices():
    return get_sourceforge_devices('https://sourceforge.net/projects/teamdarkness/files/Atomic-OS/')

print(getSupportedDevices())