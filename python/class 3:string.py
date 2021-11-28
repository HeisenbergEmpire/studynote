# 留意引號在單詞和變量詞之間使用的不同,當變量詞再次輸入的時候，可以按tab即可自動補全不用打全部字
first_name = 'heisenberg'
last_name = 'chueng'
print(first_name + last_name)
print('Hello,' + first_name.capitalize()+ ' ' + last_name.capitalize())
print()
print()
# 以下命令釋義：upper是全大寫，lower是全小寫，capitalize是首字母大寫，count是計算，例子中count的意思為計算a字母在sentence變量值中a出現的次數
sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))
print()
print()
# input為輸入結果，input作為變量值即輸入結果為最終變量值，input後（）內的內容為input文本前置內容
ming = input('what is your ming?')
xing = input('what is your xing?')
print('Hello,' + ming.capitalize() + ' '\
    + xing.capitalize())
# 另外小技巧，命令如果太長需要換行，最後可以加個 \，也是釋義符的運用之一，如上便是例子
# 當某行某段出現波浪下劃線，代表該段代碼有問題