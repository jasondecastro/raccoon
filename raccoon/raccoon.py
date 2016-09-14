#!/usr/bin/env python

import sys

fname = sys.argv[1]
action = ''
if len(sys.argv) == 3:
  action = sys.argv[2]
schema = []
queries = []
current = []
converted_schema = []
db = []
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

  for query in queries:
    db.append(query[0])

  global dbname
  dbname = db[0]
  queries[0].remove(db[0])

  dbname = dbname.strip(":")

  for query in queries:
    columns = str(len(query) - 1)
    string = []

    for line in query:
      if ':' not in line:
        if len(line.split(" ")) > 1:
          string.append('  ' + line + ',')
        else:
          string.append('  ' + line + ' STRING,')

        for reaction in string:
          if '?' in reaction:
            string[string.index(reaction)] = reaction.replace("?","").replace("STRING", "BOOLEAN")

    string[-1] = string[-1].strip(',')
    sql.append("CREATE TABLE IF NOT EXISTS %s ( id INTEGER PRIMARY KEY AUTOINCREMENT, %*s );" % (query[0].strip(':'), len(query) - 1, "\n".join(string).strip(' ').replace('\n', '')))

    # print "The `%s` table will be created with %s columns.\n" % (query[0].strip(':'), len(query) - 1)

    converted_schema.append("""CREATE TABLE IF NOT EXISTS %s (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
%*s
);
    """ % (query[0].strip(':'), len(query) - 1, "\n".join(string)))

    # print converted_schema

    database.append(query[0].strip(':'))



def runQueries(sql, engine="sqlite"):
  import sqlite3
  con = sqlite3.connect(dbname + '.db')
  cur = con.cursor() 
  for query in sql:
    cur.execute(query)
  con.commit()

def run():
  readSchema(fname)
  parseSchema(schema, queries, current)
  convertSchema(schema)
  if action == 'raw':
    with open('schema.sql', 'a') as target:
      target.write("\n".join(converted_schema))
  else:
    runQueries(sql)

if __name__ == '__main__':
  run()