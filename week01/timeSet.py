from datetime import *
import time
#===use time
print(time.time())#基本不用

print(time.localtime())#strcut_time

#对struct_time进行格式化 strftime
print(time.strftime("%Y-%m-%d %X",time.localtime()))

#将格式化的时间重新转为struct_time
print(time.strptime("2020-12-27 11:48:39","%Y-%m-%d %X"))

#===use datetime
print(datetime.today(),datetime.now())
print(datetime.today()+timedelta(days=1))#对时间加减等操作



