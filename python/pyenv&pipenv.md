# 虛擬環境使用與庫包管理
## 1.pyenv
pyenv是管理某文件使用什麼python版本的工具，其條件是必須要用pyenv安裝的python版本才能被pyenv管理，首先是安裝pyenv
```
brew install pyenv
```
這樣就安裝好，安裝前homebrew會檢查更新，我們可以用homebrew看看是否已經完成安裝
```
brew list
```
檢查無誤後，使用pyenv直接安裝python的版本，這裏我安裝時python 3.10.0
```
pyenv install 3.10.0
```
之後我們可以通過versions來看pyenv安裝了哪些python版本
```
pyenv versions
```
如果要刪除哪個版本也非常簡單(還是以我的3.10為例）
```
pyenv uninstall 3.10.0
```
然後我們可以創建一個文件夾，用pyenv指定這個文件夾使用哪個版本的python（雖然可以用鼠標直接以終端機打開文件夾，但還是必須要掌握用終端機命令來創建運行文件夾比較好）
```
cd 文件夾名
mkdir 文件夾名
pyenv local 3.10.0
```
這三條指令意思是打開文件（cd），創建文件（mkdir），和用pyenv指定該文件夾使用的python版本

&nbsp;

## 2.pipenv
pipenv是管理python第三方庫包的工具，他可以指定某文件夾依賴（安裝）這些庫包，首先安裝pipenv
```
brew install pipenv
```
注意安裝後如果運行出現找不到文件，請用homebrew刪除pipenv從新安裝，刪除是
```
brew uninstall pipenv
```
接著在某文件夾中創建pipenv虛擬機並啟動
```
pipenv install
pipenv shell
```
之後便可以愉快地安裝第三方庫包了
```
pipenv install 第三方庫包名
```

