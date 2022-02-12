# python學習筆記

## 第二十六課：文件I:O

### 1.文件流

在python中想修改文件的内容，可以使用open()函数，稱為stream文件流

&nbsp;

格式如下:

```
# stream = open(filename, mode, buffer_size)
# filename: 文件名
# buffer_size: 文件缓冲区大小，默认为1

# mode: 文件打开模式:
# r: read mode, 只读模式
# w: write mode, 只写模式（覆蓋原有文件）
# a: append mode, 插入模式（寫入新的内容，不覆蓋原有文件）
# r+: read and write mode, 读写模式
# w+: write and read mode, 读写模式
# a+: append and read mode, 追加读模式
# x: create mode, 创建模式（創建新的文件並寫入，如果文件已存在，則抛出IOError）

# b: binary mode, 二进制模式
# t: text mode, 文本模式（如圖片等非文字的)
```

&nbsp;

### 2.讀文件

以下操作通過看文件是否有權限被讀取、其中有沒有奇怪的字符不可被讀取，以此減少錯誤的發生

```
stream = open('xxx.txt')

# readline那一行因上接read(1)，所以會從第一行的第二個字母讀起，直到遇到換行符為止，就像是read(1)使文本內光標停在了第一個字母之後
print('\nIs this readable?' + str(stream.readable())) # 是否可以被读取 
print('\nRead one character : ' + stream.read(1)) # 读取一个字符
print('\nRead to end of line : ' + stream.readline()) # 读取一行
print('\nRead all lines to end of file : \n' + str(stream.readlines())+ '\n') # 读取所有行
stream.close() # 关闭文件

print(stream.closed) # 是否已经关闭
```

&nbsp;

### 3.寫文件

以下為寫入文件的例子

```
stream = open('xxx.txt', 'wt') # 在指定的文件中覆蓋寫入
stream.write('H') # 寫入一個字符
stream.writelines(['ello\n', 'World\n']) # 寫入一行字符，與之前一樣上行命令結束時光標在第一個字母之後，\n為換行符
names = ['Heisenberg', 'White'] # 以列表形式創建一個對象
stream.writelines(names) # 寫入一個對象
stream.write('\n') # 寫入一個換行符
stream.writelines('\n'.join(names)) # 寫入一個對象，對象列表中每一個詞都會換行一次
stream.close()
```

&nbsp;

### 4.seek和flush

`seek()`可以將寫入文件的“光標”重新定位在特定位置，以數字表示

&nbsp;

`flush()`的用處是相當與寫入一大堆內容的時候，臨時“暫存”保存一下文件，並且刷新緩衝區，以免系統不穩定時，造成文件資料損毀

<br>

且可以在自己錄入的時候，另一端可以看到我`flush()`之前的內容，因已經“暫存”了，不過如果最終沒有執行`close()`，依然會被清空，因沒有被實際保存

```
stream = open('xxx.txt', 'wt')
stream.write('demo!')
stream.seek(0) # 將光標移到文件的第一個字符之前
stream.write('cool')
stream.flush()
stream.close() # 這裡的關閉與之前的不同，因為這裡會最後先刷新緩衝區，將餘下的內容寫入文件，再關閉文件
```