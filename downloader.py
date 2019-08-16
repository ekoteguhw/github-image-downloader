import requests
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-l', '--link', required=True, help='Link file')
args = vars(ap.parse_args())

r = requests.get(args['link'])

filename = args['link'].split('/')[-1]
new_filename = filename.split('?')[0] + '.jpg'

f = open(new_filename, 'wb')
f.write(r.content)
f.close()