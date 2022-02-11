# python之中僅有兩種循環，for和while
# 以下先從for循環講起,意思為打印出name變量中每一個值
for name in ['Heisenberg', 'White', 'Walter', 'Jesse', 'Gustavo']:
    print(name)
print()

# 下面range是代表index變量是從數字0至1
for index in range(0,2):
    print(index)
print()

# 下面是while的應用，意思為while（當）index的值小於name變量詞的值數量
# 則打印（name【index數值位】），index加1，（name【index數值位】），index加1
# 如此循環直到while（當）index值大於或等於name值數量，while循環結束
name = ['Heisenebrg', 'White', 'Walter', 'Jesse', 'Gustavo']
index = 0
while index<len(name):
    print(name[index])
    index = index + 1
print()
# 同樣的意義用for循環來做就更簡潔，所以可以用for就不用while了
for i in name:
    print(i)

# 且for為有限循環，循環完即停止；而while為無限循環，假若條件設錯就會造成無限循環錯誤
