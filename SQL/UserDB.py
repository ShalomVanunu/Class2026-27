import sqlite3


DBfile = 'usersdb.db'



#generic DB function for changing DB
def handle_Db(DBfile, SQL):
    connectionDB = sqlite3.connect(DBfile) # connect to DBfile
    cursor =connectionDB.cursor()  #reset to cursor
    cursor.execute(SQL) # load the SQL language to RUN
    connectionDB.commit() # Do and Run the Command
    connectionDB.close() # close the connection fo DBfile

create_table_sql = "CREATE TABLE IF NOT EXISTS users  (fname TEXT,lname TEXT,phone TEXT)"

handle_Db(DBfile,create_table_sql) #create DB

insert_data_sql = " INSERT INTO users VALUES ('shalom','vanunu','0547590807') "

handle_Db(DBfile, insert_data_sql)


















