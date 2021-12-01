# python學習筆記
## 第五課 數字與變量詞
1.變量詞與數字結合運用，可用於運算，幫數字起有意義的變量詞名有助於理解
```
pi = 3.14159
print(pi)
```
如上，便可打印pi值

&nbsp;

2.將變量詞用於數字的運算，如下，加減乘除分別對應+-*/，注意指數（冪）的符號是**（雙星號）
```
first_num = 6
second_num = 3
print(first_num + second_num)
print(first_num - second_num)
print(first_num * second_num)
print(first_num / second_num)
print(first_num ** second_num)
```

&nbsp;

3.當需要運用python語言做數字型變量詞和文字拼接時，python會搞不清狀況，到底是像數字般進行加減乘除運算，還是像文字型變量詞字符串般進行拼接
```
day_in_feb = 28
print(day_in_feb + ' day in February')
```
如上會顯示錯誤，正確做法需要加上str將數字性變量詞轉換成文字型變量詞，才可以與文字進行拼接，以下是正確做法

&nbsp;

```
day_in_feb = 28
print(str(day_in_feb) + ' day in February')
```
輸出結果為 28 day in February

&nbsp;

同樣，str轉換後的數字型變量詞亦適合使用佔位符{}和format，因為str已經將數字型變量詞的屬性改變為文字型變量詞，還可以在str括號內進行運算，如下
```
word = 'day in february'
output = f'{str(day_in_feb + second_num)} {word} '
print(output)
```

&nbsp;

4.有時，python無法識別變量詞屬性到底是數字還是文字，例如以下兩例
```
first_numb = '5'
second_numb = '6'
print(first_numb + second_numb)
```
如上，兩變量詞因為變量值中存在單引號，python便認為5和6是文字屬性，於是進行了拼接而不是數學運算

&nbsp;

```
first_number = input('Enter first number')
second_number = input('Enter second number')
print(first_number + second_number)
```
如上，因為input輸入被定義為文字屬性變量詞，所以結果進行了拼接而不是數學運算

&nbsp;

在這些時候，與str功能相反的int和float，將文字屬性變量詞轉換成數字屬性變量詞
<br>
int是計算出整數（只能用於無小數點計算），float是計算出浮點數（有小數點），例子如下
```
first_number = input('Enter first number')
second_number = input('Enter second number')
print(int(first_number) + int(second_number))
print(float(first_number) + float(second_number))
````
如此，輸入項便可用於計算
