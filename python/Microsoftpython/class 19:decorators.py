# 原代碼3種演繹方式
def wrapper(funa):
    for a in ['Logging execution', funa, 'Done logging']:
        print(a)

aaa = str('-- Inside aaa function')

wrapper(aaa)

print()

def wrapper1(funb):
    print('Logging execution')
    print(funb)
    print('Done logging')

wrapper1(aaa)

print()

def wrapper2(func):
    print('Logging execution')
    func()
    print('Done logging')

def bbb():
    print('-- Inside aaa function')

wrapper2(bbb)

print()

# 改變成函數裝飾器演繹
# 函數logger輸入物標記為fund
def logger(fund):
# 函數logger嵌套物為函數wrapper3
    def wrapper3():
        print('Logging execution')
        fund()
        print('Done logging')
# fund()意思是fund是一整塊輸入物
    return wrapper3

# 先把函數logger設為裝飾器
@logger
# 定義ddd函數意義
def xxx():
    print('-- Inside sample function')

# 此處為在logger裝飾器環境底下運行ddd函數，即ddd函數是logger裝飾器環境的變量
xxx()

# 謹記裝飾器只能用於函數（def）