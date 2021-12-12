# python學習筆記

## 第八課：if

### 1.if（如果）是一種篩選方法，常用於結果篩選

&nbsp;

記得if是一連串包含代碼，結尾一定要有個冒號: 代表。。。。的情況下，即代表此行包含下面行

&nbsp;

所以包含在內的下面行全部要比第一行開頭多四個空格（也可以按tab但前期還是先要習慣四個空格）

&nbsp;

**而用於數字運算亦有多種多樣的結果用於if篩選，分別是**

```
# >(Greater than大於號)
# <(Less than小於號)
# >=(Greater than or equal to大於等於號)
# <=(Less than or equal to少於等於號)
# ==(is equal to等於號)可以參照上面理解為什麼要是兩個等於號
# !=(is not equal to不等於號)
```

&nbsp;

以下用加拿大稅法為例子，意思為：

&nbsp;

**當商品價格大於等於1元，則稅收為7%，顯示稅率；當商品價格不在大於等於1的範圍內，則稅收為0。顯示稅率:**

```
price = 0.05
if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)
```

&nbsp;

除了上述的方式，亦有下面縮略的表現方法，這種方法比較簡潔，但首先一定要讀懂語法意義，意思為：

&nbsp;

**如果商品價格大於等於1，則稅率為7%；如果商品價格不在上述範圍內的，則稅率為0。打印稅率：**

```
price = 0.05
if price >= 1.00:
    tax =  .07
else:
    tax = 0
print(tax)
```

&nbsp;

**而正式用戶使用的話，就要設為輸入式**

```
price1 = input('how much did you pay? : ')
price1 = float(price1)
if price1 >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax rate is: ' + str(tax))
```

記得加入float令數值從文字類型轉變為數字類型  和  要記得輸入str將tax從數字類型轉變為文字類型

&nbsp;

**除上述亦可以這樣簡化出來**

```
tax =  .07 if price1 >= 1.00 else 0
print('Tax rate is: ' + str(tax))
```

&nbsp;

### 2.if亦可用於文字型篩選，以下是例子

```
country = 'CANADA'
if country == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canadaian')
print()
```

從上面可以看到，出現的結果為你不是加拿大人，因為if的條件是極其苛刻的，必須完全等同結果

&nbsp;

**為此我們可以這樣處理代碼令結果不會出現誤差**

```
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canadaian')
```

這樣輸入不論大小寫，只要輸入canada結果變為小寫

&nbsp;

**以下同樣以輸入為例子**

```
country1 = input('Enter the name of your home country')
if country1.lower() == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')
```

&nbsp;

**同上，可以簡化成下面的樣子**

```
print('So you must like hockey!') if country1.lower() == 'canada' else print('You are not from Canada')
```

注意以同行簡化時，沒有縮進則不用加冒號
