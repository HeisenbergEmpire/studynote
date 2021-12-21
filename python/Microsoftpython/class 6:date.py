# 為了獲取當前日期時間，需要先從datetime庫導入datetime及timedelta函數（datetime模塊及庫包屬於python標準庫裡的代碼模塊，不需下載第三方庫）
from datetime import datetime,timedelta
# 以變量詞來代表現時datetime，記得後面要有空格
current_date = datetime.now()
# 輸出日期時間
print('today is:' + str(current_date))
print()
# 之前的timedelta函數將用於下列代碼
today = datetime.now()
print('Today is:' + str(today))
# 以下代碼將顯示出相差日子，timedelta為一個時間差的量，days=1為一天，weeks=1為一週，hours為一小時
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
one_hour = timedelta(hours=1)
yesterday = today - one_day
lastweek = today - one_week
nexthour = today - one_hour
print('Yesterday was:' + str(yesterday))
print('Lastweek was:' + str(lastweek))
print('Nexthour is:' + str(nexthour))
print()
# 若只想顯示現時時間的年/月/日/時/分/秒數而非完整時間，可以用以下方法（上接第一部分第一二行代碼）
print('Day:' + str(current_date.day))
print('Month:' + str(current_date.month))
print('Year:' + str(current_date.year))
print('Hour:' + str(current_date.hour))
print('Minute:' + str(current_date.minute))
print('Second:' + str(current_date.second))
print()
# 補充用法，可以在datetime.now()後面加年月日時分秒，直接顯示出當前時間
today1 = datetime.now().year
print('Now:' + str(today1))
# strptime可以將輸入符合預設格式的年月日數字變成日期，注意%Y代表4位年數，小寫y代表兩位年數，上接第一行代碼
birthday = input('When is your bitthday(dd/mm/yyyy)')
birthday_date = datetime.strptime(birthday,'%d/%m/%Y')
print('Birthday:' + str(birthday_date))
#下面就可以聯合timedelta一起使用，上接one_day那一行代碼
birthday_eve = birthday_date - one_day
print('Day brfore birthday:' + str(birthday_eve))
print()
# 以下是這課的作業，在此發現新版本中，日期輸入再不用受文字或數字類型影響
today2 = datetime.now()
print(today2.day)
print()
# print yesterday's date
today_date = datetime.now()
one_day = timedelta(days=1)
yesterday_date = today_date - one_day
print(yesterday_date.day)
print()
# ask a user to enter a date
date = input('what is the date you want? :(dd/mm/yyyy)')
date = datetime.strptime(date, '%d/%m/%Y')
# print the date one week from the date entered
one_week = timedelta(weeks=1)
one_week_later = date + one_week
print(one_week_later.day)