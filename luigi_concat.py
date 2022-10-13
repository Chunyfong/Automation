import pandas as pd
import pymssql
import datetime
import numpy as np
import luigi
from sqlalchemy import create_engine
import datetime
import os
import shutil
import gc


# params = {'latest': datetime.datetime.today() - datetime.timedelta(days=100)}
conn = pymssql.connect(
    host=r'',
    user=r'',
    password=r'', database='Main')
cursor = conn.cursor(as_dict=True)


class TAset(luigi.Task):

    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget(r"C:\Users\xxxx\Desktop\Pipline_Data\T_A.csv")

    def run(self):
        df = pd.read_sql("""
                             xxx
        
        
                            WHERE DATEDIFF(day,[Date],GETDATE()) between 0 and 100 """, con=conn)
        
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %h:%m:%s').dt.date
        df = df.fillna(0)
        df.iloc[:, 2:] = df.iloc[:, 2:].astype("int32")
        df = df.groupby(['User_ID', 'Date'], as_index=False).max()
        df = df.drop_duplicates()
        df = (df.set_index('Date').groupby('Date').apply(
            lambda d: d.reindex(pd.date_range(min(d.index), max(d.index), freq='D')))
              .drop('User_ID', axis=1).reset_index('User_ID').ffill().bfill().reset_index())
        df.iloc[:, 2:] = df.iloc[:, 2:].astype("int32")
        df.to_csv(r'C:\Users\xxxx\Desktop\Pipline_Data\T_A.csv', index=False)


class TBset(luigi.Task):

    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget(r"C:\Users\xxxx\Desktop\Pipline_Data\T_B.csv")

    def run(self):
        df = pd.read_sql("""
            SELECT 


            xxx

            WHERE DATEDIFF(day,[Date],GETDATE()) between 0 and 100 """, con=conn)
        
        
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %h:%m:%s').dt.date
        df = df.fillna(0)
        df.iloc[:, 2:] = df.iloc[:, 2:].astype("int32")
        df = df.groupby(['User_ID', 'Date'], as_index=False).max()
        df = df.drop_duplicates()
        df = (df.set_index('Date').groupby('User_ID').apply(
            lambda d: d.reindex(pd.date_range(min(d.index), max(d.index), freq='D')))
              .drop('User_ID', axis=1).reset_index('User_ID').ffill().bfill().reset_index())
        df.iloc[:, 2:] = df.iloc[:, 2:].astype("int32")
        df.to_csv(r'C:\Users\xxxx\Desktop\Pipline_Data\T_B.csv', index=False)


class Concat(luigi.Task):

    def requires(self):
        return [TAset(), TBset()]

    def output(self):
        return luigi.LocalTarget(r"C:\Users\xxxx\Desktop\Pipline_Data\Master.csv")

    def run(self):
        a = pd.read_csv(r'C:\Users\xxxx\Desktop\Pipline_Data\T_A.csv')
        b = pd.read_csv(r'C:\Users\xxxx\Desktop\Pipline_Data\T_B.csv')
        df = b.merge(a, on=['User_ID', 'index'], how='outer')
        df = df.ffill().bfill()
        df.rename(columns={"index": "Date"}, inplace=True)
        df.iloc[:, 2:] = df.iloc[:, 2:].astype("int32")
        df['T'] = df.groupby('User_ID')['User_ID'].transform('count')
        df = df[df['T'] > 100]
        df.drop(columns='T', inplace=True)
        df = df.sort_values(['User_ID', 'Date'])
        df.to_csv(r'C:\Users\xxxx\Desktop\Pipline_Data\Master.csv', index=False)


class Clean(luigi.Task):

    def requires(self):
        return [Concat()]

    def output(self):
        return luigi.LocalTarget(r"C:\Users\xxxx\Desktop\Pipline_Data\Master.csv")

    def run(self):
        df = pd.read_csv(r'C:\Users\xxxx\Desktop\Pipline_Data\Master.csv')
        col = df.iloc[:, 1:].columns
        dif = df[col]
        dif = dif.groupby(['User_ID']).diff().fillna(0).astype('int32')
        for col in dif:
            dif[col] = np.where(dif[col] >= 0, dif[col], df[col])
        df.iloc[:, 2:] = dif
        df.to_csv(r'C:\Users\xxxx\Desktop\Pipline_Data\Master.csv', index=False)


if __name__ == '__main__':
    # Since delete all the files and folders can trigger luigi to run again
    # Anyway this works for me
    shutil.rmtree(r'C:\Users\xxxx\Desktop\Pipline_Data\')
    os.makedirs(r'C:\Users\xxxx\Desktop\Pipline_Data\')
    luigi.build([Clean()], workers=2, local_scheduler=True)
