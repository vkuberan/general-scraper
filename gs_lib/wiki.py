from gs_lib import general
from bs4 import BeautifulSoup

types_of_content = {
    'entertainment': ['award', 'filmography', 'performance',
                      'videography', 'discography'],
}

# if classname is specified, it will look for the table with the class
# name otherwise it will get the first table found in the page
# (mostly this information table is found at the top of the page) If
# information table is found, it will be parsed and data will be send
# otherwise an empty message will be send


def find_wiki_info_table(data, classname='infobox', contenttype='general'):
    soup = BeautifulSoup(data, 'lxml')

    info_box = soup.find('table', class_=classname)

    # if class is not specified or it returns None,
    # try to use the classname infobox
    if info_box is None:
        info_box = soup.find('table', class_='infobox')

    if info_box is None:
        return False

    data = {}

    data_rows = info_box.find('tbody').find_all('tr')
    iCnt = 0
    for data_row in data_rows:
        replace_html = {
            u'\xa0': u' ',
            '\u200b': ''
        }
        data_captions = data_row.find('th')
        data_contents = data_row.find('td')

        if data_captions is None and data_contents is None:
            pass
        elif data_captions is not None and data_contents is None:
            data[iCnt] = data_captions.get_text(separator=',', strip=True)
        elif data_captions is None and data_contents is not None:
            pass
        else:
            header = data_captions.get_text(strip=True)
            header = general.wiki_replace_unicode(header, replace_html).strip()
            content = data_contents.get_text(separator=', ', strip=True)
            data[header] = general.wiki_replace_unicode(content, replace_html)

        iCnt += 1

    if contenttype == 'entertainment':
        # types_of_content[contenttype]

    return data
