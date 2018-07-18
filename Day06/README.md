### Unittest in python3
依據另一篇[Travis_CI-hello]()所寫，能夠自動化幫忙進行測試，但是測試的程式就得要自己學了。
---
###### 以下是依些基礎概念、程式語法的教學。
1. 
如果要做unittest的話，必須有兩個檔案，一個為自寫的程式，另一個為測試 自己寫的程式 的程式。
EX：circle_area.py
```py
# Garden area 
from math import pi
def circle_area(r):
    return pi*(r**2)
```
接下來我們就會建立另一個測試的部分。
EX：tset_circle_area.py
```py
import unittest
from circle_area import circle_area
from math import pi

class Test_circle_area(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >=0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)
        

if __name__=='__main__':
    unittest.main()

```
接下來執行tset_circle_area.py ， will see that
>![](https://github.com/fogdingding/python-tutorial/blob/master/img/unittest-OK.JPG)

2. 
接下來再精進測試的部分。(處理明顯會錯誤的值)
EX：tset_circle_area.py
```py
import unittest
from circle_area import circle_area
from math import pi

class Test_circle_area(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >=0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)
    
    def test_values(self):
        #make sure value errors are raised when necessary
        self.assertRaises(ValueError,circle_area,-2)
if __name__=='__main__':
    unittest.main()
```
接下來執行tset_circle_area.py ， will see that
>![](https://github.com/fogdingding/python-tutorial/blob/master/img/unittest-NO_OK.JPG)

明顯我們會看到錯誤訊息，那接下來就是要回去改原始的檔案circle_area.py。
```py
# Garden area 
from math import pi
def circle_area(r):
    if r<0:
        raise ValueError("the radius cannot be calculation")
    return pi*(r**2)
```
接下來執行tset_circle_area.py ， will see that
>![](https://github.com/fogdingding/python-tutorial/blob/master/img/unittest-OK-2.JPG)

3. 
接下來再精進測試的部分。(處理明顯會錯誤的型態)
EX：tset_circle_area.py
```py
import unittest
from circle_area import circle_area
from math import pi

class Test_circle_area(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >=0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)
    
    def test_values(self):
        #make sure value errors are raised when necessary
        self.assertRaises(ValueError,circle_area,-2)

    def test_types(self):
        #make sure type errors are raised when necessary
        self.assertRaises(TypeError,circle_area,3+5j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,'radius')
        
if __name__=='__main__':
    unittest.main()
```

接下來執行tset_circle_area.py ， will see that
>![](https://github.com/fogdingding/python-tutorial/blob/master/img/unittest-NO_OK2.JPG)

明顯我們會看到錯誤訊息，那接下來就是要回去改原始的檔案circle_area.py。
```py
# Garden area 
from math import pi
def circle_area(r):
    if type(r) not in [int,float]:
        raise TypeError("the radius must be a non-negative")
    if r<0:
        raise ValueError("the radius cannot be calculation")
    return pi*(r**2)
```

接下來執行tset_circle_area.py ， will see that
>![](https://github.com/fogdingding/python-tutorial/blob/master/img/unittest-OK-3.JPG)

4. 
理論上就是透過測試程式去驗證自己所寫的有沒有一些錯誤，進而改進自己的程式能夠完美的被執行。
為何如此大費周章呢?這牽扯到另一個概念，就是改善程式-重構的概念。
可以參考 《Refactoring – Improving the Design of Existing Code》 這本書，中文翻譯為 《重構 — 改善既有程式的設計》，雖然是JAVA為範例語言，不過還蠻值得看的。

###### 重構之前的類別圖
>![](https://github.com/fogdingding/python-tutorial/blob/master/img/%E9%87%8D%E6%A7%8B-1.png)
###### 重構之後的類別圖
>![](https://github.com/fogdingding/python-tutorial/blob/master/img/%E9%87%8D%E6%A7%8B-2.png)