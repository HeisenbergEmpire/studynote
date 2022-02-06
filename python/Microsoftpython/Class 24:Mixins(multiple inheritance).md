# python學習筆記

## 第24課：多重繼承

### 1.多重繼承就是用一個class來繼承多個父類class，但使用多重繼承一定要特別小心出錯，以下為本課例子

```
# 以下為本課例子，假設現在有登陸與連結的兩個數據庫功能
class Loggable:
    def __init__(self):
        self.title = ''
    def log(self):
        print('Log message from ' + self.title)

class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print('Connecting to database on ' + self.server)

# 假設我們想要把這兩個功能都加入到我們的程式中，我們可以用多重繼承來實現這個目標
class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__() # 呼叫兩個父類別的__init__()函數，所以下面要將兩個父類未定義的屬性設定給子類
        self.title = 'Sql Connection Demo'
        self.server = 'Some_Server'
```

### 2.接下來我們看看加入操作的方法和顯示內容，其中framework函數起到篩選的效果，如果只是想登陸就不用連結

```
# 以下函數為篩選是登陸還是連結的函數
def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()

# 以下由於使用SqlDatabase類別，所以會執行兩個父類別的__init__()函數
sql_connection = SqlDatabase()
framework(sql_connection)

print()

# 以下由於使用Loggable類別，所以只會執行一個父類別的__init__()函數
class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just Logging'

just_log = JustLog()
framework(just_log)
```

&nbsp;

**顯示結果如下**

```
Connecting to database on Some_Server
Log message from Sql Connection Demo

Log message from Just Logging
```

&nbsp;

需要對應會兩個父類函數參考
