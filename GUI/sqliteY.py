import sys
import traceback
import glob
import json
import sqlite3

# https://realpython.com/command-line-interfaces-python-argparse/
# https://devopsheaven.com/sqlite/databases/json/python/api/2017/10/11/sqlite-json-data-python.html

ACTION = "select"

def handle_args():
    global ACTION
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("-- Use options -h or --help for help")
        sys.exit()
    elif sys.argv[1] in ['-h', '--help']:
        print("-- OPTIONS:")
        print("-- -l, --load - Loads data into sqlite db based on json files in Json dir.")
        print("-- -s, --select - Selects data from sqlite db and prints result to terminal.")
        sys.exit()
    elif sys.argv[1] in ['-l', '--load']:
        ACTION = "load"
    elif sys.argv[1] in ['-s', '--select']:
        ACTION = "select"
    else:
        print("-- Invalid OPTION.")
        print("-- Use options -h or --help for help")
        sys.exit()

def load_db():
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
    cur.execute("CREATE TABLE entities (id INT, data json)")
    for entry in json_data:
        cur.execute("INSERT INTO entities VALUES (?, ?)", [entry['id'], json.dumps(entry)])
        con.commit()
    cur.close()
    con.close()
    print("-- Values inserted.")

def select_db():
    con = sqlite3.connect('projecty.sqlitedb')
    cur = con.cursor()
    for row in cur.execute("SELECT id, data FROM entities ORDER BY id ASC"):
        print(row[1])
        print("--")
    cur.close()
    con.close()

def main():
    try:
        handle_args()
        if ACTION == 'load':
            load_db()
        else:
            select_db()
    except Exception as e:
        print ("An unforeseen error has occurred!")
        print ("Error message: ", e, ".")
        print (traceback.format_exc())
    finally:
        print ("-- Closing %s, Bye!" % sys.argv[0])

#Python convention to call main():
if __name__ == "__main__":
   main()