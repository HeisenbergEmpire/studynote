# python學習筆記

## 第二十五課：文件管理（pathlib的基礎運用）

### 1.我們有時需要查詢一個系統裡文件的基礎信息，以免造成錯誤，以下為本課例子內容

引入pathlib庫中的path

```
from pathlib import Path
```

&nbsp;

Path.cwd()為查詢當前工作所在目錄,兩個\n是為了之後的內容換行顯示

```
cwd = Path.cwd() # 以下所有代碼均需要這行代碼及上行代碼
print('\nCurrent working directory:\n', str(cwd))
```

&nbsp;

path.joinpath()為將一個文件名或者路徑與另一個文件名或者路徑結合，如下即是將cwd與'new_file.txt'結合，最後顯示為cwd/new_file.txt

```
# cwd位也可以是其他路徑
new_file = Path.joinpath(cwd, "new_file.txt")
print('\nFull path:\n' + str(new_file))
```

&nbsp;

以下是檢測檔案是否存在的方法，以防代碼調用文件出錯

```
print('\nDoes the file exist:' + str(new_file.exists()) + '\n')
```

&nbsp;

### 2.parent（父級）即上級目錄的意思，child(子級）即下級文件或目錄，下面是檢查各種是否問題

cwd.parent()為查詢當前工作目錄的上層（父級）目錄前置操作

```
parent = cwd.parent
```

&nbsp;

is_dir()為檢測路徑是否為目錄

```
print(parent.is_dir())
```

&nbsp;

is_file()為檢測路徑是否為檔案

```
print(parent.is_file())
```

&nbsp;

iterdir()為查詢上級（父級）目錄下的所有子目錄

```
for child in parent.iterdir():
    if child.is_dir(): # 如果是目錄，則印出
        print(child)
```

&nbsp;

### 3.以下為檢測文件信息的一系列方法

這裡意思是查詢目標是當前環境下的xxx.txt

```
demo_file = Path(Path.joinpath(cwd, "xxx.txt"))
```

&nbsp;

查詢文件名

```
print('\nfile name:' + demo_file.name)
```

&nbsp;

查詢文件後綴

```
print('\nfile suffix:' + demo_file.suffix)
```

&nbsp;

查詢文件父級環境（路徑）名

```
print('\nfile folder:' + demo_file.parent.name)
```

&nbsp;

查詢文件大小,stat()為查詢文件的信息，st_size為文件大小

```
print('\nfile size:' + str(demo_file.stat().st_size))
```

&nbsp;


&nbsp;

## 在寫入、讀取與遷移文件之前，檢查一下文件資料非常有助于防止發生錯誤，比如掉失文件、代碼等
