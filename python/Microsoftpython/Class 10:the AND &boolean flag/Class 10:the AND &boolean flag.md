# python學習筆記

## 第十課：and和布爾標記

### 1.現假設一家學校的優等生標準，最低成績不得低於70%，gpa成績必須大於等於0.85,可以用if嵌套實現

```
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >=  .85:
    if lowest_grade >=  .70:
        print('Well done')
```

gpa跟lowest中的float除了可以在input行實現，同樣也可以加在if的變量詞前面

&nbsp;

```
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if float(gpa) >=  .85:
    if float(lowest_grade) >=  .70:
        print('You made the honour roll')
```

&nbsp;

**除了用if嵌套，由於是兩個條件都相同的情況下才能達到優等生標準，所以也可以用and來表達**

<br>

**注意and是用於兩個條件必須同時滿足，而in是多個條件都同一結果，注意差別**

```
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >=  .85 and lowest_grade >=  .70:
    print('Well done')
```

**注意and的邏輯是必須同時兩個條件達成才能輸出結果：**

<br>

當第一項是，第二項是，則結果為是；

<br>

當第一項否，第二項是，則結果為否；

<br>

當第一項是，第二項否，則結果為否；

<br>

當第一項否，第二項否，則結果為否；

&nbsp;

### 2.上述情況除了可以用and來表達，還可以用布爾標記來表達,Ture和False記得首字母要大寫

```
if gpa >=  .85 and lowest_grade >=  .07:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('Well done')
```

**使用布爾標記可以減少運行時的系統負載，增加速度**
