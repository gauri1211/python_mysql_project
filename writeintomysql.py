import mysql.connector as m
from sqlalchemy import create_engine
import pandas as pd
import pymysql

dict1={
    'sno':[4,5],
    'name':['alpha','beta'],
    'salary':[2100,30000]

}
df1=pd.DataFrame(dict1)

engine = create_engine('mysql+pymysql://root:1234@localhost/practicedb')

conn = engine.connect()

print(conn)

df1.to_sql('emp_c',conn)



# mycon=m.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="practicedb"
# )

# query = 'select * from domst;'

# dfx=pd.read_sql(query,mycon)

# print(dfx)