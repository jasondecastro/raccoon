fname = 'schema.sw'
meanings = {}
schema = []
queries = []
current = []
sql = []

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

def convertSchema(schema):
  string = []

  for query in queries:
    columns = str(len(query) - 1)
    string = []

    for line in query:
      if ':' not in line:
        string.append('  ' + line + ' STRING,')

    print "The `%s` table will be created with %s columns.\n" % (query[0].strip(':'), len(query) - 1)
    print """CREATE TABLE IF NOT EXISTS %s (
%*s
)
    """ % (query[0].strip(':'), len(query) - 1, "\n".join(string))


if __name__ == '__main__':
  readSchema(fname)
  parseSchema(schema, queries, current)
  convertSchema(schema)

