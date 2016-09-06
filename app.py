fname = 'schema.sw'
meanings = {}
schema = []
queries = []
current = []

def readSchema(filename):
  with open(fname) as f:
      for line in f.readlines():
        schema.append(line.strip('\n').strip(' '))

def parseSchema(schema, queries, current):
  for a in schema:
    if a == '':
      queries.append(current)
      current = []
    else:
      current.append(a)

  queries.append(current)

if __name__ == '__main__':
  readSchema(fname)
  parseSchema(schema, queries, current)

  print(queries)