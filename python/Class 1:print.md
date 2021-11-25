# python學習筆記
## 第一課 print(打印）的使用
1.print顧名思義是打印的意思，即打印框中的內容，例如

```
print('hello world')
```

  即會在結果中顯示 **hello world**
  
&nbsp;
  
  另外記得框內要有單引/雙引號(除了是命令類型打印，如第二點），並全文保持用同一種以免混亂

&nbsp;

2.print也可以print出一個指令的內容，例如

```
name = input('你的大名:')
print(name)
```
即可在結果中顯示輸入**你的大名：**然後輸入後下一行會出現對應輸入的文字

&nbsp;

3.print可以在括號內輸入\n來換行顯示，例如

```
print（'你的名字\n我的姓氏'）
```
則結果中顯示為:
<br>
**你的名字**
<br>
**我的姓氏**

&nbsp;

另外如果用print（）做一行指令，結果中則出現空行一條

&nbsp;

4.print也可以檢查算式錯誤，例如
```
print('Adding number')
x = 10 + 2
print('Performing division')
y = x / 0
print('Math complete')
```
則會在結果中出現除數不能等於0的錯誤提示，算式沒有問題則不會提示
