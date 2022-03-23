# python學習筆記

## 第二十八課：詳述異步

### 1.異步基本概念與演示

#### 一.基礎理論

python在並發(concurrency)任務中，雖然本身還是只能達到單核CPU的效能，無法達到完全的平行(parallelism)運算  
但相比於單核cpu的效能，很多操作要是一個一個執行起來，還是比cpu慢太多，  
好比網路io操作，cpu從收到response到發送request的時間連千分之一秒都不用，但發送後等送到response時間就得0.2～0.3秒  
雖然對於人類的時間很短，但非常不符合電腦的效益  

&nbsp;

就好比在一條高速公路上，前面有台貨運大卡車在緩慢行駛，司機還在邊抽菸邊聊電話，此時你在後面即使開著一台擁有v8渦輪發動機的跑車  
由於只能在單一線路上行駛，所以只好無奈地等待前面的大卡車  
而這樣就叫做阻塞，如果我們在高速公路上能有更多條車道，那麼你的超快跑車就不用等待前面的大卡車能直接超車了  
這就是非阻塞，即增加更多的線程

&nbsp;

事實上，一個阻塞線程在對其需求的數據執行操作的時候，它就是在操作權上上了一個鎖  
（global interpreter lock，全局解釋器鎖，其目的是用預處理數據的方式加速運行與保護關鍵共享數據結構免受損壞，但其實預處理的方式是幼稚的，用時實質一致）  
直到操作完畢才解鎖  

&nbsp;

而當兩個線程同時對同一數據作出不同操作的時候，假設第一個線程幸運地先獲得了數據的操作權，對其上了鎖，那麼另一個線程在這時只能夠乾等，  
直到第一個線程執行操作完畢解鎖後，第二個線程才能進行操作，而這時，第一個線程也只能無聊地乾等。

&nbsp;

若現在有四五個線程要對同一個數據進行操作，那麼就很有可能其中有一兩個線程，直到整個進程（一個進程可以包含多個線程）結束都未能有機會對數據作任何操作，就被主進程直接結束了

&nbsp;

所以asyncio的目的是使用異步處理並通過使用協同程序啟用並發代碼來使單線程得到最大化利用，當然使用協程，除了asyncio，還有trio和yield生成器也可以做，但asyncio是python自帶標準庫。

&nbsp;

事實上，協程的好處不單單是充分利用CPU單核的效率提升，在現今社會，網速已經達到了百兆甚至千兆，而對於只有幾kb至幾十kb數據的的網絡交互請求（若不包含圖片視頻），只是單線程阻塞型的操作亦明顯沒有利用好帶寬


#### 二.並發與並行

用bartender做例子，一個bartender只能在一次調較一種飲料，但他可以一次照顧幾個客人，這叫並發

&nbsp;

而並行則需要請幾個調酒師

&nbsp;

實際上，asyncio是並發的而不是並行，因為它僅僅是在使用單核運算，而若果真的想python使用並行，其實今天有很多方式已經可以達到

&nbsp;

#### 三.實例展示異步處理的好處

下面用一個對url重複操作的request來看看效率到底有多慢
```
import requests
import time

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
```

結果如下：

```
Send a request at 9.5367431640625e-07 seconds.
Receive a response at 0.24921870231628418 seconds.
Send a request at 0.2493278980255127 seconds.
Receive a response at 0.45850086212158203 seconds.
Send a request at 0.45862388610839844 seconds.
Receive a response at 0.7273769378662109 seconds.
Send a request at 0.7274868488311768 seconds.
Receive a response at 0.9692249298095703 seconds.
Send a request at 0.969343900680542 seconds.
Receive a response at 1.1745657920837402 seconds.
```
這是很正常的，當程式接收到網路來的response到繼續發送下一個request，中間所需要的時間就只是讓CPU去執行下一個python指令，  
但是發送request之後，到接收到response中間是需要等待網路另一端的server去回傳response，所需時間當然要長多了。

&nbsp;

**所以發送request後，中間傻等就很智障，而異步的好處就在於程序不用傻等，一邊等自動提醒收到response（異步），一邊愛幹嘛幹嘛去（非阻塞）**

&nbsp;

下面用asyncio模組以異步非阻塞的方式做上一段程式所做的事，程序的細節先嫑理會，看執行效率是否有提升

```
import aiohttp
import time
import asyncio

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
```

還可以簡化成這樣：

```
import aiohttp
import time
import asyncio

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
```
相對來說，用`asyncio.create_task`比不用要好，因為創建了任務就會紀錄整個協程進行期間的“上下文”並且保證任務有callback（返回）  
在loop時代是必須要創建任務才能被`loop = asyncio.get_event_loop()`和`loop.run_until_complete`調用

&nbsp;

**要注意`request.get()`不是一個攜程，是不可打斷的，所以不能用await，如果要用`request`就要用到`loop`的方法，如下（比較不便和落後）：**
```
import requests
import time
import asyncio

url = 'https://www.google.com.tw/'
loop = asyncio.get_event_loop()

start_time = time.time()

async def send_req(url):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    res = await loop.run_in_executor(None,requests.get,url) # request.get不可以稱為協程，所以要用run_in_executor將它定義為協程

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

tasks = []

for i in range(10):
    task = loop.create_task(send_req(url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
```

&nbsp;

輸出的結果是：

```
Send a request at 0.0005939006805419922 seconds.
Send a request at 0.0012447834014892578 seconds.
Send a request at 0.001558065414428711 seconds.
Send a request at 0.001840829849243164 seconds.
Send a request at 0.002079010009765625 seconds.
Send a request at 0.002344846725463867 seconds.
Send a request at 0.002588987350463867 seconds.
Send a request at 0.002850770950317383 seconds.
Send a request at 0.0030930042266845703 seconds.
Send a request at 0.0033979415893554688 seconds.
Receive a response at 0.3997218608856201 seconds.
Receive a response at 0.4014577865600586 seconds.
Receive a response at 0.4039268493652344 seconds.
Receive a response at 0.40762972831726074 seconds.
Receive a response at 0.410524845123291 seconds.
Receive a response at 0.4114408493041992 seconds.
Receive a response at 0.4166998863220215 seconds.
Receive a response at 0.41788291931152344 seconds.
Receive a response at 0.42113780975341797 seconds.
Receive a response at 0.42241382598876953 seconds.
```

1.17秒和0.42秒，簡直快了三倍，可以看出程式在發完一個request之後並沒有停下，而是將剩下九個繼續發完，等0.39秒之後得到連續返回，果然乾等真傻

&nbsp;

### 2.實際概念

#### 一.協程(coroutines)

首先，協程（Coroutine）並非計算機中真實存在的，計算機中只有進程和線程，而協程是程序猿人為創造的。  
專業來上來說叫微線程，是一種用戶態內的上下文切換技術。它的原理，是通過一個線程實現代碼塊相互切換執行  
簡單來說就是在幾個函數間切換執行，需要注意諸如類的後續（例如`asyncio.sleep()`)或者系統自帶函數（`print`、`str`）本身也是函數，即代碼塊

&nbsp;

就如同電腦多線程工作一樣，微線程亦可像多線程一樣同時進行，只要它在一個線程任務列表（event loop，又稱事件迴圈）上  
以下是協程的詳細定義

&nbsp;

實際上，python中的函數（`def`），絕大部分都是同步（完成不返回callback提示）且阻塞（一步一步地完成，未完成時不會幹其他東西）的  
若果在`def`前面加上一個`async`，這樣就會將這個函數定義為一個協程（Coroutine）

&nbsp;

以下是協程的詳細定義

```
# 协程，又称微线程，纤程，英文名Coroutine。协程的作用是在执行函数A时可以随时中断去执行函数B，然后中断函数B继续执行函数A（可以自由切换）
# 但这一过程并不是函数调用，这一整个过程看似像多线程，然而协程只有一个线程执行。
```

&nbsp;

以下我們函數（`def`）和協程之間一個簡單的對比

```
# 以下是一個函數的創建與執行
def main(): # 創建
    print('Heisenberg') # 內容

main() #執行

# 以下是一個協程的創建與執行
import asyncio

async def main(): # 創建
    print('Heisenberg') # 內容

asyncio.run(main()) # 執行 
```
事實上，一個函數`def`只要前面加上了`asyncio`，就會被定義為一個協程

&nbsp;

而兩者在執行上的不同在於，函數用`main()`就可以執行了，而協程則需要在前面加上`asyncio.run()`，事實上`asyncio`包含了三個動作  
只是後來被簡化了。且若果需要理解一段異步代碼，那麼必先要從asyncio.run()去理解，括號裏的協程就是程序輸出口（或稱程式入口）。

```
loop = asyncio.get_event_loop() # 創建事件循環（即線程任務列表，event loop）

loop.run_until_complete(main()) # 執行該協程（這裡即main())

loop.close() # 關閉事件循環（畢竟任務執行完畢，任務列表就沒必要存在）

# 以上三句現在就歸納為一句
asyncio.run(main())
```

**實際上，我們現在就是創建了一個event loop（事件循環，異步線程任務列表）**這個概念要注意

&nbsp;

#### 二.協程和協程對象

def前面有async的函數就稱為協程，而一個協程在其他地方（即`攜程名()`）則稱為協程對像

#### 三.事件循環（event loop）

可以理解成是一個while true型的循環，這個循環會檢測在列表中的所有task或future，若果可執行的全部執行，並等待該任務的完成回應（callback）  
當`create_task`或者`ensure_future`之後，任務清單event loop中就會有task1、task2、task3......，即你設立了多少個任務就會有多少個task  
若task或future處于等待callback中，則檢查有沒有其他task或future剛好需要執行或繼續執行，若有則執行，若無則繼續等待callback  
若等待到callback返回，則檢查callback返回後是否有內容需要繼續執行，若有則執行，若無則從event loop中註銷
若循環中所有task或future都已完成（future則除了等待完成還有等待return），則event loop將得到所有task或future已完成的總callback，則終止event loop

&nbsp;

注意，當協程中沒有`await`，協程只會在event loop裡面當作普通函數，以阻塞方式執行  
若只是`create task`或者`ensure_future`，前面沒有await，則task或future不會等待callback，執行後直接被完成，不會等待裡面的`await`  
除非用的是`gather`或者`wait`

&nbsp;

### 3.await（等待）

`await`是異步中一個常見的命令，代表等待`await`（某事）的發生，  
不過實際上它不只是在乾等，而是等待的同時交出執行權讓其他task或future執行，在等待結束有callback在繼續執行原協程

&nbsp;

先看看以下例子：
```
import asyncio

async def foo(x):
    print(x)
    await asyncio.sleep(1)
    print('done')

async def text():
    print('this is a')

# 此處await必須添加，不然則代表text協程不等待foo協程就結束，因為foo中有await，text沒有await就等於foo完全沒有被執行，但又寫在了text裡面就會報錯

    await foo('text')
    print('finished') # 到這步會看到finished之前會停頓1秒

asyncio.run(text())
```

實際上這個`asyncio.sleep()`的原理和`time.sleep()`是不一樣的  
`time.sleep()`是把整個進程終止掉，其他操作也沒辦法使用cpu，而`asyncio.sleep()`是把協程退出讓給其他操作，直到sleep時間結束  

&nbsp;

結果如下

```
this is a
text
# 停頓1秒
done
finished
```

&nbsp;

現在我們再看一個複雜點的`await`協程：

```
import asyncio

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
```

輸出結果為：

```
I will use the async function which used the async function
I used the return value of asyncfunction
I am a async function
The return value of asyncfunction is: Heisenberg
```

這裡其實可以看出，其實三個函數之間，用不用協程和`await`是沒關係的，因為它也是按流程一步一步的執行下去，真正的非阻塞請看下一節。當然，此處只是一個協程跟await的語法展示

&nbsp;

**謹記`await`必須放在協程嵌套之內（即`async def`之內）**

&nbsp;

### 4.task（任務）&future（未來允諾）及await

#### 一.await

在第二、三節，我們雖然運用了async協程，但我們做的其實只是在掛羊頭賣狗肉地的同步阻塞程式，從結果可見，我們只是等待它一步一步地完成操作  

&nbsp;

以下我們做一下真正的異步（有call back）非阻塞程式，先看第一個例子

```
import asyncio

async def foo(x):
    print(x)
    await asyncio.sleep(1)
    print('done')

async def text():
    print('this is a')

# 將await foo('text')改成如下task
# (foo('text')).add_done_callback(lambda x: print('well done'))，可以在text協程執行（run）完成後反饋（callback）一個well done

    task = asyncio.create_task(foo('text')).add_done_callback(lambda y: print('well done'))
    print('finished')

asyncio.run(text())
```

記得`asyncio.create_task`原理是被創建的那一刻，整個協程就已經被當成一個任務登記到event loop中了。輸出結果如下：

```
# 上例結果，用於對比
this is a
text
# 停頓1秒
done
finished

# 本例結果
this is a
finished
text
well done
``` 

從上面可以看出，finished被提前打印出來，原因是當協程`text`被執行（`run`）的時候，當第一行`print('this is a')`執行完畢後  
`task`被執行後的一瞬間，由於協程將資源分配回主協程`text`，所以打印finished的那一步並沒有停下來等待`task`而是接著被執行，但`task`被作為任務，則必須被執行（但不是被完成）才能結束協程`text`

&nbsp;

**所以在finished之後就會看到`text`和well done，但沒有done，因為和上例一樣沒有被`await`，只是此時`foo`被作為`task`所以會被執行，才沒有報錯**

&nbsp;

下面加上`await task`就能完整顯示`foo`的內容了

```
import asyncio

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
```

顯示結果為：

```
this is a
text
# 停頓一秒
done
finished
```

&nbsp;

再給出一個例子，證明上面的協程資源分配理論：

```
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
```

結果如下：

```
this is a
text
# 停頓1秒
finished
```

上面沒有停頓3秒也是因為當task執行之後，資源回調主協程text，所以並沒有等待task完成

&nbsp;

#### 二.await與await task之間的不同

先看第一個例子：

```
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
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = task1
    print(value)

asyncio.run(xxx())
```

結果為：

```
# 第一行僅報告task2在哪處運行，忽略
start fetching
0
```

此處因為沒有`await`兩個`task`，所以一運行`xxx`協程裡的兩個`task`就關閉了沒有給足夠的時間，下例是加上`await`：

&nbsp;

```
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
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)

asyncio.run(xxx())
```

結果為：

```
start fetching
0
1
2
3
4
5
6
7
done fetching
{'data': 1}
```

&nbsp;

這裡因為只是`await task1`，`task2`沒有被`await`，所以`task2`不夠時間打完數字8和9就被結束了，只有`task1`完成了，完整完成應如下：

```
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
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    await task2
    value = await task1
    print(value)

asyncio.run(xxx())
```

結果為：

```
start fetching
0
1
2
3
4
5
6
7
done fetching
start fetching again
done fetching again
really done fetching
8
9
{'data': 1}
```

&nbsp;

**如果把`await task1`和`await task2`換成`await fetch_data()`和`await print_numbers()`會怎樣呢，請看下面三個例子：**

&nbsp;

例子1:

```
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
    await fetch_data()
    await print_numbers()

asyncio.run(xxx())
```

結果為：

```
start fetching
done fetching
0
1
2
3
4
5
6
7
8
9
```

&nbsp;

例子2:

```
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
    task2 = asyncio.create_task(print_numbers())

    await fetch_data()
    await task2

asyncio.run(xxx())
```

結果為：

```
start fetching
0
1
2
3
4
5
6
7
done fetching
8
9
```

&nbsp;

例子3:

```
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
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    await task2
    value = await task1
    print(value)

asyncio.run(xxx())
```

結果為：

```
start fetching
0
1
2
3
4
5
6
7
done fetching
8
9
{'data': 1}
```

&nbsp;

**以上三例可以看出：**

&nbsp;

如此可以看出，當不設立task直接`await`，則只是變成了阻塞執行
這是因為，當`create_task`後，`fetch_data`整個協程將被作為一個大的`await`對象執行  
所以當task1被執行後的那一瞬間，因為`await`所以馬上交出執行權給task2執行，而之所以task1被先執行是因為`xxx()`被`asyncio.run()`當作大的協程運作，task1比task2先一步被登記在event loop上

&nbsp;

而若不`create_task`直接`await fetch_data()`，則被等待的是`fetch_data`中需要被等待的對象，即`await asyncio.sleep(2)`  
因為不是在event loop裡task與task之間對應，則只能在外面await和event loop對應，上面第二例就是這樣的狀況  
所以，`fetch_data`當執行到`await asyncio.sleep(2)`的時候，才會讓出執行權給task2執行

&nbsp;

而當`fetch_data`和`print_number`都不`create_task`，則兩個協程都只能被阻塞執行，由於`print_number`並無需要`await`的內容，所以按順序執行

&nbsp;

接著上例還有下面這種情況，很能說明主協程中的順序與event loop裡的內容之間的轉換並沒有關係

&nbsp;

正序：
```
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
```


結果為：

```
start
start fetching
0
1
2
3
4
5
6
7
done fetching
end
8
9
{'data': 1}
```

&nbsp;

兩個換位`await task`換位：

```
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

    await task2
    print('end')

    value = await task1
    print(value)

asyncio.run(xxx())
```

結果為：

```
start
start fetching
0
1
2
3
4
5
6
7
done fetching
8
9
end
{'data': 1}
```

&nbsp;

上面兩例對比之下便可以得出，因為一開始task1和task2的create_task已經把兩個task註冊在event loop內，  
所以在task與task之間，是在兩者中協程的await位置相互交出執行權，所以除去start和end的部分會發現兩個例子得到結果完全一致  
但在task與主協程之間，則內容會按主協程的順序執行，所以例一end的位置的位置是在task1結束之後；而例二end的位置則是在task2結束之後

&nbsp;

最後可以在對照一下此例，不作解釋

```
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
    value = await task1

    print('end')

    task2 = asyncio.create_task(print_numbers())
    await task2
    
    print(value)

asyncio.run(xxx())
```

結果為：

```
start
start fetching
# 停頓2秒
done fetching
end
0
1
2
3
4
5
6
7
8
9
{'data': 1}
```

&nbsp;

#### 三.callback

仔細觀察之下，會發現之前的`.add_done_callback(lambda x: print('well done'))`不見了，為什麼呢？  
因為不刪掉就報錯了，顯示不能`await`，於是下面做了個實驗：

```
import asyncio

async def foo(x):
    print(x)
    await asyncio.sleep(1)
    print('done')

async def text():
    print('this is a')
    task = asyncio.create_task(foo('text')).add_done_callback(lambda y: print('well done'))
    print('finished')
    print('really finished')
    print('really really finished')

asyncio.run(text())
```

結果如下：

```
this is a
finished
really finished
really really finished
text
# 等待一秒
well done
```

如此，發現原來`.add_done_callback`真正執行的位置，並不真正在協程`text`內執行

&nbsp;

回看之前，可以發現`asyncio.run()`包含以下三句程式

```
loop = asyncio.get_event_loop() # 創建事件循環（即線程任務列表，event loop）

loop.run_until_complete() # 執行該協程

loop.close() # 關閉事件循環（畢竟任務執行完畢，任務列表就沒必要存在）
```

&nbsp;

**其中`loop.run_until_complete()`本身就包含了一個`task`的`add_done_callback` ，畢竟有callback才能稱為真正的異步，所以在語法中.`add_done_callback`需要跟在`task`或者`create_task()`後面，但不能在任何一個協程內被`await` ，畢竟它實際執行的時候是在`asyncio.run()` 裡面**

&nbsp;

正確在有`await`的情況下使用`.add_done_callback`的方式如下

```
import asyncio

async def foo(x):
    print(x)
    await asyncio.sleep(1)
    print('done')

async def text():
    print('this is a')
    task = asyncio.create_task(foo('text'))
    await task
    task.add_done_callback(lambda x: print('well done'))
    print('finished')

asyncio.run(text())
```

&nbsp;

#### 四.future

其實future就相當於一個空殼的task，future也是task的父類，task繼承自task，  
如下，則會完全空白執行且不會終止，因為await它但沒有返回任何值

```
async def main1():
    loop = asyncio.get_running_loop()

    fut = loop.create_future()

    await fut

asyncio.run(main1())
```

想要future有值則只能自己給予

```
import asyncio

async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('say my name')

async def main1():
    loop = asyncio.get_running_loop()

    fut = loop.create_future()

    await asyncio.create_task(set_after(fut))

    data = await fut
    print(data)

asyncio.run(main1())
```

結果為：

```
# 等待兩秒
say my name
```

#### 五.ensure_future

如果想多個任務在完成後都能傳會callback，我們應該這麼做：

```
import asyncio

async def cron_job(url):
    await asyncio.sleep(2)
    print(f'get {url} done in 2 seconds')


async def cron_scheduler():
    future_list = []
    page = 10
    while page >= 0:
        url = f'http://www.last{page}daysoftheworld.com/{page}day.html'
        future = asyncio.ensure_future(cron_job(url))
        future_list.append(future)
        page -= 1
        future.add_done_callback(lambda future: print('goodbye, cruel world'))
    
    await asyncio.gather(*future_list)


asyncio.run(cron_scheduler())
```

只有使用`ensure_future`才能得到每個任務的callback，因為future和task不同的地方在於  
task只會把任務掛到event loop上，不能得到return結果，如果強行要結果或者知道結束，只能是`add_done_back`在整個event loop結束之後才能獲得
而future則是保證return會被返回，所以future的return是分離的（即非阻塞的），因此能在event loop運行中返回

&nbsp;

另外，`ensure_future`不一定要是協程，函數也可以，所以，如果讓task等待（await）future的話，就會造成阻塞

&nbsp;

為了證明，加上計時就知道了

```
import asyncio
import time

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
asyncio.run(cron_scheduler())
end = time.time()
print(f'{end - start} seconds')
```

結果為：

```
get http://www.last10daysoftheworld.com/10day.html done in 2 seconds
get http://www.last9daysoftheworld.com/9day.html done in 2 seconds
get http://www.last8daysoftheworld.com/8day.html done in 2 seconds
get http://www.last7daysoftheworld.com/7day.html done in 2 seconds
get http://www.last6daysoftheworld.com/6day.html done in 2 seconds
get http://www.last5daysoftheworld.com/5day.html done in 2 seconds
get http://www.last4daysoftheworld.com/4day.html done in 2 seconds
get http://www.last3daysoftheworld.com/3day.html done in 2 seconds
get http://www.last2daysoftheworld.com/2day.html done in 2 seconds
get http://www.last1daysoftheworld.com/1day.html done in 2 seconds
get http://www.last0daysoftheworld.com/0day.html done in 2 seconds
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
goodbye, cruel world
2.0025508403778076 seconds
2.0035409927368164 seconds
```

&nbsp;

#### 六.可await對象

可await的對象只有三種，分別是協程對象（即`協程名()`）、task和future

&nbsp;

注意，例如`asyncio.sleep()`亦是一種協程對象，因`.sleep()`也是一個函數，詳看22課

&nbsp;

### 5.with...as（上下文管理器）

當asyncio引用其他庫或函數變量、類後序的時候，就需要運用with...as，先看下例：

```
from timeit import default_timer
import asyncio
import aiohttp

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp: # 此處，resp等於session.get(url)
        text = await resp.text() # 這裡即等於awiat session.get(url).text()
        print(f'Completed {delay} second timer')
        return text

async def main():
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

asyncio.run(main())
```

輸出結果為：

```
Starting 2 second timer
Starting 3 second timer
Doing other work
Completed 2 second timer
Completed 3 second timer
The operation took 3.8 seconds
```

從上例註解便可看出，with...as是一種簡化的手法，with後面的內容便等於as，with後面一切的內容，均可採用任何後序/協程變量等

&nbsp;

### 6.gather(收集)與wait（整合）

#### 一.gather與wait的區別

`gather`相當於把多個協程登記到event loop裡面並自動生成task運行，之後收集執行  
而`wait`則等於把多個協程的列表打包成一個event loop，之後執行

```
import asyncio

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
    # await asyncio.gather(taskA, taskB)

asyncio.run(gatherwait())
```

&nbsp;

#### 二.wait用法技巧介紹

首先，`asyncio.wait()`的對象必須是列表，否則無效

&nbsp;

1.你可以設定裡面的等待時間，如下（以上例作對照）：

```
import asyncio

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
```

由於得不到充分的等待時間，所以結果如下

```
start
func1
func2
finish
```

&nbsp;

2.設立done可以看得到協程基本信息反饋：

```
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
```

其中，`done`的意思是完成的任務列表信息，所以結果如下，注意最後一段就是done反饋的東西，結果為：

```
start
func1
func2
func1 end
func2 end
({<Task finished name='Task-3' coro=<func2() done, defined at /Users/heisenberg/empire/Vscode/lab/text.py:8> result='func2 finish'>, <Task finished name='Task-2' coro=<func1() done, defined at /Users/heisenberg/empire/Vscode/lab/text.py:3> result=None>}, set())
finish
```

&nbsp;

3.pending則能在設定特定的錯誤條件下得到信息反饋，由於其特殊性它常與done一起運用，如下：

```
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
```

結果為：

```
start
func1
func2
set()
{<Task pending name='Task-3' coro=<func2() running at /Users/heisenberg/empire/Vscode/lab/text.py:10> wait_for=<Future pending cb=[Task.task_wakeup()]>>, <Task pending name='Task-2' coro=<func1() running at /Users/heisenberg/empire/Vscode/lab/text.py:5> wait_for=<Future pending cb=[Task.task_wakeup()]>>}
finish
```

&nbsp;

**上面wait_for=< Future pending cb=[Task.task_wakeup()] >>就是pending出來的東西**

&nbsp;

4.在`create.task`中可以對task進行命名，這樣就能讓task的自定義名出現在done輸出中，並且done也會輸出return內容，如下：

```
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
```

結果為：

```
start
func1
func2
func1 end
func2 end
{<Task finished name='func2' coro=<func2() done, defined at /Users/heisenberg/empire/Vscode/lab/text.py:8> result='func2 return'>, <Task finished name='func1' coro=<func1() done, defined at /Users/heisenberg/empire/Vscode/lab/text.py:3> result=None>} set()
finish
```

注意如果timeout等候不足，會令到result顯示None

&nbsp;

5.結合`asyncio.run`應用

&nbsp;

其實就是把整個`asyncio.wait()`在`loop = asyncio.get_running_loop()`創建之後登記進去

```
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

task_list1 = [func1(),func2()]

done, pending = asyncio.run(asyncio.wait(task_list1))
print(done)
```

結果為：

```
func1
func2
func1 end
func2 end
{<Task finished name='Task-3' coro=<func2() done, defined at /Users/heisenberg/empire/Vscode/lab/text.py:8> result='func2 return'>, <Task finished name='Task-2' coro=<func1() done, defined at /Users/heisenberg/empire/Vscode/lab/text.py:3> result=None>}
```

但不是很標準的用法，雖然也能出結果和完成反饋。一般不推薦

&nbsp;

#### 三.gather詳解

第五節例子亦可以簡化成這樣：

```
from timeit import default_timer
import asyncio
import aiohttp

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp: # 此處，resp等於session.get(url)
        text = await resp.text() # 這裡即等於awiat session.get(url).text()
        print(f'Completed {delay} second timer')
        return text

# 這裡必須要把原來在elapsedtime()中的sleep抽出來
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

        # 這裡當task執行後，text進入等候，然後下面便要等候sleep結束，print出doing other work
        # await asyncio.sleep(1)
        # print('Doing other work')

        # 之後就等待兩個task結束才能進行下一步，而task裡就進行到text，當中就有delay停頓，兩個task重疊便停頓3秒
        # two_result = await two_task
        # three_result = await three_task

        # 這裡就是等待三個task結束，並且把三個task的結果gather起來，並且把結果傳回result
        # 並且不用create_task()因為gather()已經把task自動放入event_loop裡了
        result = await asyncio.gather(one_task, two_task, three_task)

        # 接著兩個task返回text值，寫在了Completed {delay} second timer裡，接著兩個task結束，print出總用時值（即elapsed time）
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(elapsedtime())
```

注意必須將原來在`elapsedtime()`中的`await asyncio.sleep(1)`抽出來，變成一個獨立的協程  
這樣才能打包成一個task放入`gather`裡與其他兩個task一起執行，不然就不能以預設的順序執行  
因為在`gather`是一個小的event loop，只是會收集括號裡的結果，而外面是一個大的event loop，當中包含了`gather`
所以`gather`就會按外面大的event loop的順序執行，當執行到`gather`才會出現括號內的內容（如果有`print`）  

&nbsp;

`gather()`為收集執行的意思，若有多個task需要等待（`await`）結果，則可直接採用`await gather()`簡化，且無需`create_task`，因為`gather()`已經把task自動放入event_loop裡了

&nbsp;

還可以以字典方式繼續簡化成這樣：

```
from timeit import default_timer
import asyncio
import aiohttp

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
```

如此，當若有大量task的時候，就可以直接用字典簡化收集

&nbsp;

在下面，我們應用低層級loop多做一個版本，讓我們更好理解下一節內容

```
from timeit import default_timer
import asyncio
import aiohttp

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

loop = asyncio.get_event_loop()
loop.run_until_complete(elapsedtime())
```

結果為：

```
DeprecationWarning: There is no current event loop
  loop = asyncio.get_event_loop()
Starting 2 second timer
Starting 3 second timer
Doing other work
Completed 2 second timer
Completed 3 second timer
The operation took 3.9 seconds
```

&nbsp;

這裡報錯，是因為在3.10 版後已棄用`get_event_loop()`，如果没有正在运行的事件循环则会发出弃用警告  
在未来的 Python 发行版中，此函数将成为`get_running_loop()`的别名。現在只能在主線程協程函數中才不會報錯  
即意思已改變為增設一個新的event loop，包含在主event loop中，即表示其需與特殊loop後續配合使用，例如`run_in_executor`、`run_forever`等

&nbsp;

### 7.run_in_executor(分解執行)

通常，協程只適合做IO密集型工作，不適合做計算密集型工作，因為IO密集型工作只需設定處理輸出之後，CPU便不用參與；但計算密集型工作則需要CPU一直參與

&nbsp:

下面是一段類菲波那契計算代碼例子：

```
import time
def fib(n):
    if n in [1,2]:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()
print(fib(38))
end = time.time()

print(end-start)
```

用時是5.233759880065918，如果加上一段sleep做異步的話：

```
import time
import asyncio

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
```

結果如下：

```
63245986
10.203260898590088
```

可以看出，其效果僅僅等於串行執行（從先print出結果可知），甚至有些條件下，這樣強行做異步的效果比串行還要差，因為在計算密集型代碼中，cpu需要一直參與

&nbsp:

但若是非要進行一些大運算量的代碼，例如遞歸類，則`run_in_executor`可以幫助其代碼以非阻塞方式執行  
其原理是將一個大運算量代碼，每一個運算步驟分解出來，使cpu可以在每一步運算結束的時候得到短暫的結束，從而執行一下其他任務，再繼續執行
這裡需要用到之前提過的`get_runing_loop`(`get_event_loop`已經改變成這個)

&nbsp:

以下是一個分解執行例子：

```
import time
import asyncio

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
    loop = asyncio.get_runing_loop() #創建一個event loop任務例表
    # 下面是將calc_fib包裝成一個任務並分解執行，注意executor不接受關鍵字參數，只接受位置参数，第一位是用於執行的模塊功能，第二位是函數名，第三位是參數
    # 便要使用None佔位，因為沒有用於執行的模塊功能，只是為了讓executor執行，若有，則需要用with...as...來包裝成一個executor傳入None位
    task3 = loop.run_in_executor(None, calc_fib, 38)
    task4 = request()
    await asyncio.gather(task3,task4)
    end = time.time()
    print(end-start)

asyncio.run(needtime())
```

執行結果為：8.804831981658936秒，可見比之前快了約兩秒

&nbsp:

注意，如果函數有大量的參數位，若不全部填寫令某些參數出現空位，當運用`run_in_executor`執行則會導致錯誤，而大量使用None佔位不僅麻煩且易出錯  
此時，我們可以參照以下代碼片段方法，將`run_in_executor`包裝成另一個協程，如此則可以使用簡單的關鍵字參數，另代碼更方便編寫少出錯

```
async def simple_run_in_executor(f, *args, async_loop=None, **kwargs):
    loopx = async_loop or asyncio.get_runing_loop()
    result = await loopx.run_in_executor(async_executor, partial(f, *args, **kwargs))
    return result
```

注意以上只是用於示例的代碼片段，不可執行

&nbsp:

除了計算密集型之外，`run_in_executor`亦可以將一個非協程包裝成協程，這樣便於與其他語言的模塊相結合，若該語言沒有異步功能

```
import time
import asyncio
import concurrent.futures

def func1():
    print('func1 start')
    time.sleep(2)
    print('func1 end')

async def main():
    loop = asyncio.get_running_loop()

    # fut = loop.run_in_executor(None, func1)
    # result = await fut
    # print('default thread pool', result)

    with concurrent.futures.ThreadPoolExecutor() as pool: # 加入線程池
        fut = loop.run_in_executor(pool, func1)
        result = await fut
        print('thread pool', result)

    # with concurrent.futures.ProcessPoolExecutor() as pool: # 加入進程池
    #     fut = loop.run_in_executor(pool, func1)
    #     result = await fut
    #     print('process pool', result)

asyncio.run(main())
```

結果為：

```
func1 start
func1 end
thread pool None
```

&nbsp:

再多給一個非異步轉異步的爬蟲例子(也是第一節例子）：

```
import requests
import time
import asyncio

url = 'https://www.google.com.tw/'
loop = asyncio.get_event_loop()

start_time = time.time()

async def send_req(url):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    res = await loop.run_in_executor(None,requests.get,url) # request.get不可以稱為協程，所以要用run_in_executor將它定義為協程

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

tasks = []

for i in range(10):
    task = loop.create_task(send_req(url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
```

&nbsp:

### 8.Semaphore(信號量限制)

假设如果我们同时发起10个请求，每个请求的时间不同，那么总共的请求时间大概跟最长耗时的请求差不多。我们先来写一个用于测试的例子：

```
import asyncio
import aiohttp
import time

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
```

結果為：

```
waiting for semaphore with 3 seconds delay
waiting for semaphore with 2 seconds delay
waiting for semaphore with 8 seconds delay
waiting for semaphore with 4 seconds delay
waiting for semaphore with 1 seconds delay
waiting for semaphore with 5 seconds delay
waiting for semaphore with 7 seconds delay
waiting for semaphore with 6 seconds delay
waiting for semaphore with 9 seconds delay
waiting for semaphore with 10 seconds delay
waiting for semaphore with 3 seconds delay
waiting for semaphore with 6 seconds delay
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
cost 10.469586849212646 seconds # 接近十秒，正常結果
```

&nbsp:

现在的问题是，由于网站有反爬虫机制，最多只能同时发起3个请求。那么我们怎么确保同一时间最多只有3个协程在请求网络呢？  
asyncio 实际上自带了一个限制协程数量的类，叫做`Semaphore`。我们只需要初始化它，传入最大允许的协程数量，然后就可以通过上下文管理器来使用。我们看一下代码：

```
import asyncio
import aiohttp
import time

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
```

結果為：

```
waiting for semaphore with 3 seconds delay
waiting for semaphore with 2 seconds delay
waiting for semaphore with 8 seconds delay
waiting for semaphore with 4 seconds delay
waiting for semaphore with 1 seconds delay
waiting for semaphore with 5 seconds delay
waiting for semaphore with 7 seconds delay
waiting for semaphore with 6 seconds delay
waiting for semaphore with 9 seconds delay
waiting for semaphore with 10 seconds delay
waiting for semaphore with 3 seconds delay
waiting for semaphore with 6 seconds delay
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
got response 200
cost 25.424988269805908 seconds # 比同步或者只是三個三個加起來快多了
```

&nbsp:

我们来看看`Semaphore`的用法，它的格式为：
```
sem = asyncio.Semaphore(同时运行的协程数量)

async def func(sem):
    async with sem:
        这里是并发执行的代码

task_list = []
for _ in range(总共需要执行的任务数):
    task = asyncio.create_task(func(sem))
    task_list.append(task)
await asyncio.gather(*task_list)
```

&nbsp:

当我们要限制一个协程的并发数的时候，可以在`调用协程之前`，先初始化一个`Semaphore`对象。然后把这个对象传到需要限制并发的协程里面，在协程里面，使用异步上下文管理器包住你的正式代码：

```
async with sem:
    正式代码
```

&nbsp:

这样一来，如果并发数没有达到限制，那么`async with sem`会瞬间执行完成，进入里面的正式代码中。如果并发数已经达到了限制，那么其他的协程会阻塞在`async with sem`这个地方，直到正在运行的某个协程完成了，退出了，才会放行一个新的协程去替换掉这个已经完成的协程。

&nbsp:

这个写法其实跟多進程的加锁很像。只不过锁是确保同一个时间只有一个线程在运行，而`Semaphore`可以人为指定能有多少个协程同时运行。  
(可以去了解`multiprocessing`多進程處理庫)

&nbsp:

另外，可以加上sleep來限制一段時長內的協程數：

```
async def req(delay,sem):
    print(f'waiting for semaphore with {delay} seconds delay')
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://www.google.com.tw') as resp:
                print(f'got response {resp.status}')
                await asyncio.sleep(delay)
    await asyncio.sleep(60)
```

最後加上這段`await asyncio.sleep(60)`便可以控制一分鐘內協程只有3個

&nbsp:

### 9.asyncio在class中的用法

其實與平常使用無異，只需在class裡的函數中加上async變成協程，以及使用協程後序時使用`asyncio.run()`即可

```
import asyncio
import aiohttp

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
```

以上例子可作參考

&nbsp:

### 10.異步請求連續編號頁面的方法（range task list）

下面是異步請求連續編號頁面的代碼編寫方向，只要稍作修改便可實驗，僅供參考：

```
import asyncio

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
```

只需修改`cronjob`和修改`while loop`部分代碼即可實現，當然，此例代碼由於加入了遞增量的sleep，看起來只會像阻塞代碼

&nbsp:

### 11.異步IO操作管理器

這是一個應用範例，可以對文件自動進行打開、操作、關閉的動作，供參考

```
import asyncio

class AsyncContextManager:
    def __init__(self):
        self.conn = 'conn'
    
    async def do_something(self):
        # 異步操作數據庫
        return 'Heisenberg'
    
    async def __aenter__(self):
        # 異步鏈接數據庫
        self.conn = await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        # 異步關閉數據庫
        await asyncio.sleep(1)
    
async def func():
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)

asyncio.run(func())
```

&nbsp:

### 12.uvloop

uvloop是一個由Cython编写、建立在libuv之上的異步IO框架，亦是現時效率最快的異步IO框架，用於替代asyncio裡的默認event loop以提高效率  

&nbsp:

使用方法非常簡單：

```
import asyncio
import uvloop

# 方法一:設定event loop權限獲取方為uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# 方法二：uvloop直接設定（兩種方法一樣效果，未來方法二可能取代方法一）
uvloop.install()
```

&nbsp:

一開始設定好這些然後正常使用asyncio語法即可

&nbsp:

注意uvloop在win不能使用，用的是另一套叫IOCP的，設定方法如下：

```
import sys, asyncio, uvloop

if sys.platform == 'win32': #支持windows

if sys.version_info.major >=3 and sys.version_info.minor >= 7:

asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

else:

asyncio.set_event_loop(asyncio.ProactorEventLoop())
```