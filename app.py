fname = 'schema.sw'

meanings = {}

sections = {
  0: [], 
  1: [], 
  2: [], 
  3: []
}

schema = []

with open(fname) as f:
    for line in f.readlines():
      schema.append(line.strip('\n').strip(' '))

for element in schema:
  sections[0].append(element)

  if len(element) == 0:
    sections[1].append(element)


for section in schema:
  while 'end' not in section:
    sections[len(sections)].update(section)

for query in schema:
  if ':' in query:
    meanings[schema.index(query)] = 'CREATE TABLE IF NOT EXISTS %s' % query.replace(':', '').replace('\n', '')

print meanings