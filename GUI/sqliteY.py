import glob
import json
import sqlite3

# https://realpython.com/command-line-interfaces-python-argparse/

# https://devopsheaven.com/sqlite/databases/json/python/api/2017/10/11/sqlite-json-data-python.html

# Read jsons in local files into a list and store them as dictionaries.
# glob creates a list with path+filename+extension e.g. 'Json/nginx.json'
json_filenames = (glob.glob("Json/*.json"))
json_data = []
for file in json_filenames:
    file = open(file, "r")
    json_file = json.loads(file.read())
    json_data.append(json_file)
    file.close()

# Store data in SQLite.
con = sqlite3.connect('projecty.sqlitedb')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS entities")
cur.execute("CREATE TABLE entities (id varchar(3), data json)")
for entry in json_data:
    cur.execute("INSERT INTO entities VALUES (?, ?)", [entry['id'], json.dumps(entry)])
    con.commit()
print("-----")
for row in cur.execute("SELECT id, data FROM entities ORDER BY id ASC"):
    print(row[1])
print("-----")
cur.close()
con.close()

print(json_data)

'''


>>> conn = sqlite3.connect('test.db')
>>> c = conn.cursor()
>>> c.execute("CREATE TABLE countries (id varchar(3), data json)")
<sqlite3.Cursor object at 0x7f32fa57cf10>

f = open("demofile.txt", "r")
print(f.read()) 


import sqlite3
con = sqlite3.connect('projecty.sqlitedb')

cur = con.cursor()

# Create table
cur.execute("CREATE TABLE IF NOT EXISTS stocks
               (date text, trans text, symbol text, qty real, price real)")

# Json example
cur.execute("CREATE TABLE IF NOT EXISTS entities (id varchar(3), data json)")

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','SELL','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()


for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)




# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
'''