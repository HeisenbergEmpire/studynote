# 以下三種用法只是編寫時略有不同，對於邏輯與代碼運行效率沒有不同
# 第一種方法，表示只是導入helpers模塊，所以每個helpers模塊裡面的函數都在前面加上helpers.才能運用
import helpers
helpers.display('Not a warning',True)

# 第二種方法，意思是從helpers模塊中調用所有函數（星號代表所有的意思）
from helpers import *
display('Not a warning')

# 第三種方法，意思是從helpers模塊中調用display函數，調用單個函數的好處在於，vscode在聯想時不會因為同首字母彈出大量詞彙
from helpers import display
display('Not a warning')
