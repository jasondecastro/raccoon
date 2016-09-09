import sys

print sys.argv[1]
fname = sys.argv[1]
meanings = {}
schema = []
queries = []
current = []
sql = []
datatypes = ["integer", "string", "boolean"]
database = []

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
  print queries

  for query in queries:
    columns = str(len(query) - 1)
    string = []

    for line in query:
      if ':' not in line:
        if len(line.split(" ")) > 1:
          string.append('  ' + line + ',')
        else:
          string.append('  ' + line + ' STRING,')

    string[-1] = string[-1].strip(',')
    sql.append("CREATE TABLE IF NOT EXISTS %s ( id INTEGER PRIMARY KEY AUTOINCREMENT, %*s );" % (query[1].strip(':'), len(query) - 1, "\n".join(string).strip(' ').replace('\n', '')))
    print sql

    print "The `%s` table will be created with %s columns.\n" % (query[1].strip(':'), len(query) - 1)
    print """CREATE TABLE IF NOT EXISTS %s (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
%*s
);
    """ % (query[1].strip(':'), len(query) - 1, "\n".join(string))

    database.append(query[0].strip(':'))

def runQueries(sql, engine="sqlite"):
  import sqlite3
  print database
  con = sqlite3.connect(database[0] + '.db')
  cur = con.cursor() 
  for query in sql:
    cur.execute(query)
  con.commit()

if __name__ == '__main__':
  readSchema(fname)
  parseSchema(schema, queries, current)
  convertSchema(schema)
  runQueries(sql)