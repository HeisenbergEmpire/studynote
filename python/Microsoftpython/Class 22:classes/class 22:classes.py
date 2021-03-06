# 以下是本課例子，記得類（class）的名稱，約定俗成使用駝峰命名法，即每個單詞的首字母均為大寫，並且第二個字母為小寫。
# 在此處一些命名當中有使用到雙下劃線（__），這是為了讓Python識別這些特殊名稱，並且讓Python不要讓使用者直接使用這些特殊名稱。
# 而有另一些命名有使用到單下劃線（_），為了讓Python識別這些特殊名稱，但Python會讓使用者直接使用這些特殊名稱。是一種警告，可以改值但不明白就不要亂改
class Presenter():
    # 類裡面的函數中，self是一個特殊的變數，代表類別本身，必須要在括號的第一位。
    # 這是Python的一個約定的命名，不需要我們自己去宣告，Python會自動宣告。
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Say my name, {}'.format(self.name))
# 以下將體驗類的用處，例如那個name屬性，就是類當中創造出來的，presenter就是一個物件，這個物件有一個name屬性，其值為name。
# White是必須要給予的值，不然會出錯。如果空值python將自動給予類運行中一個自動預設值，此時由於類運行為自動預設值，下文為空值就報錯
presenter = Presenter('White')
presenter.name = 'Heisenberg'
presenter.say_hello()

print()
# 下面是property的用法，他能使一個函數成為一個屬性，並且可以自動計算，並且可以自動更新。
class Presenter():
    def __init__(self, name):
        self.name = name
    # 下面操作相當於把self.name寫死，不能變更，只能讀取，因為name這之後將變成一個屬性。
    # 這個環節稱為getter
    @property   
    def name(self):
        return self.__name
    # property之後便伴隨一個setter，這個setter可以讓name變更，因為name這之後將變成一個屬性。
    @name.setter
    def name(self,value):
        self.__name = value

presenter = Presenter('White')
presenter.name = 'Heisenberg'
print('Say my name, {}'.format(presenter.name))

print()
# 類的用途很廣泛，包括python中一些例如.upper()/.lower()/.title()等函數，以及資料庫的操作，這些函數都是類的方法。
# 只不過這些基礎的類所創造出來的屬性，是c語言寫出來的
# 下面是另一個類的例子，他可以讓使用者輸入一個數字，並且輸出他的平方。
class Square():
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    
square = Square(5)
print(square.area())
