import csv

#READ KELURAHAN.CSV
kelurahan_list = []
with open('list_kelurahan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        kelurahan_list.append(row)
        line_count += 1
    print(f'Processed {line_count} lines.')

file_count = 1
kelurahan_split = []
#Turn into CSV for backup
for kelurahan in kelurahan_list:
    kelurahan_split.append(kelurahan)
    if(len(kelurahan_split) == 10):
        with open('scraper/iwantitsplited/list_kelurahan-'+str(file_count)+'.csv', 'w',newline='') as csvFile:
            list_writer = csv.writer(csvFile)
            for kelurahan2 in kelurahan_split:
                list_writer.writerow([kelurahan2[0],kelurahan2[1],kelurahan2[2],kelurahan2[3],kelurahan2[4],kelurahan2[5]])
        del kelurahan_split
        kelurahan_split = []
        file_count = file_count + 1