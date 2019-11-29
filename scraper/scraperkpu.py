from bs4 import BeautifulSoup as Soup
import time
import csv
import requests
import traceback
import io

#Variables
seconds = 20 #DO NOT SMASH THE WEBSITE

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


#Scraping Provinsi
provinsi_list = []
provinsi_url = 'https://lindungihakpilihmu.kpu.go.id/index.php/rekap'
provinsi_html = requesttheurl(provinsi_url)
a_containers = parseprovinsitokecamatan(provinsi_html)
#Count from 5 because the 1 - 4 are table header
count = 5
while count < len(a_containers):
    nama = a_containers[count].text
    link = a_containers[count]['href']
    provinsi_list.append([nama,link])
    count = count + 1
    print('Provinsi Scraped : ',len(provinsi_list))

# printing provinsi list
# for provinsi in provinsi_list:
#   print(provinsi)

#Sleeping
print('Sleeping for '+str(seconds)+' seconds')
time.sleep(seconds)

#Scraping Kota/Kabupaten
kotakabupaten_list = []
for kotakabupaten_link in provinsi_list:
    kotakabupaten_html = requesttheurl(kotakabupaten_link[1])
    a_containers = parseprovinsitokecamatan(kotakabupaten_html)
        # Count from 6 because the 1 - 5 are table header
    count = 6
    #len(a_containers)
    while count < len(a_containers):
        nama = a_containers[count].text
        link = a_containers[count]['href']
        kotakabupaten_list.append([kotakabupaten_link[0],nama,link])
        count = count + 1
    print('Kota/Kabupaten Scraped : ',len(kotakabupaten_list))

#printing kotakabupaten list
for kota_kabupaten in kotakabupaten_list:
    print(kota_kabupaten)

#Sleeping
print('Sleeping for '+str(seconds)+' seconds')
time.sleep(seconds)

#Scraping Kecamatan
kecamatan_list = []
#Looping to get kecamatan from each Kota/Kabupaten
for kecamatan_link in kotakabupaten_list:
    kecamatan_html =requesttheurl(kecamatan_link[2])
    a_containers = parseprovinsitokecamatan(kecamatan_html)
    # Count from 7 because the 1 - 6 are table header
    count = 7
    #len(a_containers)
    while count < len(a_containers):
        nama = a_containers[count].text
        link = a_containers[count]['href']
        kecamatan_list.append([kecamatan_link[0],kecamatan_link[1],nama,link])
        count = count + 1
    print('Kecamatan Scraped : ',len(kecamatan_list))

#printing kecamatan list
for kecamatan in kecamatan_list:
    print(kecamatan)

#Sleeping
print('Sleeping for '+str(seconds)+' seconds')
time.sleep(seconds)

#Scraping Kelurahan
kelurahan_list = []
#Looping to get Kelurahan from each kecamatan
for kelurahan_link in kecamatan_list:
    kelurahan_html = requesttheurl(kelurahan_link[3])
    kelurahan_soup = Soup(kelurahan_html,"html.parser")
    kelurahan_tables = kelurahan_soup.findChildren('table')
    my_table = kelurahan_tables[0]
    rows = my_table.findChildren(['tr'])
    del rows[0]
    for row in rows:
        cells = row.findChildren('td')
        count = 0
        for cell in cells:
            count = count + 1
            if (count == 2) :
                nama = cell.string
                link = cell.a['href']
            if (count == 3) :
                tps = cell.string
        kelurahan_list.append([kelurahan_link[0],kelurahan_link[1],kelurahan_link[2],nama,link,tps])
    print('Kelurahan Scraped : ',len(kelurahan_list))

#Turn into CSV for backup
with open('list_kelurahan.csv', 'w',newline='') as csvFile:
    list_writer = csv.writer(csvFile)
    for kelurahan in kelurahan_list:
        list_writer.writerow([kelurahan[0],kelurahan[1],kelurahan[2],kelurahan[3],kelurahan[4],kelurahan[5]])

del kelurahan_list
# #Scraping Orang
# orang_list = []
# request_count = 1
# for kelurahan in kelurahan_list:
#     print(kelurahan)
#     url = kelurahan[4]
#     split_url = url.split("/")
#     pemilih_count = 1
#     while pemilih_count <= int(kelurahan[5]):
#         url = 'https://lindungihakpilihmu.kpu.go.id/index.php/rekap/pemilih/'+str(pemilih_count)+'/'+split_url[6]
#         my_url = url
#         request_count = request_count +1
#         orang_html = requesttheurl(my_url)
#         orang_soup = Soup(orang_html,"html.parser")
#         orang_tables = orang_soup.findChildren('table')
#         my_table = orang_tables[0]
#         rows = my_table.findChildren(['tr'])
#         del rows[0]
#         for row in rows:
#             cells = row.findChildren('td')
#             count = 0
#             for cell in cells:
#                 count = count + 1
#                 if (count == 2) :
#                     nama = cell.string
#                 if (count == 5) :
#                     jenkel = cell.string
#             orang_list.append([kelurahan[0],kelurahan[1],kelurahan[2],kelurahan[3],nama,jenkel])
#         print('Orang Scraped : ',len(orang_list))
#         pemilih_count = pemilih_count + 1
#         del kelurahan_list[0]
#         if(request_count % 100 == 0):
#             with open('list_orang'+str(request_count)+'.csv', 'w',newline='',encoding='utf-8') as csvFile:
#                 list_writer = csv.writer(csvFile)
#                 for orang in orang_list:
#                     list_writer.writerow([orang[0],orang[1],orang[2],orang[3],orang[4],orang[5]])
#             del orang_list
#             orang_list = []
#             time.sleep(seconds)