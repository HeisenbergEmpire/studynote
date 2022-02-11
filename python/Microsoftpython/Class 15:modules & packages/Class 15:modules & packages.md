# python學習筆記

## 第15課模塊與庫包

### 1.設立一個代碼模塊其實很簡單，如課中例子，在文件夾中加入一個名為helpers.py的python文件，其內代碼如下

```
# 其中引用的colorama庫在下文中會講述
from pip._vendor.colorama import init, Fore 

def display(message,is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)
```

**之後保存即可成為一個模塊**

&nbsp;

### 2.之後可以用以下三種方式加入模塊，各有不同作用

&nbsp;

**第一種方法，表示只是導入helpers模塊，所以每個helpers模塊裡面的函數都在前面加上helpers.才能運用**

```
import helpers
helpers.display('Not a warning',True)
```
其中true表示helpers中的is_warning中的值為ture，所以出來的效果是print出紅色的not a warning，而紅色的效果正是來源於colorama模塊

&nbsp;

**第二種方法，意思是從helpers模塊中調用所有函數（星號代表所有的意思)**

```
from helpers import *
display('Not a warning')
```

&nbsp;

**第三種方法，意思是從helpers模塊中調用display函數，調用單個函數的好處在於，vscode在聯想時不會因為同首字母彈出大量詞彙(如果有多段函數時)**

```
from helpers import display
display('Not a warning')
```

&nbsp;

### 3.用pipenv在終端機安裝與使用colorama庫的方法

```
# 第一步，用pipenv安裝colorama
pipenv install colorama
# 若要卸載colorama，則如下
pipenv uninstall colorama

# 第二步，在文件夾內運行pipenv終端機
pipenv shell
# 若要退出，如下輸入exit即可
exit

# 第三步，在helpers.py中，輸入from pip._vendor.colorama來引用，其中colorama路徑如下
Macintosh HD/使用者/用戶名/.local/share/virtualenvs/虛擬機目標文件夾開頭/lib/python版本號/site-package/pip/vendor/colorama
```
更詳盡的pipenv、pyenv和homebrew使用方法，請看文件pyenv&pipenv&homebrew.md
