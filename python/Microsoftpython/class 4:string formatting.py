# 此為上一課的原始代碼
first_name = 'heisenberg'
last_name = 'chueng'
print(first_name + last_name)
print('Hello,' + first_name.capitalize()+ ' ' + last_name.capitalize())
print()
print()
# 加號變代碼格式化,使用{}佔位符來代表變量詞的實際位置和用format來代表變量詞的組成,以上面最後一段為演示
output1 = 'Hello,{} {}'.format(first_name, last_name)
print(output1)
print()
# 如果要變量詞以自己指定的位置排列，這時可以用到數字，format內第一項為數字0，類推
output2 = 'Hello,{1} {0}'.format(first_name, last_name)
print(output2)
# 如上，變量詞與上一例輸出位置發生變化，謹記第一項為數字0
print()
# 另外，可以用{}括住變量詞直接插入，僅需在前面加上f或者F代表format（此方法僅可使用于py3及以後版本，但不可用於py3.3.2，如下
output3 = f'Hello,{first_name} {last_name}'
print(output3)
print()
# 除此之外，還有這樣一種佔位用法
output4 = 'Hello,%s %s'%(first_name, last_name)
print(output4)
