import sqlite3


#generic DB function for changing DB
def handle_Db(DBfile, SQL):
    connectionDB = sqlite3.connect(DBfile) # connect to DBfile
    cursor =connectionDB.cursor()
    cursor.execute(SQL)
    connectionDB.commit()
    connectionDB.close()











