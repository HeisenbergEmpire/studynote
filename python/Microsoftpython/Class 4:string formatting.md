# python學習筆記

## 第四課 格式化字符串（即佔位符與format）

首先我們先回顧上一課的原始代碼

```
first_name = 'heisenberg'
last_name = 'chueng'
print('Hello,' + first_name.capitalize()+ ' ' + last_name.capitalize())
```

&nbsp;

### 1.加號變代碼格式化,使用{}佔位符來代表變量詞的實際位置和用format來代表變量詞的組成,以上面最後一行作改變為演示

```
output = 'Hello,{} {}'.format(first_name, last_name)
print(output)
```

最終效果將與原始代碼一樣

&nbsp;

### 2.如果要變量詞要以自己指定的位置排列，這時可以用到數字，format內第一項為數字0，類推

```
output = 'Hello,{1} {0}'.format(first_name, last_name)
print(output)
```

如上，變量詞與上一例輸出位置發生變化，謹記第一項為數字0

&nbsp;

### 3.另外，可以用{}括住變量詞直接插入，僅需在前面加上f或者F代表format（此方法僅可使用于py3及以後版本，但不可用於py3.3.2

```
output = f'Hello,{first_name} {last_name}'
print(output)
```
**当f里面每个变量词中间有空格便有空格，没有便没有**

&nbsp;

### 4.除此之外，還有這樣一種佔位用法,至此僅供參考

```
output4 = 'Hello,%s %s'%(first_name, last_name)
print(output4)
```
