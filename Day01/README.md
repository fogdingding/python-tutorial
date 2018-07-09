# 今天如果你想爬信件的內容，可以參考這兩篇網頁寫的
1. [信件爬衝教學網站連結](http://imsardine.simplbug.com/note/email/python.html)
2. [信件爬衝教學網站連結](http://imsardine.simplbug.com/note/imap/python.html )
######## 兩個網站是同一個作者寫的
**簡單的import 東西 如果沒有就安裝吧。**
**以下用的是py3版本哦。**
``` py
import imaplib, inspect
inspect.getmro(imaplib.IMAP4_SSL)
imap = imaplib.IMAP4_SSL('imap.gmail.com')
imap.login('user@gmail.com', 'password')
#登入自己的帳號密碼 另外，因為使用gmail.com 你這邊會失敗，原因是因為你必須要把安全性給關掉。

# ('OK', ['username@gmail.com ... authenticated (Success)']) 出現這些就是成功。
imap.select()
imap.list()
# 這邊可以小小確認有沒有成功，如果有會顯示你有那些東西。
# 如'(\\HasNoChildren) "/" "INBOX"',
#   '(\\Noselect \\HasChildren) "/" "[Gmail]"',
#   '(\\HasChildren \\HasNoChildren \\All) "/" "[Gmail]/&UWiQ6JD1TvY-"',
#   '(\\HasChildren \\HasNoChildren \\Trash) "/" "[Gmail]/&V4NXPmh2-"',

imap.search(None, "UNSEEN") 
imap.search(None, "ALL")
# 取出有哪些陣列，順便有沒有OK。
# ('OK', ['1 2 3 4 5 6 7 8 9']) 如這樣

result, data = _
last_msgnum = data[0].split()[-1]
# 解果存取在last_msgnum 你會看到類似 你爬HTML的東西。

imap.fetch(last_msgnum, '(RFC822)')
# 讀取信件內容，不過我們用的RFC822的格式，這有點舊版了，新的肯定不是這樣，不過還行用拉。
result, data = _
raw = data[0][1]
# 把東西存取起來。

# 接下來使用別的地方的格式，因為eml這個東西，我沒看過，也不知道怎麼讀寫，可能是py2才有的東西，所以我把她格式更改下
# 這邊TPYE可以看出 是BYTES 是組態檔案
import email
from email.header import decode_header
# IMPORT 我所需要的內建API

# 接下來把東西轉換格式

message = email.message_from_string(raw.decode("uft-8"))
# https://stackoverflow.com/questions/606191/convert-bytes-to-a-string 參考這個

message.__class__
# 會回傳email.message.Message 應該就沒什麼問題
message['SUBJECT'] 
# 我們就有信件標頭檔案。
```
![信件標頭檔案](https://github.com/fogdingding/python-tutorial/blob/master/img/%E4%BF%A1%E4%BB%B6%E6%A8%99%E9%A0%AD%E6%AA%94%E6%A1%88.JPG)
