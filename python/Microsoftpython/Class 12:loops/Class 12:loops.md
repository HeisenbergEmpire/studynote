# python學習筆記

## 第十二課：循環（for & while）

### 1.python之中僅有兩種循環，for和while

&nbsp;

以下先從for循環講起,意思為按順序打印出name變量中每一個值，直到打印完畢，終止

```
for name in ['Heisenberg', 'White', 'Walter', 'Jesse', 'Gustavo']:
    print(name)
```

&nbsp;

**下面range是代表index變量是從數字0至1**

```
for index in range(0,2):
    print(index)
print()
```
打印出從0到2之前的每個數字，打印完結束，結果是0和1

&nbsp;

### 2.下面是while的應用

&nbsp;

**意思為while（當）index的值小於name變量詞的值數量**

<br>

**則打印（name【index數值位】），index加1，（name【index數值位】），index加1**

<br>

**如此循環直到while（當）index值大於或等於name值數量，while循環結束**

```
name = ['Heisenebrg', 'White', 'Walter', 'Jesse', 'Gustavo']
index = 0
while index<len(name):
    print(name[index])
    index = index + 1
```

&nbsp;

**同樣的意義用for循環來做就更簡潔，所以可以用for就不用while了**

```
for i in name:
    print(i)
```

&nbsp;

### 且for為有限循環，循環完即停止；而while為無限循環，假若條件設錯就會造成無限循環錯誤，故儘量使用for循環為佳
