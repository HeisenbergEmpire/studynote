# python學習筆記

## 第九課：elif & in

### 1.如果有多個篩選項目，只用if-else就太重重複複，這時就可以用elif（否則如果），還是要謹記後面要有冒號

&nbsp;

雖然下面也可以全用if來代替elif，但其實電腦運行起來邏輯上會連貫點快一點

&nbsp;

以下以加拿大部分省份稅率為例:

```
province = input('what provinve do you live in? ')
if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print('Tax rate is: ' + str(tax))
```

elif後面亦可以繼續加用else

&nbsp;

### 2.上面由於Alberta和Nunavut省的稅率是一樣的，所以我們可以縮略寫成這樣

```
sheng = input('what sheng do you live in? ')
if sheng == 'Alberta' \
    or sheng == 'Nunavut':
    tax = 0.05
elif sheng == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print('Tax rate is: ' + str(tax))
```

**or的邏輯為：**
<br>
第一項是，第二項是，則結果為是；
<br>
第一項是，第二項否，則結果為是；
<br>
第一項否，第二項是，則結果為是；
<br>
第一項否，第二項否，則結果為否；

&nbsp;

**斜槓是代表本來是一行的意思，可用於多行轉接；冒號是代表擴在那個條件（如if、else、elif、or）之下**

```
if sheng == 'Alberta' or sheng == 'Nunavut':
    tax = 0.05
elif sheng == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print('Tax rate is: ' + str(tax))
```

&nbsp;

### 3.當有多個or選項時，我們則可以直接用in來縮略，注意只能用於多項條件為同一結果的前提下（上例只有兩個條件也可用in，看起來更簡潔）

&nbsp;

只要在前面前置了tax為0，當輸入項不在if條件內，則反應結果為0

```
sheng1 = input('what sheng1 do you live in? ')
tax = 0

if sheng1 in ('Alberta', \
              'Nunavut','Yukon'):
    tax = .05
elif sheng1 == 'Ontario':
    tax = 0.13
print('Tax rate is: ' + str(tax))
```

&nbsp;

**上述與前面or一樣，斜槓可縮略為if同行（估計上述是為了教課邏輯要清晰才會那樣）**

```
if sheng1 in ('Alberta','Nunavut','Yukon'): 
    tax = .05
elif sheng1 == 'Ontario': 
    tax = 0.13
else: 
    tax = 0.15
print('Tax rate is: ' + str(tax))
```

&nbsp;

### 4.if和其他一樣，可以多重嵌套，雖注意這樣要滿足第一個條件才可繼續第二個條件

```
country = input('What country do you live in? ')

if country.capitalize() == 'Canada':
    sheng2 = input('What sheng2/state do you live in? ')
    if sheng2.capitalize() in ('Alberta', \
              'Nunavut','Yukon'):
        tax = .05
    elif sheng2 == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.00
print('Tax rate is: ' + str(tax))
```

按照邏輯順序，將省的問題插到了嵌套中間。加上了capitalize就不用擔心用戶輸入大小寫的關係引致if檢驗錯誤的問題

&nbsp;

### 最後要非常注意，由於if語句有一定複雜性，一定要每一行檢查清楚以免造成錯誤bug
