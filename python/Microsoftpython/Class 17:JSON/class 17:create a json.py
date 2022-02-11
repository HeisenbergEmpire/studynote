# 首先要導入json模塊
import json

# 使用字典方法創建json鍵對
person_dict = {'first': 'Heisenberg', 'last': 'White'}
# 加入鍵對同樣需要字典
person_dict['city'] = 'Albuquerque'

# 創建好所有鍵對之後，就用json.dumps的方法導入
person_json = json.dumps(person_dict)
print(person_json)

print()

# 假如要加入子鍵嵌套，則如下用字典嵌套字典，前置為第5行代碼
# person_dict = {'first': 'Heisenberg', 'last': 'White'}
staff_dict ={}
staff_dict['Program Manager']=person_dict

# 然後同樣用json.dumps的方法導入
staff_json = json.dumps(staff_dict)
print(staff_json)

print()

# 假如要在原字典中加入子鍵，則要用字典嵌套列表，依然前置為第5行
# person_dict = {'first': 'Heisenberg', 'last': 'White'}
languages_list = ['CSharp','Python','JavaScript']
# 用原字典嵌套列表
person_dict['languages']= languages_list

# 繼續用json_dumps的方法導入
person_json = json.dumps(person_dict)
print(person_json)

# 用python寫json
# 第一記得用print來調試，確認顯示出來是你想要的
# 第二記得閱讀json時，用print來檢查每個鍵值是否有正確的包含關係
