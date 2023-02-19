import csv
#csv file has 2 parts header and record
c_col=['ID','Name','Age']#defininng header
dict_data=[{'ID':1,'Name':'Abbas','Age':13},
           {'ID':2,'Name':'Abina','Age':16},
           {'ID':3,'Name':'Abhiraj','Age':15},
           {'ID': 4, 'Name': 'Abhirami', 'Age': 25},
           {'ID': 5, 'Name': 'Ajel', 'Age': 17},
           {'ID': 6, 'Name': 'Akash', 'Age': 26},
           {'ID': 7, 'Name': 'Akhil', 'Age': 12},
            {'ID': 8, 'Name': 'Akhila', 'Age': 22},
           {'ID': 9, 'Name': 'Akku', 'Age': 42},
         {'ID': 10, 'Name': 'Akhil', 'Age': 32},
           ]
try:#starting write operation
    with open("name.csv","w")as f:
        write=csv.DictWriter(f,fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)

except IOError:
    print("input/output error")
d=csv.DictReader(open("name.csv"))
print("CSV file output is:")
for i in  d:
    print(i)
