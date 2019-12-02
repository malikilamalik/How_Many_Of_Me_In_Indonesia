# Nama yang sama

Aplikasi berbasi web,untuk mencari jumlah nama yang sama.
Data diambil dari website rekapitulasi KPU

## Installation
### Prerequisites
Python  
Nodejs  
### Install Python and Nodejs libraries
1.Download this repository  
2.create Python Virtual environment  
3,Use pip to install the libraries  
`pip install -r requirements.txt`  
4.install package.json  
`npm install`  
### Scraping the dataset
1.run splitting.py  
`python scraper/splitting.py`  
2.open the checkpoint.py file  
checkpoint.py is a program to scrape the dataset,if you don't want to scrape specific dataset don't change anything from this file  
3.run the checkpoint.py file  
`python scraper/checkpoint.py`  
### Import the dataset to mongodb
1.run the checkpoint.py file  
`python mongo/mongo1.py`  
if you don't scrape specific dataset don't change anything from this file  
### Run the website
1.Build the frontend  
'npm run dev'  
2.Run the server  
'Python website/totalnamaapi/manage.py runserver'  
## License
[GNU General Public License v3.0](https://github.com/defdotpy/HowManyOfMe_In_Indonesia/blob/master/LICENSE)

[![defdotpybadge](https://i.imgur.com/FepXuRN.png)](https://github.com/defdotpy)
