# Package_for Data Clean
import pymssql
import pyodbc
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#Pandas Setting
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', None)

"{:.2f}".format(5)

# Analytics & Viz Library
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# SQL Database Login ID
server =
user =
pw =
database =

# For Azure Interactive Login
db = ' '
username ='secretid@'
Authentication= 'ActiveDirectoryInteractive'
driver= '{ODBC Driver 17 for SQL Server}'

#conn = pymssql.connect(server= server, user=user, password= pw, database= database)
#Table
#Linked Server can use this connection as well
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+ pw)
cursor = cnxn.cursor()

# For Azure 
conn = pyodbc.connect('DRIVER='+driver+
';SERVER='+server+
';PORT= ;DATABASE='+db+
';UID='+username+
';AUTHENTICATION='+Authentication
)
print(conn)

#Table 1
query = "SELECT *FROM [dbo].[Table1]"

#SQL Para
params = {
    # all rows after this timestamp, 7 days ago relative to 'now'
    'latest': datetime.datetime.today() - datetime.timedelta(days=30),
    # if date *only* (no time component), use
    # 'earliest': datetime.date.today() - datetime.timedelta(days=7),
}

df = pd.read_sql("""
  bababa,
  where [PARTS_DATETIME] >= %(latest)s
    """, params=params, con=conn)


#Date
# Date
df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y %I:%M:%S %p')
df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y %H:%M:%S.%f')
# Chop the timestamp
df['DATE']=df.DATE.dt.date
# Filter by Period
df =df[(df['DATE']> "2018-12-30") & (df['DATE']< "2020-01-01")]
# Return Daily Max Data
df2 = df.groupby(['ID','DATE'],as_index=False).max()

# Reindex
filter_df = (df2.set_index('DATE').groupby('ID').apply(lambda d: d.reindex(pd.date_range(min(d.index),max(d.index),freq='D')))
             .drop('ID', axis=1).reset_index('ID').ffill().bfill().reset_index())
filter_df.rename(columns={"index":"Date"}, inplace=True)

# Merge
df1 = m.merge(df2, on = ['ID', 'DATE'], how = 'left')
#Fill the empty data for Right hand size
master = master1.ffill().bfill()
# 
df1['E'] = df1['E'].fillna(0)
test['E_Csum'] = test.groupby(['ID'])['E'].apply(lambda x: x.cumsum())

down  = pd.read_excel(' ')
down  = down ['ID'].values.tolist()
len(down)
df_check = df2[df2.ID.isin(down)]

#setting up Bat script for window schedule
call C:\Users\Anaconda3\Scripts\activate.bat
start C:\Users\Anaconda3\envs\ML_Env1\python.exe "cd Python Script Path\Automation.py"
