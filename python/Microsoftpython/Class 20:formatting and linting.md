# python學習筆記

## 第20課：格式化與linting及文檔字符串

### 1.格式化

&nbsp;

把python代碼格式規範化，更便於大家閱讀、管理與修改，例如以下凌亂的代碼就看起來很不爽

```
x = 12
if x== 24:
 print('Is valid')
else:
    print("Is not valid")

def helper(name='sample'):
 pass

def another( name = 'sample'):
         pass
```

&nbsp;

***而有了格式規範工具，當格式錯誤的時候就會有提示，從而避免格式凌亂***

&nbsp;

### 2.格式化工具pylint的安裝與啟用

#### 第一步，安裝pylint

```
pipenv install pylint
```

&nbsp;

#### 第二步，啟用

```
# vscode下按ctrl+shift+p，彈出的命令框輸入以下命令
select linter

# 選擇python：select linter，之後選擇linter工具是pylint

# 之前沒有安裝pylint的vscode會彈出提示窗口安裝，但在terminal執行的命令是pipenv install pylint --dev
# 會把pylint安裝到dev開發環境中，不便於使用，所以不要從vscode安裝，儘量選擇手動安裝

# 安裝設定好後繼續ctrl+shift+p，輸入以下命令，然後選擇enable就會運行pylint
python enable linter

# 要關閉也只要輸入上面代碼，然後選擇disable就會關閉運行pylint
```

&nbsp;

***啟用後，當格式有錯誤（比如打了些無關的符號，單引號雙引號亂用，縮進空格不標準）就會收到提示***

&nbsp;

### 3.文檔字符串

文檔字符串主要用於說明某個參數或者函數，作一個說明，因為有時代碼量多了很容易搞混,例子如下：

```
ef print_hello(name: str) -> str:
    """
    Greets the user by name


    Parameters
        name(str): The name of the user

    Returns
        str: The greeting
    """
    print('Hello,' + name)

print_hello('heisenberg')
```

&nbsp;

***當打到最後print_hello的一行，就會出現以下提示***

```
(funcion) print_hello(name:str) -> str

Greets the user by name

Parameters
    name(str): The name of the user

Returns
    str: The greeting
```

&nbsp;

## 代碼格式規範化和文檔字符串提示都是很好的習慣，我們應該努力執行>_<
