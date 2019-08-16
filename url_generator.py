def generator(a, b):
  base = 'https://avatars1.githubusercontent.com/u/{}?s=460&v=4'

  links = []

  for i in range(a, b):
    links.append(base.format(i))
  return links