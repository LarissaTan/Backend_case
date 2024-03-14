import pandas as pd
from sqlalchemy import create_engine, text

# Absolute path to CSV data file
csv_file_path = r'/Users/tanqianqian/Desktop/OA_Larissa/restaurants.csv'

# read the file
df = pd.read_csv(csv_file_path)

# database conection
'''
in order to run the code successfully, some of the database information need to be change base on user environment
'''
DATABASE_TYPE = 'mysql'
DBAPI = 'mysqlconnector'
HOST = '127.0.0.1'  
USER = 'root'  
PASSWORD = '12345678' 
DATABASE = 'sys'  
PORT = 3306  

engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

# create the 'restaurants' table, and set 'id' as primary key
with engine.connect() as connection:
    query = """
        CREATE TABLE IF NOT EXISTS restaurants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(128) NOT NULL,
            location VARCHAR(128) NOT NULL,
            cuisine VARCHAR(128) NOT NULL,
            rating FLOAT NOT NULL,
            contact_phone VARCHAR(20) NOT NULL,
            contact_email VARCHAR(128) NOT NULL
        );
    """
    connection.execute(text(query))

# import data into MySQL
df.to_sql('restaurants', con=engine, if_exists='append', index=False, chunksize=1000)
