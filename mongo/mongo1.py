from pymongo import MongoClient
import csv
client = MongoClient('mongodb://localhost:27017')
db = client['teknofestdb']
listorang = db.listorangcoba
print(listorang)
x = 6283
#READ ORANG.CSV
while x <= 6283:
    orang_list = []
    with open('scraper/iwantitsplited/orang/list_orang'+str(x)+'.csv',encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            orang_list.append(row)
            line_count += 1
        print(f'Processed {line_count} lines.')
    for orang in orang_list:
        provinsi = str(orang[0])
        nama = str(orang[4])
        jenkel = str(orang[5])
        input = {
            'provinsi' : provinsi,
            'nama' : nama,
            'kelamin' : jenkel
        }
        result = listorang.insert_one(input)
        print(result)
    x = x+1
    print(x)
    del orang_list


listorang.create_index([('nama', 'text')])

orangorang = listorang.find({"$text": {"$search": 'Malik'}})
for orang in orangorang:
    print(orang)