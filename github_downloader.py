import requests
import argparse
import progressbar
from url_generator import generator

ap = argparse.ArgumentParser()
ap.add_argument('-l', '--range', required=True, help='Range image download, ex. 1-100')
args = vars(ap.parse_args())

ranges = args['range'].split('-')
if int(ranges[1]) > int(ranges[0]):
  kumpulan_link = generator(int(ranges[0]), int(ranges[1]))
  for i in progressbar.progressbar(range(len(kumpulan_link))):
    r = requests.get(kumpulan_link[i])
    filename = kumpulan_link[i].split('/')[-1]
    new_filename = filename.split('?')[0] + '.jpg'

    f = open('profiles/' + new_filename, 'wb')
    f.write(r.content)
    f.close()
else:
  print('{} must be greater or same than {}'.format(ranges[1], ranges[0]))
  quit()