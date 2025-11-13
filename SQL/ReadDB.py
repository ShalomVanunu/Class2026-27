
import sqlite3
#SELECT

file = "Our_data.db"

def read_db(DBfile, SQL):
    connectionDB = sqlite3.connect(DBfile)  # connect to DBfile
    cursor = connectionDB.cursor()  # reset to cursor
    cursor.execute(SQL)  # load the SQL language to RUN
    data = cursor.fetchall()
    connectionDB.commit()  # Do and Run the Command
    connectionDB.close()  # close the connection fo DBfile
    return data

SQL = "SELECT * FROM employee_records "
data = read_db(file,SQL)

for line in data :
    print(line)
