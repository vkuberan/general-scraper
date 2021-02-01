from gs_lib import general
from gs_lib import wiki


link_src = 'https://en.wikipedia.org/wiki/Leonardo_DiCaprio'
actor = general.fetch_data(link_src, 'data/wiki/leonardo-dicaprio.html')
print(actor)
