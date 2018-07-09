import requests
from bs4 import BeautifulSoup
import re
data_7date=[]
data_3day_rain=[]
data_7day=[]
data_7day.append([])
data_7day.append([])
data_7day.append([])
global index
url = 'https://www.cwb.gov.tw/V7/forecast/town368/7Day/1001401.htm'
resp = requests.get(url)
soup = BeautifulSoup(resp.text.encode(resp.encoding),'html.parser',from_encoding='utf-8')
dcard_title = soup.find_all('td')
for index, item in enumerate(dcard_title[1:8]):
    data_7date.append(item.text.strip())
for index, item in enumerate(dcard_title[38:53]):
    data_7day[0].append(item.text.strip())
for index, item in enumerate(dcard_title[53:68]):
    data_7day[1].append(item.text.strip())
for index, item in enumerate(dcard_title[98:113]):
    data_7day[2].append(item.text.strip())
for index, item in enumerate(dcard_title[143:150]):
    data_3day_rain.append(item.text.strip())

def day0():
    print(data_7date[0])
    for x,item in enumerate(data_7day):
        print(data_7day[x][0],data_7day[x][1])
    print("降雨機率：",data_3day_rain[1])

def day1():
    print(data_7date[1])
    for x,item in enumerate(data_7day):
        print(data_7day[x][0],data_7day[x][3])
    print("降雨機率：",data_3day_rain[3])

def day2():
    print(data_7date[2])
    for x,item in enumerate(data_7day):
        print(data_7day[x][0],data_7day[x][5])
    print("降雨機率：",data_3day_rain[5])
def day3():
    print(data_7date[3])
    for x,item in enumerate(data_7day):
        print(data_7day[x][0],data_7day[x][7])

def day4():
    print(data_7date[4])
    for x,item in enumerate(data_7day):
        print(data_7day[x][0],data_7day[x][9])

def day5():
    print(data_7date[5])
    for x,item in enumerate(data_7day):
        print(data_7day[x][0],data_7day[x][11])

def day6():
    print(data_7date[6])
    for x,item in enumerate(data_7day):
        print(data_7day[x][0],data_7day[x][13])
def fucknumber():
    print('您輸入的數字是錯誤的！！')

def start_data(x):
    switch={
        '0':day0,
        '1':day1,
        '2':day2,
        '3':day3,
        '4':day4,
        '5':day5,
        '6':day6,
    }
    func=switch.get(x,fucknumber)
    return func()

for index, item in enumerate(data_7date):
    print("{0:2d}. {1}".format(index + 1, item))
selection=input("請選擇您要的天氣資料：(請輸入編號)\n")
start_data(selection)

