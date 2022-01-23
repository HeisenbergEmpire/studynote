# 前置，從dotenv導入load_dotenv，用於讀取env文件，及導入os獲取env文件
from dotenv import load_dotenv
load_dotenv()
import os
# 例1，從env文件中讀取password值
password = os.getenv('PASSWORD')
print(password)

print()
# 例2，從env文件中讀取database值
database = os.getenv('DATABASE')
print(database)