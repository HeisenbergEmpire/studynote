# 回歸到除以0的錯誤講起
x = 42
y = 0
print()
# 以下是一組幫助糾錯的代碼，try即嘗試運行
# except即出現zerodivision的錯誤（e=error：）就會出現Not allowed to divide by zero
# else即如果不是zerodivision錯誤就會出現Something else went wrong
# finally最後就會都會顯示出This is our cleanup code
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
