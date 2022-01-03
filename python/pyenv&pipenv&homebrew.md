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
#可以使用 pipenv install --python x.x 來指定使用的python版本，前提你電腦裡有（最好首先用pyenv裝好在文件夾）
```

&nbsp;

### 之後是激活pipenv虛擬機

```
# 激活pipenv虛擬機
pipenv shell
# 退出pipenv虛擬機
exit
```

除此之外還可以直接在終端，通過pipenv直接運行某個單獨的python文件：

```
pipenv run 文件名.py
```

**謹記不要在pipenv shell或pipenv run後運行pipenv install和deactivate，會出錯**

&nbsp;

### 之後便可以愉快地安裝第三方庫包了

```
# 安裝指定第三方庫
pipenv install 第三方庫包名

# 根據pipfile中的描述安裝所有依賴
pipenv install

# 或者，根據pipfile.lock中的描述安裝所有依賴
pipenv install --ignore-pipfile

# 或者，只安裝dev組的依賴
pipenv install --dev

# 或者 ，根據曾經在pip上導出requirement.txt（即pip環境安裝的第三方庫列表）安裝依賴
pipenv install -r <path-to-requirements.txt>
```

當然有安裝就肯定有卸載了

```
# 刪除某個包
pipenv uninstall 第三方庫包名

# 刪除整個環境
pipenv --rm
```

&nbsp;

### 安裝好後，可以通過下面代碼查看當前環境所依賴的第三方庫

```
pipenv graph
```

&nbsp;

### 可以通過以下代碼檢查一般安全性

```
pipenv check
```

&nbsp;

### 如果想指定創建的虛擬環境之python版本，可以使用下面指令

```
pipenv --python 3.10
```

&nbsp;

### 顯示當前虛擬環境的儲存位置

```
pipenv --venv
```

&nbsp;

### 查看虛擬環境所有模塊

```
pip list
```

&nbsp;

### 還有一些其他雜項

```
# 查看當前路徑
pipenv --where

# 顯示虛擬環境使用的python路徑
pipenv --py

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

## 5.homebrew使用說明，及軟件升級，詳情請看下面網站

[homebrew](https://blog.devhitao.com/2020/01/18/homebrew-usage/)
