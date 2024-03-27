import pandas as pd
import zipfile
from sqlalchemy import create_engine
from kaggle.api.kaggle_api_extended import KaggleApi

# Init Kaggle
api = KaggleApi()
api.authenticate()

# downloading file from kaggle.com
# write to the current directory
api.dataset_download_file('anoopjohny/consumer-complaint-database/data',
                          file_name='complaints.csv',
                          path='./')

# File Names
zip_file = 'complaints.csv.zip'
csv_file = 'complaints.csv'

# Unzip the file and extract the CSV

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
     zip_ref.extractall()

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Connect to Azure SQL database
#   Values to be updated according to the environment:
#   login to database: database_user
#   user password: user_pass
#   Azure SQL server name: sql_server
#   Database to insert: database_name
#  

conn_str = 'mssql+pyodbc://database_user:user_pass@sql_server.database.windows.net:1433/database_name?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(conn_str)

# Insert csv data into the Azure SQL table complaints in database database_name
df.to_sql('complaints', con=engine, if_exists='replace', index=False,chunksize=10000)

print('Data has been successfully inserted into the Azure table.')
