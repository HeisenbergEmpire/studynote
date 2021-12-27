# python學習筆記

## 第13課：函數def

&nbsp;

### 1.例子，求運行一段代碼運行完畢的所需時間（也是調試技巧之一，看代碼運行速度）

&nbsp;

```
import datetime

first_name = 'Heisenberg'
print('task completed')
print(datetime.datetime.now())

print()

for x in range (0,10):
    print(x)
first_name = 'Heisenberg'
print('task completed')
print(datetime.datetime.now())
```

&nbsp;

**如上，其中有兩段代碼是一樣的，那我們可以儲存一個函數（模板），此模板改名為print_time,後面直接取用**

&nbsp;

```
def time_print(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Heisenberg'
time_print('first name assigned')

for x in range(0,10):
    print(x)
time_print('loop completed')
```

&nbsp;

### 2.接下來是另外一個例子，提取首字母([0:1]部分可以直接用[0]代替，作用一樣)

&nbsp;

```
firstname = input('Enter your first name:')
first_name_initial = firstname[0:1]
lastname = input('Enter your last name:')
last_name_initial = lastname[0:1]

print('Yout initials are:' + first_name_initial + last_name_initial)
```

&nbsp;

**以下是def簡化，意思為當input接收了一個值後，按name[0:1]的模式return（返回）一個值給get_initial()**

&nbsp;

```
def get_initial(name):
    xxx = name[0:1]
    return xxx

firstname = input('Enter your first name:')
first_name_initial = get_initial(firstname)

lastname = input('Enter your last name:')
last_name_initial = get_initial(lastname)

print('Yout initials are:' + first_name_initial + last_name_initial)
```

&nbsp;

xxx部分只是隨便起個名代表get_initial()，所以要return給xxx(即get_initial())

&nbsp;

**而想變成大寫字母（加入後續項）的話，只需像下面這樣**

&nbsp;

```
def get_initial(name):
    xxx = name[0:1].upper()
    return xxx

firstname = input('Enter your first name:')
first_name_initial = get_initial(firstname)

lastname = input('Enter your last name:')
last_name_initial = get_initial(lastname)

print('Yout initials are:' + first_name_initial + last_name_initial)
```

&nbsp;

### 4.還可以簡化成這樣，少打兩行字

&nbsp;

```
def get_initial(name):
    xxx = name[0:1].upper()
    return xxx

firstname = input('Enter your first name:')

lastname = input('Enter your last name:')

print('Yout initials are:' + get_initial(firstname) + get_initial(lastname))
```

&nbsp;

# 平時在def段之前加上註釋