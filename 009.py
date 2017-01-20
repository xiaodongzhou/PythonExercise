import time

one_line = raw_input("please input a line.  You can see it after 3 seconds. ")
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
time.sleep(3)
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print one_line