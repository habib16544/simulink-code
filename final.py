'''import xlrd
import mysql.connector
mydb=mysql.connector.connect(host="127.0.0.1",user="root", passwd="",database="matlab")
mycursor= mydb.cursor()
loc=("C:\\Users\HP\Desktop\matlab pro\simudata.xls")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
insert_query="insert into simudata (time,voltage1,voltage2) values(%s,%s,%s)"
for r in range(1, sheet.nrows):
        simudata_time= sheet.cell(r,0).value
        simudata_voltage1= sheet.cell(r,1).value
        simudata_voltage2= sheet.cell(r,2).value
        values=(simudata_time,simudata_voltage1,simudata_voltage2)
        mycursor.executemany(insert_query, values)
        mycursor.executemany(insert_query, values)
        mydb.commit()'''


import xlrd
import mysql.connector
mydb=mysql.connector.connect(host="127.0.0.1",user="root", passwd="",database="matlab")
mycursor= mydb.cursor()
loc=("C:\\Users\HP\Desktop\matlab pro\simudata.xls")
list=list()
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)   
sheet.cell_value(0,0)
for i in range(1,51):
    list.append(tuple(sheet.row_values(i)))
insert_query="insert into simudata (time,voltage1,voltage2) values(%s,%s,%s)"
mycursor.executemany(insert_query, list)
mydb.commit()
mydb.close()    