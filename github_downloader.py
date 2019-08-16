import requests
from url_generator import generator

kumpulan_link = generator()

for link in kumpulan_link:
  r = requests.get(link)
  filename = link.split('/')[-1]
  new_filename = filename.split('?')[0] + '.jpg'

  f = open('profiles/' + new_filename, 'wb')
  f.write(r.content)
  f.close()
