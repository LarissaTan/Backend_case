import pandas as pd
import os
from sqlalchemy import create_engine, text

# Absolute path to CSV data file
csv_file_path = os.path.join(os.getcwd(), 'restaurants.csv')

# read the file
df = pd.read_csv(csv_file_path)

# database conection
'''
in order to run the code successfully, some of the database information need to be change base on user environment
'''
DATABASE_TYPE = 'mysql'
DBAPI = 'mysqlconnector'
HOST = 'rm-bp110at41skc47s4nzo.mysql.rds.aliyuncs.com'  
USER = 'root'  
PASSWORD = 'Tan011205' 
DATABASE = 'dashmote_case'  
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
