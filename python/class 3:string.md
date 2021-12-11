# python學習筆記

## 第三課 變量詞

### 1.變量詞即框括一段字或者數字的代理詞，例如

```
first_name = 'heisenberg'
```

如上，first_name就代表了變量內容**heisenberg**，當print出first_name時就會出現**heisenberg**而不是first_name

&nbsp;

### 2.變量詞之間可以用+號作聯繫，例如

```
first_name = 'heisenberg'
last_name = 'chueng'
print(first_name + last_name)
print('Hello,' + first_name.capitalize()+ ' ' + last_name.capitalize())
```

如上，print出的結果就是**heisenbergchueng**和下段**Hello,Heisenberg Chueng**,其中first_name.capitalize()+和+last_name.capitalize()之間的單引號對代表空格

&nbsp;

### 3.變量詞亦方便對變量內容的前後加上命令，例如上面2.的部分，capitalize（）便是首字母大寫的命令，下面再加以演示

```
# 以下命令釋義：upper是全大寫，lower是全小寫，capitalize是首字母大寫，count是計算，例子中count的意思為計算a字母在sentence變量值中a出現的次數
sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))
```

&nbsp;

### 4.除了在變量詞前後可以加以命令，也可以在變量內容裡面加上命令，例如

```
ming = input('what is your ming?')
xing = input('what is your xing?')
print('Hello,' + ming.capitalize() + ' '\
    + xing.capitalize())
```

如上，加上input令輸入結果輸入變量內容成為變量詞的框括內容
