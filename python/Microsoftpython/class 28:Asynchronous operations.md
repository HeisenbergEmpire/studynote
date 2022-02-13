# python學習筆記

## 第二十八課：簡述異步編程概念

### 1.本課基礎例子

此例為一效率慢的操作辦法,為了和之後效率快的辦法作比較，下面會進行數字標記

&nbsp;

part1（因為part2會設置一個延遲時間來做一個假設執行的“用時”，所以下面會print出使用秒數）:

```
# timeit為計時工具庫
from timeit import default_timer
# requests為獲取api服務的庫
import requests
```

以`load_data()`函數獲取名為`delay`的api服務（此服務除延時並沒有其他作用），並print出開始（`starting`）服務至結束服務的使用秒數（`second timer`）

<br>

`text`行為獲取此api服務作測試

```
def load_data(delay):
    print(f'Starting {delay} second timer')
    text = requests.get(f'http://httpbin.org/delay/{delay}').text
    print(f'Completed {delay} second timer')
```

&nbsp;

part2：

```
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
```

&nbsp;

最後terminal執行顯示的內容為：
```
Starting 2 second timer # two_task
Completed 2 second timer # three_task
Starting 3 second timer # two_task
Completed 3 second timer # three_task
The operation took 6.3 second # 運行用時為5秒，另外1.3秒為連接、顯示等的用時
```

&nbsp;

這裡的執行流程可以看得出是，先執行`two_data`，待其結束才執行`three_data`，所以用時為
```
two_data(2s) + three_data(3s) + run&connect（1.3s） = 6.3s
```

&nbsp;

### 2.異步例子（效率快的例子）

part1:

&nbsp;

前置，引入aiohttp（第三方庫需自行下載）與asyncio庫

```
from timeit import default_timer
import aiohttp
import asyncio
```

下面`async`在`def`前面才能使用`awite`，第三行`async`開始至第六行`return`行意思為用獲取`delay`api服務

<br>

`resp.text()`暫停並等待（即`await`)`print`行同時執行，`print`執行時返回（`return`）text的`delay`延時值存入`print`中顯示

```
async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed {delay} second timer')
        return text
```

&nbsp;

part2:

```
async def main():
    # Start the timer
    start_time = default_timer()

    # Creating a single session
    async with aiohttp.ClientSession() as session:
        # Setup our tasks and get them running
        two_task = asyncio.create_task(load_data(session, 2))
        three_task = asyncio.create_task(load_data(session, 3))

        # 這裡對應下面asyncio.run()，意思是讓整個main函數暫停並print出Doing other work
        await asyncio.sleep(1)
        print('Doing other work')

        # Let's go get our values
        two_result = await two_task
        three_result = await three_task

        # Print our results
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(main())
```

&nbsp;

上面意思為創建兩個任務（`create_task`)，名為`two_task`和`three_task`，任務內容為part1的`load_data`函數

<br>

讓`two_task`與`three_task`同時暫停並等待（即`await`）對方準備好同時執行，之後`asyncio.run()`讓`main`函數整體停下（sleep）

<br>

並print出Doing other work，之後兩個分別結束

最後terminal顯示如下：

```
Starting 2 second timer # two_task
Starting 3 second timer # three_task
Doing other work
Completed 2 second timer # two_task
Completed 3 second timer # three_task
The operation took 3.3 seconds
```

運行時間為3.3秒，因為同時進行，所以two_task的兩秒已經包含在three_task中，實際為3秒，0.3秒為連結與執行顯示等時間

## 不太明白的，可以對比兩例中的part1和part2同時進行比較