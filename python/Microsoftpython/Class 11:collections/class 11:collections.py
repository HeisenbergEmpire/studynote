# 在一個變量詞中能夠含有不止一個值，可以是多個
names = ['Heisenberg', 'Walter']
print(names)
print()
# 然後我們亦可以在變量中插入多個值
scores = []
scores.append(98)
scores.append(99)
print(scores)
# 並且可以只是print其中一個值出來
# 再次注意第一個值為0，所以print出來的是第二個值
print(scores[1])
print()
# 除上述基本操作，我們還可以加入數組（數據類型），以下引用數組庫array
from array import array
scores1 = []
scores1 = array('d')
# d為數據類型double，雙精度浮點數（後面有詳細解釋類型）
# array是指定類型的，而list則可以把任何東西放進變量詞
scores1.append(97)
scores1.append(98)
print(scores1)
print(scores1[1])
print()
# 以下是數組的更多用法
names1 = ['Walter', 'Heisenberg']
print(len(names1))
# len代表計算變量詞中有多少個值
names1.insert(0,'Xman')
print(names1)
# insert可以具體控制插入值的位置
names1.sort()
print(names1)
# sort輸出的結果將以首字母的書序排列變量詞中的值
print()
# 如下，可以用一個新的變量詞來抽出已有變量詞中，列表裡的幾個值
# 注意這裡的1:4代表從1位（第二個）到4位（第五個）之前的東西
# 格式是：列表（數組）名[起始（包括）；結束（不包括）]
names2 = ['Heisenebrg', 'Walter', 'Mitrix', 'Xman']
preserters = names2[1:4]
print(names)
print(preserters)
print()
# 下面是字典的用法，在變量詞中，位置將以鍵值來表示（如下代碼中的first、last）
person = {'first': 'Heisenberg'}
person['last'] = 'White'
print(person)
print(person['first'])
print()
# 最後總結
# 數組array用於統一類型的值，通常是數字
# 列表list通常用於要確保值的排列，變量詞當中的值可以為任意類型（甚至包含字典為值）
# 字典dictionaries用於多個變量詞不用確保排序，可以通過鍵值來調用當中的值（如上直接調用first）
# 以下為字典與列表聯用例子：
Heisenberg = {}
Heisenberg['1'] = 'Heisenberg'
Heisenberg['2'] = 'Chueng'

Walter = {'first': 'Walter','last': 'White'}

print(Heisenberg)
print(Walter)
print()
people = [Heisenberg, Walter]
people.append({'first': 'Jesse', 'last': 'Pinkman'})
presenters = people[1:3]
print(people)
print()
print(presenters)
print()
print(len(presenters))
print()


# array類型簡述
# b，signed char，-128至127之間的整數，1bytes
# B，unsigned char，0至255之間的整數，1bytes
# U，wchar_t,雙字節類型，通常用於漢字、韓文、日文等
# h，signed short，-32768至32767之間的整數，2bytes
# H，unsigned short，0至65535之間的整數，2bytes
# i，signed int，-32768至32767之間的整數，2bytes
# I，unsigned int，0至65535之間的整數，2bytes
# l，signed long，-9223372036854775808至9223372036854775807之間的整數，8bytes
# L，unsigned long，至18446744073709551615之間的整數，8bytes
# q，signed long long，-9223372036854775808至9223372036854775807之間的整數，8bytes
# Q，unsigned long long，0至18446744073709551615之間的整數，8bytes
# f，float，單精度浮點數，只能保證小數點後6位的運算準確，4bytes
# d，double，雙精度浮點數，只能保證小數點後15位的運算準確，8bytes
