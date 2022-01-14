# python學習筆記

## 第17課：JSON

### 例子json

原始格式：
```
result
{"color": {"dominantColorForeground": "White", "dominantColorBackground": "White", "dominantColors": ["White"], "accentColor": "595144", "isBwImg": false}, "description": {"tags": ["bear", "polar", "animal", "mammal", "outdoor", "water", "white", "large", "walking", "snow", "standing"], "captions": [{"text": "a large white polar bear walking in the water", "confidence": 0.7419737378283093}]}, "requestId": "33290a37-ad67-42af-b647-c5a236ecd202", "metadata": {"width": 220, "height": 221, "format": "Jpeg"}}
```

&nbsp;

美化格式：
```
results
{
  "color":
           {"dominantColorForeground": "White",
            "dominantColorBackground": "White", 
            "dominantColors": ["White"], 
            "accentColor": "595144", 
            "isBwImg": false, 
            "isBWImg": false},
   "description": 
            {"tags": 
	      ["bear", "polar", "animal", "mammal", "outdoor", "water", "white", "large", "walking", "snow", "standing"], 
              "captions": 
                     [{"text": "a large white polar bear walking in the water",
	        "confidence": 0.7419737378283093}]
             },
  "requestId": "33290a37-ad67-42af-b647-c5a236ecd202"
  }
```

&nbsp;

### 1.JSON的三種格式

#### 第一種：單鍵對

```
"requestId": "33290a37-ad67-42af-b647-c5a236ecd202"
```
如此為單鍵對

&nbsp;

#### 第二種：系列子鍵

```
"color":
           {"dominantColorForeground": "White",
            "dominantColorBackground": "White", 
            "dominantColors": ["White"], 
            "accentColor": "595144", 
            "isBwImg": false, 
```
如此，一個鍵中有多個子鍵，表示了圖片的顏色、底色等的值

&nbsp;

#### 第三種：值列表

```
"tags": ["bear", "polar", "animal", "mammal", "outdoor", "water", "white", "large", "walking", "snow", "standing"]
```
如此，一個鍵對應的是多個值形成的列表

&nbsp;

### 2.json的引用

首先要導入json模塊
```
import json
```

&nbsp;

#### 一.對應上文，操作results，假設調用代碼時，請求web服務

```
print(results['requestId'])
```

返回結果為：
```
33290a37-ad67-42af-b647-c5a236ecd202
```

&nbsp;

#### 二.顯示子鍵中的值

對應子鍵，可以想像成一連串文件夾上下級目錄，如下，等於先進入color，在進入dominantColorBackground

```
print(results['color']['dominantColorBackground'])
```

返回結果為：

```
White
```

&nbsp;

#### 三.顯示鍵值列表裡的值

例如上文中的json裡面，tags裡面是一個鍵值列表，包含多個值，要單獨顯示某個值，就要用數字來表示位置

&nbsp;

如之前一樣，0表示第一個位置，1表示第二個位置如此類推

```
print(results['description']['tags'][0])
```

返回為：

```
bear
```

&nbsp;

如果要顯示出列表中的所有值，就要用到for循環

```
for item in results['description']['tags']:
    print(item)
```

返回為：

```
bear
polar
animal
mammal
outdoor
water
white
large
walking
snow
```

&nbsp;

### 3.python中創建json

首先還是從引入json模塊開始

```
import json
```

&nbsp;

#### 一.使用字典方法創建json鍵對

```
# 使用字典方法創建json鍵對
person_dict = {'first': 'Heisenberg', 'last': 'White'}
# 加入鍵對同樣需要字典
person_dict['city'] = 'Albuquerque'

# 創建好所有鍵對之後，就用json.dumps的方法導入
person_json = json.dumps(person_dict)
print(person_json)
```

返回為：

```
{"first": "Heisenberg", "last": "White", "city": "Albuquerque"}
```

&nbsp;

#### 二.加入嵌套外框架

```
# 假如要加入子鍵嵌套，則如下用字典嵌套字典，前置為第5行代碼
# person_dict = {'first': 'Heisenberg', 'last': 'White'}
staff_dict ={}
staff_dict['Program Manager']=person_dict

# 然後同樣用json.dumps的方法導入
staff_json = json.dumps(staff_dict)
print(staff_json)
```

返回為：

```
{"Program Manager": {"first": "Heisenberg", "last": "White", "city": "Albuquerque"}}
```

&nbsp;

#### 三.原字典中加入子鍵

```
# 假如要在原字典中加入子鍵，則要用字典嵌套列表，依然前置為第5行
# person_dict = {'first': 'Heisenberg', 'last': 'White'}
languages_list = ['CSharp','Python','JavaScript']
# 用原字典嵌套列表
person_dict['languages']= languages_list

# 繼續用json_dumps的方法導入
person_json = json.dumps(person_dict)
print(person_json)
```

返回為：

```
{"first": "Heisenberg", "last": "White", "city": "Albuquerque", "languages": ["CSharp", "Python", "JavaScript"]}
```

&nbsp;

## 用python寫json，第一記得用print來調試，確認顯示出來是你想要的，第二記得閱讀json時，用print來檢查每個鍵值是否有正確的包含關係