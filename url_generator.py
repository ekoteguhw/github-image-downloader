def generator():
  base = 'https://avatars1.githubusercontent.com/u/{}?s=460&v=4'

  links = []

  for i in range(1, 31):
    links.append(base.format(i))
  return links