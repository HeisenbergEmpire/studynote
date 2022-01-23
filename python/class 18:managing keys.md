# python學習筆記

## 第18課 環境變量基礎應用

### 1.環境變量是指在一個環境（文件夾）內，通過env（或更高級的操作）來預先編輯一些東西，令其不用顯示在代碼上，讀取即可運行

### 2.例子，在此例中將password和database兩個值預先在env文件中設置好

&nbsp;

#### 步驟一，在環境中新建一個文件，取名為.env，然後在裡面輸入如下鍵值對

```
PASSWORD=Dont share this value

DATABASE=Sample_Connection_String
```

&nbsp;

#### 步驟二，用pipenv安裝dotenv庫包，請確保vscode使用的與dotenv所在的虛擬環境一致（即dotenv所在的site-package位置）

```
pipenv install dotenv
```

用vscode的話，左下角運行環境會顯示你python 版本號（'目前py文件所在的文件夾名&pipenv編碼'：pipenv）

&nbsp;

#### 步驟三，在py文件中輸入如下代碼體驗

```
# 前置，從dotenv導入load_dotenv，用於讀取env文件，及導入os獲取env文件
from dotenv import load_dotenv
load_dotenv()
import os

# 例1，從env文件中讀取password值
password = os.getenv('PASSWORD')
print(password)

print()

# 例2，從env文件中讀取database值
database = os.getenv('DATABASE')
print(database)
```

&nbsp;

#### 步驟四，禁止發布env文件

通常用到env文件的話，都是用git來管理源碼，若不想將env文件發布出去，則需在虛擬環境中創建一個文件取名為.gitignore，在內輸入`.env`即可