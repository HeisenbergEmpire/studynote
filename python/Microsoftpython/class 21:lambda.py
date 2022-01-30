# 本課例子，排列名稱，sort()函數為排序函數，如下排列名稱：
def sorter(item):
    return item['name']

presenters = [
    {'name': 'Heisenberg', 'age': 25},
    {'name': 'Alex', 'age': 30},
]

presenters.sort(key=sorter)
print(presenters)

print()

# 本課例子中如果簡化排序，不特意為幾行代碼特意使用def，可以使用lambda函數，如下：
# 注意，這個lambda是一個函數，與上文的def.sorter()的效果等同，只是沒有定義函數名稱（即沒有sorter，後面打sorter()沒有用
# 所以，這個lambda函數沒有名稱，只有一個參數，內容為item，item為一個參數，又注意這裡lambda item1是一整個函數
# 因此，這個lambda函數可以接受一個參數，並且可以回傳一個值，這個值為item['name']，item['name']為字典的key，這裡的item與上文的item相同
# 以及一些代碼清晰排列的小花招
presenters1 = [
    {'name': 'Heisenberg', 'age': 25},
    {'name': 'Alex', 'age': 30},
]

presenters1.sort(key=lambda item1: item1['name'])
print('--presenters1--')
print('presenters1:', presenters1)

print()

# 多給一個例子，可以為item['name']添加一個屬性，並且排序，如下以名字長短排序：
presenters2 = [
    {'name': 'Heisenberg', 'age': 25},
    {'name': 'Alex', 'age': 30},
]

presenters2.sort(key=lambda item2: len(item2['name']))
print('--presenters2--')
print('presenters2:', presenters2)

print()

# 再多給一個例子，可以為參數item['name']與item['age']同時排序，並可添加屬性，如下：
# 當然這個同時排序是沒有意義的，因為這個排序是按照年齡排序，只是同時把名字放上去
# 這裡只是演示一下lambda的功能,令代碼更簡潔
presenters3 = [
    {'name': 'Heisenberg', 'age': 25},
    {'name': 'Alex', 'age': 30},
]

presenters3.sort(key=lambda item3: (item3['age'], len(item3['name'])))
print('--presenters3--')
print('presenters3:', presenters3)

print()