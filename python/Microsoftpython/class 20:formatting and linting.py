# 一段格式錯誤的有效代碼例子
x = 12
if x== 24:
 print('Is valid')
else:
    print("Is not valid")

def helper(name='sample'):
 pass

def another( name = 'sample'):
         pass

print()

# 文檔字符串例子
def print_hello(name: str) -> str:
    """
    Greets the user by name


    Parameters
        name(str): The name of the user

    Returns
        str: The greeting
    """
    print('Hello,' + name)

print_hello('heisenberg')