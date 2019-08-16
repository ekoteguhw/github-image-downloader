import requests

url = 'https://avatars1.githubusercontent.com/u/835315?s=460&v=4'
r = requests.get(url)

f = open('ekoteguhw.jpg', 'wb')
f.write(r.content)
f.close()