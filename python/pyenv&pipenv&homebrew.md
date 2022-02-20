# 虛擬環境使用與庫包管理

## 1.pyenv

### pyenv是管理某文件使用什麼python版本的工具，其條件是必須要用pyenv安裝的python版本才能被pyenv管理，首先是安裝pyenv

```
brew install pyenv
```

&nbsp;

### 這樣就安裝好，安裝前homebrew會檢查更新，我們可以用homebrew看看是否已經完成安裝

```
brew list
```

&nbsp;

### 檢查無誤後，使用pyenv直接安裝python的版本，這裏我安裝時python 3.10.0

```
pyenv install 3.10
```

&nbsp;

### 之後我們可以通過versions來看pyenv安裝了哪些python版本

&nbsp;

```
pyenv versions
```

&nbsp;

### 如果要刪除哪個版本也非常簡單(還是以我的3.10為例）

```
pyenv uninstall 3.10.0
```

&nbsp;

### 然後我們可以創建一個文件夾，用pyenv指定這個文件夾使用哪個版本的python（雖然可以用鼠標直接以終端機打開文件夾，但還是必須要掌握用終端機命令來創建運行文件夾比較好）

```
cd 文件夾名
mkdir 文件夾名
pyenv local 3.10.0
```

這三條指令意思是打開文件（cd），創建文件（mkdir），和用pyenv指定該文件夾使用的python版本

&nbsp;

## 2.pipenv

### pipenv是管理python第三方庫包的工具，他可以指定某文件夾依賴（安裝）這些庫包，首先安裝pipenv

```
brew install pipenv
```

&nbsp;

### 注意安裝後如果運行出現找不到文件，請用homebrew刪除pipenv從新安裝，刪除是

```
brew uninstall pipenv
```

&nbsp;

### 安裝好以後可以用以下指令查看版本

```
pipenv --version
```

&nbsp;

### 接著在某文件夾中創建文件夾（當然右鍵文件夾直接運行pipenv也可以就不用cd了），創建pipenv虛擬機

```
cd 文件名_pipenv
mkdir 文件名_pipenv
pipenv install
# 可以使用 pipenv install --python x.x 來指定使用的python版本，前提你電腦裡有（最好首先用pyenv裝好在文件夾）

# 創建pipenv虛擬環境時同時安裝所有系統已有的庫包
pipenv install --site-packages
```

&nbsp;

### 之後便可以愉快地安裝第三方庫包了

```
# 安裝指定第三方庫,並紀錄到pipfile，或者從pipfile中安裝包（即安裝同時與pipfile同步），可以同時安裝多個
pipenv install 第三方庫包名 更多的庫包名

# 安裝指定版本的包並鎖定版本（防止更新）
pipenv install requests/第三方庫包名==包版本號

# 安裝包含或排除指定的的包版本
pipenv install requests/第三方庫包名>/</>=/<=包版本號

# 安裝指定範圍的包版本（如2.2即在2.*的範圍內）
pipenv install requests/第三方庫包名～=包版本號

# 避免安裝某個特定的版本號
pipenv install requests/第三方庫包名!=包版本號

# 安裝包時根據pipfile.lock中的描述安裝所有依賴，或者安裝包時忽略pipfile，使用pipfile.lock（即與pipfile.lock同步，忽略pipfile）
pipenv install --ignore-pipfile 第三方庫包名

# 如上，忽略的是pipfile.lock文件
pipenv install --ignore-pipfile 第三方庫包名

# 將包安裝在[dev-packages]中
pipenv install -d/--dev 第三方庫包名

# 或者 ，根據曾經在pip上導出requirement.txt（即pip環境安裝的第三方庫列表）安裝依賴
pipenv install -r/--requirements <path-to-requirements.txt>

# 從pipfile有紀錄的源名稱（例如pypi，home）等地方安裝
pipenv install -i/--index

# 使用系統的pip來安裝，而不是使用vitualenv的pip命令，即安裝到真正python文件中，這有助于管理與部屬python基礎
pipenv install --system 第三方庫包名

# 通過import語句發現包並安裝包
pipenv install -c/--code<庫包名/模塊名>

# 安裝時若pipfile.lock已過期或python版本錯誤，則中止安裝
pipenv install --deploy 第三方庫包名

# 安裝包後不進行鎖定
pipenv install --skip-lock 第三方庫包名

# 安裝包時可編輯包的URL或路徑，通常用於VCS存儲庫，並將所有子依賴項添加到pipfile.lock中
pipenv install -e/--editable 第三方庫包路徑或URL

# 更新指定的包
pipenv install --selective-upgrade 第三方庫包名

# 從額外的pypi庫裡找到需要的包（通常是內網）
pipenv install --extra-index-url地址 第三方庫包名

# 一次一個地安裝依賴項，而不是同時安裝
pipenv install --sequential 第三方庫包名

# 安裝時防止pipfile.lock更新過時的庫包依賴關係
pipenv install --keep-outdated

# 允許安裝預發布的包
pipenv install --pre 第三方庫包名

# 安裝包後順便清理緩存
pipenv install --clear 第三方庫包名

# 安裝包時以最詳細信息輸出
pipenv install -v/--verbose 第三方庫包名

# 安裝包時指定版本
pipenv install --python 版本號 第三方庫包名

pipenv install --three/--two 第三方庫包名

```

當然有安裝就肯定有卸載了

```
# 卸載指定的包，並且在pipfile中刪除，可以同時刪除多個
pipenv uninstall 第三方庫包名 更多的庫包名

# 卸載所有開發環境裡的包，即紀錄在pipfile裡[dev-packages]項目裡的包
pipenv uninstall --all-dev

# 卸載虛擬環境裡的所有包，但不修改pipfile
pipenv uninstall --all

# 使用系統的pip來卸載，而不是使用vitualenv的pip命令，即從真正python文件中卸載，這有助于管理與部屬python基礎
pipenv uninstall --system

# 從某特定URL或路徑中刪除包，通常用於VCS存儲庫，並將所有子依賴項從到pipfile.lock中刪除
pipenv uninstall -e/--editable 第三方庫包名

# 卸載之後鎖定
pipenv uninstall lock

# 卸載指定的包但跳過pipfile.lock文件
pipenv uninstall --skip-lock 第三方庫包名

# 卸載指定的包並防止在pipfile.lock更新過時的依賴項
pipenv uninstall --keep-outdated 第三方庫包名

# 卸載指定的預發布包
pipenv uninstall --pre 第三方庫包名

# 卸載開發環境當中指定的包
pipenv uninstall --dev 第三方庫包名

# 從指定的python版本中卸載包
pipenv uninstall --python 版本號 第三方庫包名

pipenv uninstall --three/--two 第三方庫包名

# 卸載包並清空緩存
pipenv uninstall --clear 第三方庫包名

# 卸載包並以最詳細化信息輸出
pipenv uninstall -v/--verbose 第三方庫包名
```

&nbsp;

### 生成pipfile.lock文件

```
# 生成pipfile.lock文件
pipenv lock

# 產生與erquirements.txt相容的lock文件
pipenv lock -r/--requirements

# 創建預發布的lockfile
pipenv lock --pre

# 為[dev-packages]中的包產生與requirements.txt相容的lock文件
pipenv lock -d/--dev

# 從pipfile和pipfile.lock文件裡屬於開發環境（dev）的包紀錄導出為requirements文件
pipenv lock -r/--requirements -d/-dev

# 生成pipfile.lock文件時指定python版本
pipenv lock --python 版本號
pipenv lock --three/--two

# 生成pipfile.lock文件同時清楚依賴關係緩存
pipenv lock --clear

# 生成pipfile.lock文件同時以最詳細信息輸出
pipenv lock -v/--verbose

# 生成pipfile.lock文件並使用指定庫包源路徑
pipenv lock --pypi-mirror

# 防止pipfile.lock更新過時的套件依賴關係
pipenv lock --keep-outdated
```

&nbsp;

### 安裝所有在pipfile.lock中紀錄的包，通常用於部署環境

```
pipenv sync [options]

options:
--bare 最簡化信息輸出

--sequential 一次一個地安裝依賴項，而不是同時安裝

--keep-outdated 部署環境並防止pipfile.lock更新的過時的依賴項

--pre 允許安裝預發布包

-d/--dev 把包安裝在開發環境中

--python 版本號

--three/--two

--clear 清除套件相依性快取

-v/--verbose 最詳細化信息輸出

--pypi-mirror 指定庫包鏡像源
```

**注意：pipenv install --ignore-pipfile和pipenv sync命令很相似，但是後者命令永遠不會嘗試重新鎖定依賴項，因為他被認為是一個原子操作。**

<br>

**默認情況下，除非使用了--deploy標誌，否則pipenv install會嘗試重新鎖定依賴項**

&nbsp;

### 更新依賴包，需要先執行pipenv lock，之後再執行pipenv sync，然後再執行以下命令

```
pipenv update [options] 第三方庫包名

options：
--bare 最簡化信息輸出

--outdated 列出所有pipfile.lock中過時的依賴項

--keep-outdated 防止pipfile.lock更新過時的依賴項

--dry-run 列出過時的依賴項

-e/--editable 路徑/URL 從指定URL或路徑中更新，通常用於VCS存儲庫，並將所有子依賴項從到pipfile.lock中更新

--ignore-pipfile 安裝包時忽略pipfile，使用pipfile.lock

--selective-upgrade 更新指定的包

-r/--requirements 根據requirements文件更新

--extra-index-URL 從額外的pypi庫中更新（通常是內網）

-i/--index 從pipfile有紀錄的源名稱（例如pypi，home）等地方更新

--sequential 一次一個地更新而不是全部一次過更新

--keep-outdated 更新後保持在pipfile.lock中更新過時的依賴項

--pre 允許更新到預發布版本或更新預發布包

-d/--dev 更新開發環境中的包

--python 版本號

--three/--two

--clear 更新並清理緩存

-v/--verbose 更新並以最詳細信息顯示

--pypi-mirror 指定第三方庫包鏡像源更新
```

&nbsp;

### 若要移除當前（文件夾）的pipenv虛擬環境，輸入下面代碼

```
pipenv --rm
```

&nbsp;

### 之後是激活pipenv虛擬機

```
# 激活pipenv虛擬機
pipenv shell

# 激活pipenv虛擬機並巢狀疊加新的shell
pipenv shell --anyway shell文件名

# 激活pipenv虛擬機並指定鏡像源
pipenv shell --pypi-mirror

# 激活pipenv虛擬機並指定版本
pipenv shell --three/--two

pipenv shell --python 版本號
```

&nbsp;

# 退出pipenv虛擬機

```
exit
```

&nbsp;

### 除此之外還可以直接在終端，通過pipenv直接運行某個單獨的python文件

```
pipenv run [options] 文件名.py/文件夾名

options:
--python 版本號

--three/--two

--clear

-v/--verbose

--pypi-mirror
```

**謹記不要在pipenv shell或pipenv run後運行pipenv install和deactivate，會出錯**

&nbsp;

### 安裝好後，可以通過下面代碼查看各種環境資訊

```
# 查看當前pipenv環境所在文件夾
pipenv --where

# 查看當前pipenv環境儲存目錄
pipenv --venv

# 顯示虛擬環境使用的python路徑
pipenv --py

# 查看pipenv環境變量
pipenv --envs
```

**注意：不要講項目的.env文件提交到源代碼控制中**

&nbsp;

### 展示當前安裝包的依賴關係

```
# 展示當前安裝包的依賴關係
pipenv graph

# 展示當前安裝包的依賴關係並以最簡化信息輸出
pipenv graph --bare

# 展示當前安裝包的依賴關係並以json格式輸出
pipenv graph --json

# 展示當前安裝包的依賴關係並以json樹格式輸出
pipenv graph --json-tree

# 展示當前安裝包的依賴關係並反轉依賴圖
pipenv graph --reverse
```

&nbsp;

### 在編輯器中瀏覽指定的模塊（包括工作環境代碼）

```
pipenv open [options] 包名或者模塊名（如requests、maya等，詳参第五項）

options：
--python 版本號

--three/--two

--clear

-v/--verbose

--pypi-mirror
```

&nbsp;

### 可以通過以下代碼檢查一般安全性

```
pipenv check

# 顯示和檢查可能未使用的依賴項
pipenv check --unused

# 檢查並清理緩存
pipenv check --clear

# 檢查並詳細輸出
pipenv check --v/verbose

# 用不同python版本進行檢查
pipenv check --python 版本號

pipenv check --three/two

# 使用系統的pip來檢查，而不是使用vitualenv的pip命令，即用真正python來檢查，這有助于管理python安全
pipenv check --system
```

&nbsp;

### 卸載不在pipfile.lock中的包

```
# 卸載所有不在pipfile.lock中的包
pipenv clean

# 卸載所有不在pipfile.lock中的包並以最簡化信息輸出
pipenv clean --bare

# 卸載所有不在pipfile.lock中的包並以最詳細信息輸出
pipenv clean -v/--verbose

# 模擬並列出不需要或未使用的包，不是真的卸載
pipenv clean --dry-run
```

&nbsp;

### 以下指令用於命令自動補全

```
pipenv --completion
```

&nbsp;

### 如果想指定創建的虛擬環境之python版本，可以使用下面指令

```
pipenv --python 3.10
```

&nbsp;

### 指定pypi鏡像源（即庫包下載地址）

```
pipenv --pypi-mirror
```

&nbsp;

### 還有一些其他雜項

```
# 精簡操作手冊
pipenv --bare
```

&nbsp;

## 3.關於pipenv lock時遇到的SSL Error

錯誤反饋如下：

```
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
usr/local/Cellar/pipenv/2018.5.18/libexec/lib/python3.6/site-packages/pipenv/vendor/requests/sessions.py", line 508, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/Cellar/pipenv/2018.5.18/libexec/lib/python3.6/site-packages/pipenv/vendor/requests/sessions.py", line 618, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/Cellar/pipenv/2018.5.18/libexec/lib/python3.6/site-packages/pipenv/vendor/requests/adapters.py", line 506, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /pypi/pyobjc-framework-netfs/json (Caused by SSLError(SSLError(1, u'[SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590)'),))
```

解決方案：安裝pyopenssl一般就能解決問題。注意不要使用pipenv install，不然你需要在每個環境（文件夾）都要重新安裝一遍，乾脆把它撞到本機：

```
pip install pyopenssl
```

&nbsp;

## 4.pipfile內容解析

以此pipfile这个文件為例

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
flask = "*"

[requires]
python_version = "3.7"
```

&nbsp;

### 首先看 `[source]`

别的无关紧要，url这边一眼就可以看出是对应的pypi源，官方源比较慢，若要换成国内源，如下修改即可

```
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

&nbsp;

### 然後是 `[dev-packages]`

意为开发-包。在你把pipfile给别人时，这里面记录的包不会被自动安装，一般用来放一些开发是用到的辅助测试之类的库
<br>
用來指定開發環境需要的包，這類包只用于開發過程，不用于生產環境，比如單元測試相關的包，只在開發階段游泳，這樣分開便於管理

&nbsp;

### 那么`[packages]`就很好理解了，前面我们示例安装了flask最新版，packages中就记录了这一点，其他人使用你的pipfile时也会去下载对应库及版本

&nbsp;

### 最后是`[requires]`，里面记录了基础需求，也就是会被必然下载的部分

```
此时会有一个疑问:我安装的flask目前是最新的，但是移植给别人时可能已经不是最新的了，这不就会出问题嘛。这时pipfile.lock的作用就来了
```

`pipfile.lock`中记录了你安装的所有的库及其版本号的hash，在新的环境中安装时会去匹配hash，这样就可以保证每次安装出来的环境是一样的

&nbsp;

## 5.設置多個包的源

&nbsp;

### 如果我们需要在安装包时，从一个源下载一个安装包，然后从另一个源下载另一个安装包，我们可以通过下面的方式配置

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[[source]]
url = "http://pypi.home.kennethreitz.org/simple"
verify_ssl = false
name = "home"

[dev-packages]

[packages]
requests = {version="*", index="home"}
maya = {version="*", index="pypi"}
records = "*"
```
如上设置了两个源：

&nbsp;

pypi(https://pypi.python.org/simple)
<br>
home(http://pypi.home.kennethreitz.org/simple)
<br>
同时指定requests包从home源下载，maya包从pypi源下载

&nbsp;

### 再給一個例子以作參考

```
[[source]]
url = "https://mirrors.aliyun.com/pypi/simple"
verify_ssl = true
name = "aliyun"

[[source]]
url = "https://pypi.douban/simple"
verify_ssl = true
name = "douban"

[dev-packages]

[packages]
requests = {version="*", index="douban"}
maya = {version="*", index="aliyun"}
records = "*"
```

&nbsp;

## 6.更多的python版本指定

```
[packages]
unittest2 = {version = ">=1.0,<3.0", markers="python_version < '2.7.9' or (python_version >= '3.0' and python_version < '3.4')"}
```

&nbsp;

## 7.更多關於pipenv或pip的理論知識

### 一.到處都有 site-packages 資料夾

#### 1.`site-packages `是一個資料夾，放我們安裝的 python package，可能到處都有

#### 2.每安裝一個 python 版本，對於版本 X.Y 都有各自的`site-packages`

<br>

比方說 python 3.4 跟 python 3.6 都各自有分開的`site-packages`在不同的路徑，而 python 3.6.1 跟 python 3.6.2 的是同一個

&nbsp;

#### 3.每個 user 可以有自己的`site-packages`，在 home 目錄下的某個地方（如果有興趣可以 google`site`這個 package 的`site.USER_SITE`

#### 4.ipython 跟一些tool裝了之後也有自己的`site-packages`

&nbsp;

### 二.python script與python package的不同

#### python script：我們執行一個pip命令，其實只是一個開端，即python script

<br>

真正的運作是執行時，裡面會再去import（引用）電腦裡某個`site-packages`文件夾裡真正的包來跑（推薦用`which pip`去看一下script內容）

&nbsp;

#### python package：承上，至於會import（引用）到哪個`site-packages`文件夾下的package，是看我們怎麼執行pip

**（這部分對於pipenv用戶來講只是理解一下傳統pip的邏輯即可，因為我們的路徑是非常清晰的，下面會說明）**

&nbsp;

### 1.直接執行 pip ：
shell 會找到`$PATH`裡第一個`pip`script，依照這 script 裡的 shebang (就是`#!/usr/bin/python`這種東西)來決定用哪個版本的 python 跑。

<br>

所以會用那個版本 python 的`sys.path`去找`pip`package 來用。有興趣的人可以試試去改 shebang 的版本，看會發生什麼事。

&nbsp;

### 2.用 python 跑指定路徑的 pip script：
這樣shell執行的`python`版本會壓過shebang指定的python版本。比方說，這裡執行的`python`如果是 2.7，

<br>

就算shebang雖然指定要用python3跑，最後還是會用2.7去跑；所以，這樣就會從python2.7的`sys.path`裡去找`pip package`。

&nbsp;

### 3.用 python 的 -m 參數跑 pip：
這樣會去用shell執行的`python`版本的`sys.path`裡的`pip`package(好繞…)。如果python指令的版本是2.6，那就是跑2.6裡的`pip`package。

&nbsp;

man page 說明:

```
-m module-name: Searches sys.path for the named module and runs the corresponding .py file as a script.
```

以上不管是哪一種，如果沒有任何一個`site-packages`裡有pip，就import error跑不起來。

&nbsp;

### 三.pip install後，東西到底被裝到哪裡

**有兩個方法可以看被裝到哪裡**

&nbsp;

#### 1.最簡單的方法是剛才講到的，`pip --version`(或是pip -V)會顯示目前這個 pip 是跑哪一個`site-packages`下的`pip`package

這個路徑就是 install 時會放的 dir

&nbsp;

#### 2.或，比較間接的方法，先用`pip list`列出所有已經安裝的pkg，然後用`pip show [某pkg]`就會寫 Location 在哪

&nbsp;

### 三.pipenv的`site-packages`又在哪？
其實pipenv就比較方便了，不再使用python原來的`site-packages`，便不會倒至到處都是`site-packages`

&nbsp;

**路徑規律**

```
Macintosh HD/使用者/用戶名/.local/share/virtualenvs/虛擬機目標文件夾開頭/lib/python版本號/site-package/pip/vendor/colorama
```

&nbsp;

**所以只要輸入`pipenv --venv`或者`pipenv --py`便知道`site-package`或者庫包實際存放路徑在哪裡了**

&nbsp;

## 8.指定包的引索

如果你希望使用特定的包索引安装特定的包，你可以像下面这样做：

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[[source]]
url = "http://pypi.home.kennethreitz.org/simple"
verify_ssl = false
name = "home"

[dev-packages]

[packages]
requests = {version="*", index="home"}
maya = {version="*", index="pypi"}
records = "*"
```

&nbsp;

## 9.通過環境變量將憑證注入Pipfile

pipenv將在 Pipfile 中替換環境變量(如果定義了)。這在你需要進行私有PyPI認證時特別有用：
```
[[source]]
url = "https://$USERNAME:${PASSWORD}@mypypi.example.com/simple"
verify_ssl = true
name = "pypi"
```
pipenv在替換環境變量之前會對Pipfile進行哈希（並且，當您從Pipfile.lock 文件中安裝包時，它將再次替換環境變量

<br>

所以在提交時不會提交任何隱私文件)

&nbsp;

## 10.指定特定系統上安裝的包

如果你想指定某個包只在某個特定的系統上安裝，可以使用 PEP 508 說明符來完成。

&nbsp;

下面的例子，將只在Windows系統上安裝 pywinusb：
```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"
pywinusb = {version = "*", sys_platform = "== 'win32'"}
```
下面是個更複雜的例子
```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[packages]
unittest2 = {version = ">=1.0,<3.0", markers="python_version < '2.7.9' or (python_version >= '3.0' and python_version < '3.4')"}
```

&nbsp;

## 11.自動加載 .env 文件

如果項目目錄下包含一個 .env 文件，它會被 pipenv shell 和 pipenv run 命令自動加載：

```
$ cat .env
HELLO=WORLD⏎

$ pipenv run python
Loading .env environment variables…
Python 2.7.13 (default, Jul 18 2017, 09:17:00)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.environ['HELLO']
'WORLD'
```
這對於將生產憑證排除在代碼庫之外非常有用。我們不建議將 .env 文件提交到源代碼控制中！

&nbsp;

如果你的 .env 文件位於不同的路徑下或者有其他名稱，你可以設置一個 PIPENV_DOTENV_LOCATION 環境變量：

```
$ PIPENV_DOTENV_LOCATION=/path/to/.env pipenv shell
```

要禁止pipenv加載 .env 文件，可以設置 PIPENV_DONT_LOAD_ENV 環境變量：

```
$ PIPENV_DONT_LOAD_ENV=1 pipenv shell
```

&nbsp;

## 12.定制腳本快捷方式

Pipenv支持在Pipfile的（可選）`[scripts]`部分中創建自定義快捷方式。

&nbsp;

然後可以在終端中運行 pipenv run ，以便在pipenv虛擬環境的上下文中運行命令，即使你沒有首先激活pipenv shell。

&nbsp;

例如，在您的Pipfile中：

```
[scripts]
printspam = "python -c \"print('I am a silly example, no one would need to do this')\""
```

然後，在終端中運行：

```
$ pipenv run printspam
I am a silly example, no one would need to do this
```

需要參數的命令也可以：

```
[scripts]
echospam = "echo I am really a very silly example"

$ pipenv run echospam "indeed"
I am really a very silly example indeed
```

&nbsp;

## 13.環境變量支持

Pipenv支持在值中使用環境變量，例如：

```
[[source]]
url = "https://${PYPI_USERNAME}:${PYPI_PASSWORD}@my_private_repo.example.com/simple"
verify_ssl = true
name = "pypi"

[dev-packages]

[packages]
requests = {version="*", index="home"}
maya = {version="*", index="pypi"}
records = "*"
```

環境變量可以使用 {$MY_ENVAR} 或 $MY_ENVAR 的方式指定。在Windows下，還可以使用 %MY_ENVAR% 來指定。

&nbsp;

## 14.更多pipenv高級使用說明，請看下面網站

[pipenv高級說明1](https://blog.csdn.net/swinfans/article/details/89305301)
[pipenv高級說明後課](https://docs01.com/pages/1380399)

&nbsp;

## 15.homebrew使用說明，及軟件升級，詳情請看下面網站

[homebrew](https://blog.devhitao.com/2020/01/18/homebrew-usage/)
