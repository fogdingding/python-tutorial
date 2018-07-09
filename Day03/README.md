## 洗資料-針對資料的部分進行篩選、處理的部分

再處理的時候，因這次的case主要在進行CSV檔案的處理，屬於結構化資料，還蠻好處理的，這邊簡單介紹兩個比較好用的套件

#### 這邊是py3裡面有import的東西。
1. [Pandas](https://pandas.pydata.org)
2. [csv](https://docs.python.org/3/library/csv.html)

-----
####這邊主要介紹pandas的簡單寫法
[網站參考](https://oranwind.org/python-pandas-ji-chu-jiao-xue/)
[網站參考](https://medium.com/@yehjames/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-3%E8%AC%9B-pandas-%E5%9F%BA%E6%9C%ACfunction%E4%BB%8B%E7%B4%B9-series-dataframe-selection-grouping-447a3fa90b60)

1. 分類
>>其實裡面主要分為 Series 欄位 以及 DataFrame 表格兩種為主要表現。

2. Series 
###### 要注意的是，這個資料為一維
``` py
import pandas as pd  # 引用套件，縮寫為pd

years = ["2016", "2017", "2018", "2019", "2020"]

Series = pd.Series(cars)  
print(Series)
``` 

3. DataFrame
###### 要注意的是，這個資料通常為二維
``` py
import pandas as pd # 引用套件，縮寫為pd

names = ["Alex", "Aaron", "Baldwin", "Berg", "Bradley", "Chester"]  
age = [50, 7, 52, 2, 8, 20]

dict = {"name": names,  
        "age": age
       }

DataFrame = pd.DataFrame(dict)

print(DataFrame) 
```


-----
####這邊主要介紹CSV的簡單寫法

1. CSV-read
``` py
#讀取檔案，並依照編號、rows印出。
with open('file_name', 'r') as csvFile:
    f_R_csv = csv.reader(csvFile)
    headers = next(f_R_csv)
    for index,row in enumerate(f_R_csv):
        print ('編號：{},DATA：{}'fomat(index,row))
```

2. CSV-Wirter
``` py
#寫入檔案，這邊簡單寫入data一個字串而已。
with open('file_name', 'w') as csvFile:
    f_W_csv = csv.writer(csvFile)
    writer.writerow('data','is','where')
```

3. CSV-a
``` py
#新增寫入檔案裡面。
with open('file_name', 'a') as csvFile:
    f_W_csv = csv.writer(csvFile)
    writer.writerow('data2','is','where')
```

------
#### 這邊主要介紹在這次專案上，有應用到的一些函數

1. locals 自動生產變數
[參考網站](http://www.runoob.com/python/python-func-locals.html)
``` py
for index in range (0,10):
    print (locals()["variable_name%s"%index])
```

2. format 字串內自動對應文字
[參考網站](http://docspy3zh.readthedocs.io/en/latest/tutorial/inputoutput.html)
``` py
print ( 'this {} format {}'.format('is','function') )
```

3. type 顯示出這個'東西'是什麼型態
``` py
print ( type ('this {} format {}'.format('is','function') ) )
```

4. split 可以指定分隔字串裡的某一個元素
[參考網站](http://www.runoob.com/python/att-string-split.html)
``` py
str = "this is split";
print str.split(' ');
```
5. len 印出所指定的'東西'的長度
``` py
print ( len('this is len') )
```

6. enumerate 與for一同使用，可以額外有目錄的效果
[參考網站](http://www.runoob.com/python/python-func-enumerate.html)
``` py
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print i, element
``` 