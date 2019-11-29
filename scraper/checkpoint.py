from bs4 import BeautifulSoup as Soup
import time
import csv
import sys
import requests
import traceback
import io
#INSERT NUMBER OF LAST KELURAHAN YOU SCRAPED
file_count = 6283 #EX.Your last scraped kelurahan list files are 10 then insert 10

#Variables
seconds = 20 #DO NOT SMASH THE WEBSITE RESPECT THE ROBOT.TXT,20 SECONDS ARE MINIMAL

def requesttheurl(url):
    trying_count = 0
    while(trying_count < 10):
        try:
            urlClient = requests.get(url)
            page_html = urlClient.text
            urlClient.close()
            return page_html
        except:
            print('Retryting after 10 Seconds')
            time.sleep(10)
            trying_count = trying_count + 1
    return None

def parseprovinsitokecamatan(html):
    page_soup = Soup(html,"html.parser")
    containers = page_soup.findAll('a',href = True)
    return containers

#Scraping Orang
request_count = 1
while (file_count <= 6283):
    #Reading kelurahan
    kelurahan_list = []
    orang_list = []
    with open('scraper/iwantitsplited/list_kelurahan-'+str(file_count)+'.csv',encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            kelurahan_list.append(row)
            line_count += 1
        print(f'Processed {line_count} lines.')
    for pemilih in kelurahan_list:
        link = pemilih [4]
        split_link = link.split("/")
        pemilih_count = 1
        print(pemilih)
        while pemilih_count <= int(pemilih[5]):
            url = 'https://lindungihakpilihmu.kpu.go.id/index.php/rekap/pemilih/'+str(pemilih_count)+'/'+split_link[6]
            my_url = url
            request_count = request_count +1
            orang_html = requesttheurl(my_url)
            orang_soup = Soup(orang_html,"html.parser")
            orang_tables = orang_soup.findChildren('table')
            my_table = orang_tables[0]
            rows = my_table.findChildren(['tr'])
            del rows[0]
            for row in rows:
                cells = row.findChildren('td')
                count = 0
                for cell in cells:
                    count = count + 1
                    if (count == 2) :
                        nama = cell.string
                    if (count == 5) :
                        jenkel = cell.string
                orang_list.append([pemilih[0],pemilih[1],pemilih[2],pemilih[3],nama,jenkel])
            print('Orang Scraped : ',len(orang_list))
            pemilih_count = pemilih_count + 1
            if(request_count % 100 == 0):
                time.sleep(20)
    with open('scraper/iwantitsplited/orang/list_orang'+str(file_count)+'.csv', 'w',newline='',encoding='utf-8') as csvFile:
        list_writer = csv.writer(csvFile)
        for orang in orang_list:
            list_writer.writerow([orang[0],orang[1],orang[2],orang[3],orang[4],orang[5]])
    del orang_list
    del kelurahan_list
    file_count = file_count + 1
    trying_count = 0

