# 在日常中，如果我們開啟文件流運作（I：O），一定要注意關閉（close），不然下次打開會出現錯誤
# 一整套流程就是open-read-close
stream = open('text.txt', 'wt')
stream.write('Lorem ipsum dolar')
stream.close() # 非常重要，關閉流

# 有時我們為了防止錯誤，例如對文件沒有讀寫權限、文件不存在等，我們會使用try-finally來處理，即使前面錯誤亦保證會關閉流
try:
    stream = open('text.txt', 'wt')
    stream.write('Lorem ipsum dolar')
finally:
    stream.close() # 再次提示，非常重要，關閉流

# 如果要簡便一些，我們可以使用with來處理，這樣就不用自己關閉流了，也有try-finally的效果
with open('text.txt', 'wt') as stream:
    stream.write('Say my name:Heisenberg')