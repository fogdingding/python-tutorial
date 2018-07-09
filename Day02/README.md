# 爬蟲的第一天
這篇主要是因為在老師的要求下，去撰寫的。主要作用為，爬出氣象局的資料，在進行'洗資料'的行為。讓使用者能夠選擇七天內的氣象資料並輸出給使用者。
----
#### 這邊是py3裡面有import的東西。
1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [re](https://docs.python.org/2/library/re.html)

###### 如果有問題，pip3 install 缺少的套件即可成功執行
---
#### 爬蟲的目標網站

1. [氣象局資料]('https://www.cwb.gov.tw/V7/forecast/town368/7Day/1001401.htm')
2. [觀測站資料]('http://e-service.cwb.gov.tw/HistoryDataQuery/')
