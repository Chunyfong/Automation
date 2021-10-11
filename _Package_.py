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

#conn = pymssql.connect(server= server, user=user, password= pw, database= database)
#Table
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+ pw)
cursor = cnxn.cursor()
#Table 1
query = "SELECT *FROM [dbo].[Table1]"

down  = pd.read_excel(' ')
down  = down ['ID'].values.tolist()
len(down)
Ms = totcount.Mach_ID.isin(down)
filtered_down = totcount[Ms]

