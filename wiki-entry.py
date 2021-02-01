from gs_lib import general
from gs_lib import wiki


link_src = 'https://en.wikipedia.org/wiki/Leonardo_DiCaprio'
link_src = 'https://en.wikipedia.org/wiki/Brad_Pitt'
# link_src = 'https://en.wikipedia.org/wiki/Country'
# actor_data = general.fetch_data(link_src, 'data/wiki/leonardo-dicaprio.html')
actor_data = general.fetch_data(link_src, 'data/wiki/brad-pitt.html')
data = wiki.find_wiki_info_table(actor_data, contenttype='entertainment')

if data is False:
    print("There is no data.")
else:
    print(data)
