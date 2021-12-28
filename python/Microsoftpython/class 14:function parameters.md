# python學習筆記

## 第14課：函數def的更多運用與注意

&nbsp;

### 1.以上一課內容為例子，輸出首字母

```
def get_initial(name):
    xxx = name[0].upper()
    return xxx

first_name = input('Enter your first name:')
first_name_initial = get_initial(first_name)

print('Your initial is:' + first_name_initial)
```

&nbsp;

**如果想讓用戶自定義，是否想採用字母大寫的話(注意使用布爾變量的參數是沒有必要事先標註True or False的)**

```
def getinitial(name,force_uppercase):
    if force_uppercase:
        xxx = name[0].upper()
    else:
        xxx = name[0]
    return xxx

first_name = input('Enter your first name:')
force_uppercase = input('True or False:')

first_name_initial = getinitial(first_name,force_uppercase)

print('Your initial is:' + first_name_initial)
```

&nbsp;

**如果上述函數想直接將值鎖定為大寫，則如下：**

```
def getinitial(name,force_uppercase=True):
    if force_uppercase:
        xxx = name[0].upper()
    else:
        xxx = name[0]
    return xxx

first_name = input('Enter your first name:')

first_name_initial = getinitial(first_name)

print('Your initial is:' + first_name_initial)
```

&nbsp;

### 2.如果想讓代碼更易理解，應該如下將參數命名(這樣不僅能讓代碼更易理解，且不用管參數順序)：

```
def getinitial(name,force_uppercase):
    if force_uppercase:
        xxx = name[0].upper()
    else:
        xxx = name[0]
    return xxx

first_name = input('Enter your first name:')
forceuppercase = input('Ture or False:')

first_name_initial = getinitial(force_uppercase=forceuppercase,name=first_name)

print('Your initial is:' + first_name_initial)
```

&nbsp;

**這樣命名的好處是很有作用的，如下是某程序員希望代碼錯誤時給出提示，希望人們講這段代碼儲存起來**

```
def error_logger(error_code,error_severity,log_to_db,\
                 error_message,source_module):
    print('oh no error:' + error_message)

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(68,1,True,'Second number greater than first',\
                 'my_math_method')
```

&nbsp;

**如上，實在只會讓人看得時一臉懵逼，如果加上命名就清晰多了，如下：**

```
def error_logger(error_code,error_severity,log_to_db,\
                 error_message,source_module):
    print('oh no error:' + error_message)

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code=79,error_severity=1,
                 log_to_db=True,
                 error_message='Second number greater than first',
                 source_module='my_math_method')
```

# 最後總結，對參數進行命名是益處多多，要注意養成這良好習慣