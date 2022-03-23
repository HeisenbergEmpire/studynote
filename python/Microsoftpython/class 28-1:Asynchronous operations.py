import requests
import time
import asyncio
import aiohttp
import uvloop
from timeit import default_timer
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# 第一節第一個原例
url = 'https://www.google.com.tw/'

start_time = time.time()

def send_req(url):

    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    res = requests.get(url)

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

for i in range(5):
    send_req(url)

print()

# 第一節第一個異步例子

url = 'https://www.google.com.tw/' # 設定url網址，當然也可以在session.get()括號裡自己輸入

start_time = time.time() # 設定初始時間等於0

async def send_req(session,url):
    t = time.time() # 設定打印函數啟動時間（發送時間）
    print("Send a request at",t-start_time,"seconds.")

    await session.get(url) # 等待獲取url服務返回

    t = time.time() # 等待完畢，打印函數結束時間（返回服務時間）
    print("Receive a response at",t-start_time,"seconds.")

async def main():
    async with aiohttp.ClientSession() as session: # 把連接池（現在只有一個網址，所以就是那個服務內容）定義為session並繼承
        tasks = []
        for i in range(10): # 設定循環10次的任務，asyncio.create_task為創建任務
            tasks.append(asyncio.create_task(send_req(session,url))) # 去掉asyncio.create_task()也可以就當普通攜程
        
        await asyncio.gather(*tasks) # 等待並收集10次循環的結果，因為有這個gather所以是否創建任務無所謂


if __name__ == '__main__':
    asyncio.run(main()) # 運行攜程函數main()

print()

# 第一節第一個異步例子簡化版
url = 'https://www.google.com.tw/'

start_time = time.time()

async def send_req(session,url):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    await session.get(url)

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

async def main():
    async with aiohttp.ClientSession() as session: # 設定循環10次的任務，asyncio.create_task為創建任務
        tasks = [asyncio.create_task(send_req(session,url)) for i in range(10)] # 去掉asyncio.create_task()也可以
        await asyncio.gather(*tasks) # 等待並收集10次循環的結果，因為有這個gather所以是否創建任務無所謂

if __name__ == '__main__':
    asyncio.run(main())

print()

# 第二節例

# 以下是一個函數的創建與執行
def main1(): # 創建
    print('Heisenberg') # 內容

main1() #執行

# 以下是一個協程的創建與執行

async def main2(): # 創建
    print('Heisenberg') # 內容

asyncio.run(main2()) # 執行 

print()

# 第三節例子

async def foo(x):
    print(x)
    # 實際上這個sleep的原理和time.sleep()是不一樣的，time.sleep是把整個進程終止掉，而asyncio.sleep是把協程退出讓給下一個協程使用，直到sleep時間結束
    await asyncio.sleep(1) 

async def text():
    print('this is a')
    await foo('text') # 此處await必須添加，不然則代表text協程不等待foo協程sleep就結束，這樣就和協程foo中的await嚴重矛盾會導致出錯
    print('finished') # 到這步會看到finished之前會停頓1秒

asyncio.run(text())

print()

# 第三節第二個例子

async def asyncfunction():
    print("I am a async function")
    return 'Heisenberg'

async def callback():
    print('I used the return value of asyncfunction')
    result = await asyncfunction()
    print('The return value of asyncfunction is:', result)

async def matryoshka():
    print('I will use the async function which used the async function')
    await callback()

asyncio.run(matryoshka())

print()

# 第四節第一小節例子1

async def foo1(x):
    print(x)
    await asyncio.sleep(3)
    print('done')

async def text1():
    print('this is a')
    task = asyncio.create_task(foo1('text')).add_done_callback(lambda y: print('well done'))
    await asyncio.sleep(1)
    print('finished')

asyncio.run(text1())

print()

# 第四節第一小節例子2
async def foo(x):
    print(x)
    await asyncio.sleep(1)
    print('done')

async def text():
    print('this is a')
    task = asyncio.create_task(foo('text'))
    await task
    print('finished')

asyncio.run(text())

# 第四節第一小節例子3
import asyncio

async def foo(x):
    print(x)
    await asyncio.sleep(3)
    print('done')

async def text():
    print('this is a')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(1)
    print('finished')

asyncio.run(text())

# 第四節第二小節例子1

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(xxx())

print()

# 第四節第二小節例子2
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)

asyncio.run(xxx())

print()

# 第四節第二小節例子3
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    await task2
    value = await task1
    print(value)

asyncio.run(xxx())

print()

# 第四節第二小節例子4
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    await fetch_data()
    await print_numbers()

asyncio.run(xxx())

print()

# 第四節第二小節例子5
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    task2 = asyncio.create_task(print_numbers())

    await fetch_data()
    await task2

asyncio.run(xxx())

print()

# 第四節第二小節例子6
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    await task2
    value = await task1
    print(value)

asyncio.run(xxx())

print()

# 第四節第二小節例子7
import asyncio

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    print('start')

    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print('end')

    await task2
    print(value)

asyncio.run(xxx())

print()

# 第四節第二小節例子8
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    print('start')

    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    await task2
    print('end')

    value = await task1
    print(value)

asyncio.run(xxx())

print()

# 第四節第二小節例子9
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def xxx():
    print('start')

    task1 = asyncio.create_task(fetch_data())
    value = await task1

    print('end')

    task2 = asyncio.create_task(print_numbers())
    await task2
    
    print(value)

asyncio.run(xxx())

print()

# 第四節第三小節例子

async def foo2(x):
    print(x)
    await asyncio.sleep(1)
    print('done')

async def text2():
    print('this is a')

# 將await foo('text')改成如下task
# 在(foo('text')).add_done_callback(lambda x: print('well done'))，可以在task完成後反饋（callback）一個well done

    task = asyncio.create_task(foo2('text')) #.add_done_callback(lambda x: print('well done'))（在有await後只能賦在task後）
    await task
    task.add_done_callback(lambda y: print('well done'))
    print('finished')

asyncio.run(text2())

print()

# 第四節第四小節

async def cron_job(url):
    await asyncio.sleep(2)
    print(f'get {url} done in 2 seconds')


async def cron_scheduler():
    start = time.time()
    future_list = []
    page = 10
    while page >= 0:
        url = f'http://www.last{page}daysoftheworld.com/{page}day.html'
        future = asyncio.ensure_future(cron_job(url))
        future_list.append(future)
        page -= 1
        future.add_done_callback(lambda future: print('goodbye, cruel world'))
    
    await asyncio.gather(*future_list)
    end = time.time()
    print(f'{end - start} seconds')

start = time.time()
uvloop.install()
asyncio.run(cron_scheduler())
end = time.time()
print(f'{end - start} seconds')

print()

# 第五節例子

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp: # 此處，resp等於session.get(url)
        text = await resp.text() # 這裡即等於awiat session.get(url).text()
        print(f'Completed {delay} second timer')
        return text

async def elapsedtime():
    # Start the timer
    start_time = default_timer()

    # Creating a single session
    # 下面，session等於aiohttp.ClientSession()，聯繫load_data()中的session，則resp等於aiohttp.ClientSession().get(url)
    async with aiohttp.ClientSession() as session: 
        # 下面，load_data()中的text等於await aiohttp.ClientSession().get(http://httpbin.org/delay/1).text()，當中text()對應return text的值
        two_task = asyncio.create_task(load_data(session, 2)) 
        three_task = asyncio.create_task(load_data(session, 3)) 

        # 這裡當task執行後，text進入等候，然後下面便要等候sleep結束，print出doing other work
        await asyncio.sleep(1)
        print('Doing other work')

        # 之後就等待兩個task結束才能進行下一步，而task裡就進行到text，當中就有delay停頓，兩個task重疊便停頓3秒
        two_result = await two_task
        three_result = await three_task # 其實由於three_task是等待3秒，所以直接await three_task就可以了，無需await two_task

        # 接著兩個task返回text值，寫在了Completed {delay} second timer裡，接著兩個task結束，print出總用時值（即elapsed time）
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

uvloop.install()
asyncio.run(elapsedtime())