import sqlite3
import HASHMD5

DBfile= "users.db"

login_data = { "yaniv":"qazwsx", "moshe":"qweasd", "itizk":"asdzxc"}


#generic DB function for changing DB
# INSET INTO, UPDATE, DELETE, CREATE
def change_Db(DBfile, SQL):
    connectionDB = sqlite3.connect(DBfile) # connect to DBfile
    cursor =connectionDB.cursor()
    cursor.execute(SQL)
    connectionDB.commit()
    connectionDB.close()

# SELECT
def read_db(DBfile, SQL):
    connectionDB = sqlite3.connect(DBfile)  # connect to DBfile
    cursor = connectionDB.cursor()  # reset to cursor
    cursor.execute(SQL)  # load the SQL language to RUN
    data = cursor.fetchall()
    connectionDB.commit()  # Do and Run the Command
    connectionDB.close()  # close the connection fo DBfile
    return data


if __name__ == "__main__":
    SQL_CREATE_DB ="CREATE TABLE IF NOT EXISTS users  (username TEXT,password TEXT)"
    change_Db(DBfile, SQL_CREATE_DB)

    for data in login_data.items():
        username = data[0]
        password = data[1]
        SQL_INSERT_DB = f"INSERT INTO users VALUES ('{username}','{HASHMD5.hash(password)}')"
        change_Db(DBfile,SQL_INSERT_DB)