'''import xlrd
import MySQLdb
mydb= MySQLdb.connect(host="127.0.0.1", user="root", password="",database="all_db")
with open('simudata.xls') as xls_file:
    xlsfile= xlrd(xls_file, delimiter=',')
    all_value= []
    for row in xlsfile:
        value= ( row[0], row[1], row[2])
        all_value.append(value)
query= "insert into `matlab` (`time`, `voltage1`, `voltage2`) values (%s,%s,%s)"
mycursor= mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()'''

from tkinter.tix import Select
import mysql.connector
import csv
mydb=mysql.connector.connect(host="127.0.0.1",user="root", passwd="",database="matlab")
#mycursor=mydb.cursor()
#for connection check
'''print(mydb)
if(mydb):
    print("connection successful")
else:
    print("unsuccessful") 
#check all database
mycursor.execute("show databases")      
for db in mycursor:
    print(db)
#insert data into table
sqlform="insert into simudata (time,voltage1,voltage2) values(%s,%s,%s)" 
simudatas = [(1,10,15),(2,20,30),]   
mycursor.executemany(sqlform,simudatas)
mydb.commit()
#read data from database
mycursor.execute("Select * from simudata")
result=mycursor.fetchall()
for row in result:
    print(row)'''
with open('simudata.xls') as csv_file:
    csvfile= csv.reader(csv_file, delimiter=',')
    all_value= []
    for row in csvfile:
        value= ( row[0], row[1], row[2])
        all_value.append(value)
query= "insert into `simudata` (`time`, `voltage1`, `voltage2`) values (%s,%s,%s)"
mycursor= mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()
