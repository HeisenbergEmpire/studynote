# python學習筆記

## 第16課：調用API與request庫獲取API

### 1.什麼是API

```
# API全稱為application programming interface，作用是在網絡中調用一個網站分享出來的服務

# 好比你的項目需要一個獲得天氣數據的服務，以便提醒用戶今天寒冷需要添衣，或下雨需要帶傘，此時如果要自己再去寫一個這樣功能的程序是非常浪費時間

# 故而我們可以從網上找一個提供天氣數據的服務API插入項目中，這樣就不用自己寫了
```

&nbsp;

### 2.使用request庫獲取API服務的語言格式

```
r = requests.get/post(address(url),params,data,http_headers,
                  timeout,verify,allow_redirects,cookies,
                  function_parameters,message_body)
```

&nbsp;

**這裡逐個項目作講解：**

#### 一.`get/post`:這是http（基於TCP的超文本傳輸協議）的請求類型，某些API有說明什麼服務需要什麼類型，有些要自己想，專業定義可以看這裡

[get/post的不同](https://blog.fundebug.com/2019/02/22/compare-http-method-get-and-post/)

#### 二.`address(url)`:這是URL地址，通常指網址的？前面，比如?v=SnxhC9sKCxl

#### 三.`params`:字典形式，設置URL後面的參數，比如id?123&name=xiaoming

#### 四.`date`:字典或字符串，一般用於POST方法時提交數據

#### 五.`headers`：設置user-agent、refer、及密鑰等其他東西的請求頭，通常是向服務器提供身份地址、請求與服務約束等，某些API有具體要求，某些需要自己找規律

[請求頭詳講1](https://www.msfxt.com/log/http%E8%AF%B7%E6%B1%82%E5%A4%B4%E5%92%8C%E8%AF%B7%E6%B1%82%E8%A1%8C.html)
[請求頭詳講2](https://zhuanlan.zhihu.com/p/282737965)
[請求頭詳講3](https://blog.csdn.net/DuTianTian_csdn/article/details/82755848)

#### 六.`timeout`:超時時間，單位是秒

#### 七.`verify`:True/False，是否進行HTTPS證書認證，默認是，需要自己設置證書地址，若設置為否則可以繞過證書認證比較方便

#### 八.`allow_redirects`:True/False是否讓requests做重定向處理，即自動跳轉，默認是，設置否則可以自己選擇是否要跳轉

#### 九.`cookies`：附帶本地的cookies數據

#### 十.`function_parameters`:具體API服務指令

#### 十一.`message_body`:某些服務需要的信息主體，比如圖像分析就肯定需要一張圖片啦

&nbsp;

### 3.response響應提取語言

&nbsp;

**發出request就會收到回應，下面對不同回應做出具體查詢的簡單介紹**

```
r = requests.get/post(URL)

# 查看狀態碼，如果等於200代表請求成功，等於400代表失敗
r.status_code

# 可以查看當前編碼，以及變更編碼
# （重要！request會根據headers推測編碼，推測不到則設置為ISO-8859-1可能導致亂碼）
# （特別對於中文網頁，這時需要自己打開網頁去查看源代碼，修改encoding的值）
r.encoding

# 查看返回的網頁內容
r.test

# 查看返回的HTTP的headers（注意和訪問的URL可能會不同，因為是編碼裡的URL）
r.url

# 以字節的方式返回，比如用於下載圖片
r.content

# 服務端要寫入本地的cookies數據
r.cookies
```

&nbsp;

### 4.教程例子

```
# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python 
import requests

# We will need the json library to read the data passed back 
# by the web service(返回信息是json文件)
import json

# You need to update the SUBSCRIPTION_KEY to 
# they key for your Computer Vision Service（密鑰）
SUBSCRIPTION_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

# You need to update the vision_service_address to the address of
# your Computer Vision Service（API服務URL）
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

# Add the name of the function you want to call to the address（該服務具體指令以連結不同的URL呈現）
address = vision_service_address + "analyze"

# According to the documentation for the analyze image function （該服務具體指令以連結不同的URL及網址後續字典呈現）
# There are three optional parameters: language, details & visualFeatures
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# Open the image file to get a file object containing the image to analyze（open是打開此本地文件，read是閱讀，這樣就將文件導入函數中）
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type（這裡的請求頭是登陸方式，用的是帳號密鑰而非body，以及傳輸方式）
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code（糾錯）
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))
```

&nbsp;

## 這裡其實只要暫時簡單瞭解即可，到爬蟲時會更具體
