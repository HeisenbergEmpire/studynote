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