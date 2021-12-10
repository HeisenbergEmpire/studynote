# python學習筆記
## 第七課之二：try/excerpt/finally
### 回歸到除以0的錯誤講起
```
x = 42
y = 0
print(x / y)
```
這樣肯定出現錯誤

&nbsp;

以下是一組糾錯代碼
```
x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
```
try即嘗試運行
<br>
except即出現zerodivision的錯誤（e=error：）就會出現Not allowed to divide by zero
<br>
else即如果不是zerodivision錯誤就會出現Something else went wrong
<br>
finally最後就會都會顯示出This is our cleanup code