#### 今天第四天，上課Data mining and Big Data processing

+ [網站參考-圖片解說](https://ithelp.ithome.com.tw/articles/10191309)
+ [網站參考-特徵工程](https://towardsdatascience.com/understanding-feature-engineering-part-1-continuous-numeric-data-da4e47099a7b)
+ [網站參考-seaborn](https://jovianlin.io/data-visualization-seaborn-part-1/)
-----
### 重要觀點

1. 正確率的迷思
>>有時候正確率高不代表好，例如，美國十年來有八千萬的旅客，但其中有80位的恐怖份子。今天我要有一個演算法來判斷是否為恐怖份子?
>>那我只需要，直接假設每一個人都不是恐怖份子，我的正確率將高達99.999....%。

2. 機器學習
>> 其實只是一種Representation，像是一種y=w1+w2+w3...，其實就是找到一組方程式來代表那個model即可。

---
### 演算法
1. gradient Descent (梯度下降演算法)
>> 找出切線，當切線趨近於0的時候將會是最佳解之一。(但容易因為，在半山腰的時候也會有切線趨近於0的狀況。)所以應用資料為凸型方可執行。

2. 混淆矩陣
>>這個是一個對於正確率迷思的議題，其中一種解釋的方法。
>>混淆矩陣
>>![混淆矩陣](https://github.com/fogdingding/python-tutorial/blob/master/img/%E6%B7%B7%E6%B7%86%E7%9F%A9%E9%99%A3.jpg)
>>混淆矩陣-題目
>>![混淆矩陣-題目](https://github.com/fogdingding/python-tutorial/blob/master/img/%E6%B7%B7%E6%B7%86%E7%9F%A9%E9%99%A3-%E9%A1%8C%E7%9B%AE.jpg)
---
1. PCA_test.py
>>引用GOOGLE的研究，算出每個字與每個字的距離(把它升維)，所以maybe，is & the的距離是很相近的。
>>另一個比較大的檔案 cbow.py

2. jieba
>>[網站參考](https://github.com/fxsjy/jieba)
>>[參考網站](https://github.com/baidu/lac)

---
### 工具介紹

1. [statsmodels](https://www.statsmodels.org/stable/index.html)
>> 關於好用的統計工具。

2. [xgboost](https://xgboost.readthedocs.io/en/latest/)
>> XGboost全名為eXtreme Gradient Boosting(極限梯度提升)，XGboost之所以被稱為Kaggle競賽神器主要是因為在Kaggle上很多比賽的第一名都使用了XGboost