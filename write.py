
import mysql.connector as m
from sqlalchemy import create_engine
import pandas as pd
import pymysql

engine = create_engine('mysql+pymysql://root:1234@localhost/projects')

conn = engine.connect()

print(conn)

df1=pd.read_csv('python_mysql_project/QUIZ.csv')

print(df1)

df1.to_sql('quiz',conn)