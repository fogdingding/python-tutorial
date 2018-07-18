### 今天上課-Data mining and Big Data processing

+ [參考網站-code範例](https://github.com/mc6666/DataScience) 
----
#### 課程大綱

+ 資料科學入門
>+ 資料分析與套件介紹
>+ 資料料科學實作的生命週期

+ 機器學習理解與實作
>+ 各演算法介紹
>+ SciKit learn實作

+ 深度學習理解與實作
>+ Neural Network fundamentals
>+ 演算法介紹 CNN、CLP/RNN
>+ 應用實例介紹

----
### 簡單範例
1. flask_test.py 
>> 簡單web範例，[flask](http://flask.pocoo.org/)，是一個輕量化的框架。

2. run_keras_server_my.py
>> 一個機器學習的範例，丟一個圖，它會判斷是否為狗。

3. FirstDetection.py
>> 一個機器學習的範例，它是輸入一張圖片，會圈出特定物件後在輸出一張圖片給使用者

4. 聲明式(圖形化介面)[Microsoft Azure Machine Learning Studio](https://studio.azureml.net/) 
>> 微軟研發的一個，圖形化的機器學習。
---

---
### 工具介紹
1. [jupyter notebook](http://jupyter.org/)

##### 安裝
``` sh
$pip3 install jupyter  
```
##### 在執行就可以了
``` sh
$jupyter notebook
```

2. [anaconda](https://anaconda.org/)

###### 安裝的話，去官網載一下即可。
>>方便的多環境開發版本
``` sh
$conda creadte -n py35 python=3.5 anaconda
```
>>查看我現在所在的版本分之
``` sh
$conda info --e 
``` 
>>切換到我所需要的分支
``` sh
$source activate python34
``` 
##### 主要按鍵
>>SHIFT+ENTER 執行並跳下一行
>>CTRL+ENTER 執行並留在同一行
>>點左邊IN[] 顏色變成藍色之後 按下'A'鍵 可以在那一欄新增上面一行
>>點左邊IN[] 顏色變成藍色之後 按下'B'鍵 可以在那一欄新增上面一行

![jupyter](https://github.com/fogdingding/python-tutorial/blob/master/img/jupyter-00.JPG)



3. [VScode](https://code.visualstudio.com/)
>>在打開之後，左邊有一個蟲蟲，點下去之後，點選偵錯>新增組態 如圖所示

![VScode](https://github.com/fogdingding/python-tutorial/blob/master/img/VScode.JPG)

>>如果要偵錯的話，就在數字的左邊點一下，之後去找蟲蟲在按執行即可 如圖所示

![VScode-00](https://github.com/fogdingding/python-tutorial/blob/master/img/VScode-00.JPG)

![VScode-01](https://github.com/fogdingding/python-tutorial/blob/master/img/VScode-01.JPG)

4. [matplotlib](https://matplotlib.org/)
>>主要是作為python的圖像化，想要啥圖，就上網參考一下即可。

4. [Bokeh](https://bokeh.pydata.org/en/latest/)


5. [seaborn](https://seaborn.pydata.org/)

6. [pandas](https://pandas.pydata.org/)

7. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)