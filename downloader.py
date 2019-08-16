import requests

url = 'https://avatars1.githubusercontent.com/u/835315?s=460&v=4'
r = requests.get(url)

filename = url.split('/')[-1]
new_filename = filename.split('?')[0] + '.jpg'

f = open(new_filename, 'wb')
f.write(r.content)
f.close()