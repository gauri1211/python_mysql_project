import mysql.connector as m
from sqlalchemy import create_engine
import pandas as pd
import pymysql

mycon=m.connect(
    host="localhost",
    user="root",
    password="1234",
    database="practicedb"
)

if mycon.is_connected():
    print("connection established!");

query = "select * from emp_a;"  #

name_=input("enter your name: ")
query2=("select * from emp_a where name='{}' ;".format(name_))

df1=pd.read_sql(query,mycon)

df2=pd.read_sql(query2,mycon)
print(df1)
print()
print(df2)

#writting into sql
