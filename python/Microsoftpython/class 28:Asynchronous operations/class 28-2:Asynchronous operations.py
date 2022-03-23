import requests
import time
import asyncio
import aiohttp
from timeit import default_timer


# 第六節第一小節例子

async def func1():
    print("func1")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2")
    await asyncio.sleep(1)
    print("func2 end")

async def gatherwait():
    task = [asyncio.create_task(func1()), asyncio.create_task(func2())]
    await asyncio.wait(task)
    # await asyncio.gather(*task)

    # taskA = func1()
    # taskB = func2()
    # await asyncio.gather(task1, task2)

asyncio.run(gatherwait())

print()

# 第六節第二小節例子1：
async def func1():
    print("func1")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2")
    await asyncio.sleep(1)
    print("func2 end")

async def waitexp():
    print('start')

    task_list1 = [asyncio.create_task(func1()), asyncio.create_task(func2())]

    await asyncio.wait(task_list1, timeout=0.5)

    print('finish')

asyncio.run(waitexp())

print()

# 第六節第二小節例子2：
import asyncio

async def func1():
    print("func1")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2")
    await asyncio.sleep(1)
    print("func2 end")
    return 'func2 finish'

async def waitexp():
    print('start')

    task_list1 = [asyncio.create_task(func1()), asyncio.create_task(func2())]

    done = await asyncio.wait(task_list1)

    print(done)

    print('finish')

asyncio.run(waitexp())

print()

# 第六節第二小節例子3:
import asyncio

async def func1():
    print("func1")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2")
    await asyncio.sleep(1)
    print("func2 end")
    return 'func2 finish'

async def waitexp():
    print('start')

    task_list1 = [asyncio.create_task(func1()), asyncio.create_task(func2())]

    done, pending = await asyncio.wait(task_list1, timeout=0.5)
    print(done) 
    print(pending)

    print('finish')

asyncio.run(waitexp())

print()

# 第六節第二小節例子4:
import asyncio

async def func1():
    print("func1")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2")
    await asyncio.sleep(1)
    print("func2 end")
    return 'func2 return'

async def waitexp():
    print('start')

    task_list1 = [
        asyncio.create_task(func1(), name='func1'),
        asyncio.create_task(func2(), name='func2'),
    ]

    done, pengding = await asyncio.wait(task_list1,timeout=2)
    print(done,pengding)

    print('finish')

asyncio.run(waitexp())

print()

# 第六節第三小節例子1
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
        two_task = load_data(session, 2) 
        three_task = load_data(session, 3)

        # 這裡當task執行後，text進入等候，然後下面便要等候sleep結束，print出doing other work
        await asyncio.sleep(1)
        print('Doing other work')

        # 之後就等待兩個task結束才能進行下一步，而task裡就進行到text，當中就有delay停頓，兩個task重疊便停頓3秒
        # two_result = await two_task
        # three_result = await three_task
        # 這裡就是等待兩個task結束，並且把兩個task的結果gather起來，並且把結果傳回result
        # 並且不用create_task()因為gather()已經把task自動放入event_loop裡了
        result = await asyncio.gather(two_task, three_task) 

        # 接著兩個task返回text值，寫在了Completed {delay} second timer裡，接著兩個task結束，print出總用時值（即elapsed time）
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(elapsedtime())

print()

# 第六節第三小節例子2:
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
        two_task = load_data(session, 2)
        three_task = load_data(session, 3)
        task_list = [two_task, three_task]
        # 這裡當task執行後，text進入等候，然後下面便要等候sleep結束，print出doing other work
        await asyncio.sleep(1)
        print('Doing other work')

        result = await asyncio.gather(*task_list) # 這裡就是等待整個list都得到結果，並且將結果放入result

        # 接著兩個task返回text值，寫在了Completed {delay} second timer裡，接著兩個task結束，print出總用時值（即elapsed time）
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(elapsedtime())

print()

# 第六節第三小節例子3:

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp: # 此處，resp等於session.get(url)
        text = await resp.text() # 這裡即等於awiat session.get(url).text()
        print(f'Completed {delay} second timer')
        return text

async def sleep(): 
    await asyncio.sleep(1)
    print('Doing other work')

async def elapsedtime():
    # Start the timer
    start_time = default_timer()

    # Creating a single session
    # 下面，session等於aiohttp.ClientSession()，聯繫load_data()中的session，則resp等於aiohttp.ClientSession().get(url)
    async with aiohttp.ClientSession() as session: 
        # 下面，load_data()中的text等於await aiohttp.ClientSession().get(http://httpbin.org/delay/1).text()，當中text()對應return text的值
        one_task = sleep()
        two_task = load_data(session, 2) 
        three_task = load_data(session, 3)
        task_list = [one_task, two_task, three_task]
        # 這裡當task執行後，text進入等候，然後下面便要等候sleep結束，print出doing other work
        # await asyncio.sleep(1)
        # print('Doing other work')

        # 之後就等待兩個task結束才能進行下一步，而task裡就進行到text，當中就有delay停頓，兩個task重疊便停頓3秒
        # two_result = await two_task
        # three_result = await three_task

        # 這裡就是等待三個task結束，並且把三個task的結果gather起來，並且把結果傳回result
        # 並且不用create_task()因為gather()已經把task自動放入event_loop裡了
        result = await asyncio.gather(*task_list)

        # 接著兩個task返回text值，寫在了Completed {delay} second timer裡，接著兩個task結束，print出總用時值（即elapsed time）
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

# md文檔裡是下面兩句，但由於3.10之後已經沒有get_event_loop()，令整個課例程式執行不能，所以改成run，單獨抽出來運行可以
# loop = asyncio.get_event_loop()
# loop.run_until_complete(elapsedtime())
asyncio.run(elapsedtime())

print()

# 第七節第一例子

def fib(n):
    if n in [1,2]:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()
print(fib(38))
end = time.time()

print(end-start)

print()

# 第一節第一個例子：

async def send_req():
    await asyncio.sleep(5) # 假設等待5秒

def fib(n):
    if n in [1,2]:
        return n
    return fib(n-1) + fib(n-2)

async def fibn(n):
    print(fib(n))

async def usetime():
    start = time.time()
    task3 = fibn(38)
    task4 = send_req()
    await asyncio.gather(task3,task4)
    end = time.time()
    print(end-start)

asyncio.run(usetime())

print()

# 第一節第二個例子：
async def request():
    await asyncio.sleep(5)

def fibA(n):
    if n in [1,2]:
        return n
    return calc_fib(n-1) + calc_fib(n-2)

def calc_fib(n):
    result = fibA(n)
    # 以下一段留待改變數值執行以觀run_in_executor之結果
    # print(f'the {n}th fibonacci number is {result}')
    return result

async def needtime():
    start = time.time()
    loop = asyncio.get_event_loop() #創建一個event loop任務例表
    # 下面是將calc_fib包裝成一個任務並分解執行，注意executor不接受關鍵字參數，只接受位置参数，第一位是用於執行的模塊功能，第二位是函數名，第三位是參數
    # 便要使用None佔位，因為沒有用於執行的模塊功能，只是為了讓executor執行，若有，則需要用with...as...來包裝成一個executor傳入None位
    task3 = loop.run_in_executor(None, calc_fib, 38)
    task4 = request()
    await asyncio.gather(task3,task4)
    end = time.time()
    print(end-start)

asyncio.run(needtime())

print()

# 第八節第一例子

async def req(delay):
    print(f'waiting for semaphore with {delay} seconds delay')
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.google.com.tw') as resp:
            print(f'got response {resp.status}')
            await asyncio.sleep(delay)

async def semtext():
    start = time.time()
    delay_list = [3,2,8,4,1,5,7,6,9,10,3,6]
    task_list= []
    for delay in delay_list:
        task = asyncio.create_task(req(delay))
        task_list.append(task)
    await asyncio.gather(*task_list)

    end = time.time()
    print(f'cost {end-start} seconds')

asyncio.run(semtext())

print()

# 第八節第二例子

async def req(delay,sem):
    print(f'waiting for semaphore with {delay} seconds delay')
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://www.google.com.tw') as resp:
                print(f'got response {resp.status}')
                await asyncio.sleep(delay)

async def semtext():
    start = time.time()
    delay_list = [3,2,8,4,1,5,7,6,9,10,3,6]
    task_list= []
    sem = asyncio.Semaphore(3)
    for delay in delay_list:
        task = asyncio.create_task(req(delay,sem))
        task_list.append(task)
    await asyncio.gather(*task_list)

    end = time.time()
    print(f'cost {end-start} seconds')

asyncio.run(semtext())

print()

# 第九節第一個例子：

url = 'https://www.google.com.tw/'

class activate:
    def __init__(self):
        self.name = 'Heisenberg'

    async def req(self,url):
        async with aiohttp.ClientSession() as client:
            resp = await client.get(url)
            print(resp)

test = activate()

asyncio.run(test.req(url))

print()

# 第十節例子

async def cron_job(url, usetime):
    await asyncio.sleep(usetime)
    print(f'get {url} done in {usetime} seconds')


async def cron_scheduler():
    task_list = []
    page = 10
    usetime = 1
    while page >= 0 and usetime <= 11:
        url = f'http://www.last{page}daysoftheworld.com/{page}day.html'
        task = asyncio.create_task(cron_job(url, usetime))
        task_list.append(task)
        page -= 1
        usetime += 1
    
    await asyncio.gather(*task_list)
    print('goodbye, cruel world!')

asyncio.run(cron_scheduler())

print()
