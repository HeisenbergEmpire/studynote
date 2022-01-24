# python學習筆記

## 第19課 裝飾器

### 1.裝飾器是給代碼添加功能的方法，只適用於函數，常見是把網上的裝飾器調用到自己的代碼上，例如

```
# snippet from flask
# register http://myserver/api/products

@route('api/products')
def get_products:
    # code to list from database
    pass
```

&nbsp;

### 2.裝飾器的原理，則如下，其實是用另一組函數當作框架

```
# 原代碼的三種例子

# 原代碼1
def wrapper(funa):
    for a in ['Logging execution', funa, 'Done logging']:
        print(a)

aaa = str('-- Inside aaa function')

wrapper(aaa)

# 原代碼2
def wrapper1(funb):
    print('Logging execution')
    print(funb)
    print('Done logging')

aaa = str('-- Inside aaa function')

wrapper1(aaa)

# 原代碼3
def wrapper2(func):
    print('Logging execution')
    func()
    print('Done logging')

def bbb():
    print('-- Inside aaa function')

wrapper2(bbb)

# 用裝飾器方式演繹

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
```

&nbsp;

## 謹記裝飾器只能用於函數（def）