from rom_connectors.utils import get_source_forge_files_rss

# websites links leads on sourceforge, easyer to do like that then
def getSupportedDevices():
    firstlist =  get_source_forge_files_rss('https://sourceforge.net/projects/pixelos-releases/files/fifteen/') + get_source_forge_files_rss('https://sourceforge.net/projects/pixelos-releases/files/fourteen/') + get_source_forge_files_rss('https://sourceforge.net/projects/pixelos-releases/files/thirteen/') + get_source_forge_files_rss('https://sourceforge.net/projects/pixelos-releases/files/twelve/')
    # remove duplicates
    return list(set(firstlist))