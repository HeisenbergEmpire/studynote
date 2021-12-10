# python學習筆記
## 第七課：錯誤類型
### 在處理錯誤中，通常有兩個大分類，兩者區別在於

<br>

**Error handling(錯誤處理，指代碼放入運行環境後出現的無法預測的錯誤，如權限問題、數據庫改變、服務關閉等）**

<br>

**Debugging（調試，是指代碼本身的錯誤）**

&nbsp;

### 在錯誤類型中，又可分成三類，分別是

<br>

**1.syntax errors(語法錯誤）,通常比較簡單會有顯示錯處**
```
x = 42
y = 206
if x == y
    print('success')
```
結果如下
```
line 4
if x == y
         ^
SyntaxError: expected ':'
```

&nbsp;

**2.runtime errors（運行時錯誤），是第二簡單的錯誤**
```
x = 42
y = 0
print(x/y)
```
結果
```
line 10, in <module>
print(x/y)
ZeroDivisionError: division by zero
```

&nbsp;

**3.logic errors（邏輯錯誤）**
```
x = 206
y = 42
if x<y
    print(str(x) + 'is greater than' + str(y))
```
這種錯誤python不會給你提示的，只能靠自己分析

&nbsp;

### 在處理錯誤時，我們先要從頭到尾看一次錯誤提示，檢查清楚（如果是語法錯誤或者運行錯誤就比較好找出），然後看看註解（所以實際寫程序時寫註解是非常重要的），然後處理不了就上網搜索或者問f啦

&nbsp;

### 來自的微軟工程師的建議：多數錯誤還是要從代碼中尋找，所以錯誤要先從代碼中尋找，多數都不是框架內部出問題，因為框架內部出問題雖然從理論上來說有可能，但概率可以比得上中彩票
