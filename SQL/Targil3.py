import apikey
from google import genai
import sqlite3

DBFILE = "maketable.db"
# from sql.sql import DBfile

client = genai.Client(api_key=apikey.key)


def promptcheck(prompt):
    model = "gemini-2.0-flash"
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text


prompt = "make an table with the labels id ,car_name,sells_amount,production_amount and give me full 20 records on table using |. return just the table"

table = promptcheck((prompt))
list_table = table.split("\n")[3:-2]


def tabletodb(DBfile, SQL):
    connectionDB = sqlite3.connect(DBfile)
    cursor = connectionDB.cursor()
    cursor.execute(SQL)
    connectionDB.commit()
    connectionDB.close()


# make an table with the labels id ,car_name,sells_amount,production_amount and give me just the table
create_table_sql = """
    CREATE TABLE IF NOT EXISTS cars (
    id INTEGER ,
    car_name TEXT,
    sells_amount INTEGER,
    production_amount INTEGER
);
"""

# create table
tabletodb(DBFILE, create_table_sql)

for line in list_table:
    id = int(line.split("|")[1])
    car_name = line.split("|")[2]
    sells_amount = int(line.split("|")[3])
    production_amount = int(line.split("|")[4])
    SQL = f"INSERT INTO cars VALUES ({id}, '{car_name}',{sells_amount}{production_amount})"
    tabletodb(DBFILE, SQL)

# for col in list_table: