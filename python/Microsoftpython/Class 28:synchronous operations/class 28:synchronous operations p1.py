# timeit為計時工具庫
from timeit import default_timer
# requests為獲取api服務的庫
import requests

def load_data(delay):
    print(f'Starting {delay} second timer')
    text = requests.get(f'http://httpbin.org/delay/{delay}').text
    print(f'Completed {delay} second timer')
   
def run_demo():
    start_time = default_timer() # 設置這個start_time為初始時間即0秒

    two_data = load_data(2) # 這個two_data的假設用時（以延時delay來表達）為2秒
    three_data = load_data(3) # 這個three_data的假設用時（以延時delay來表達）為3秒

    elapsed_time = default_timer() - start_time # 結束時間 - 開始時間 = 用時
    print(f'The operation took {elapsed_time:.2} seconds')

# 包入函數main是為了和之後作比較
def main():
    run_demo()

main()
