# python學習筆記

## 第二十七課：I:O過程使用with指令

### 1.基本流程

在文件流中，一整套基本流程就是`open-read-close`

&nbsp;

在日常中，如果我們開啟文件流運作（I：O），一定要注意關閉（close），不然下次打開會出現錯誤

```
stream = open('text.txt', 'wt')
stream.write('Lorem ipsum dolar')
stream.close() # 非常重要，關閉流
```

&nbsp;

### 2.with指令

有時我們為了防止錯誤，例如對文件沒有讀寫權限、文件不存在等，我們會使用`try-finally`來處理，即使前面錯誤亦保證會關閉流

```
try:
    stream = open('text.txt', 'wt')
    stream.write('Lorem ipsum dolar')
finally:
    stream.close() # 再次提示，非常重要，關閉流
```

&nbsp;

如果要簡便一些，我們可以使用`with`來處理，這樣就不用自己關閉流了，也有`try-finally`的效果

```
with open('text.txt', 'wt') as stream:
    stream.write('Say my name:Heisenberg')
```
