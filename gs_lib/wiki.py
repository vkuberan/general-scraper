from gs_lib import general
from bs4 import BeautifulSoup


# if classname is specified, it will look for the table with the class
# name otherwise it will get the first table found in the page
# (mostly this information table is found at the top of the page) If
# information table is found, it will be parsed and data will be send
# otherwise an empty message will be send
def find_wiki_info_table(data, classname='infobox'):
    soup = BeautifulSoup(data, 'lxml')

    info_box = soup.find('table', class_=classname)

    # if class is not specified or it returns None,
    # try to use the classname infobox
    if info_box is None:
        info_box = soup.find('table', class_='infobox')

    if info_box is None:
        return False

    data = {}

    data['Voila'] = info_box.contents

    return data
