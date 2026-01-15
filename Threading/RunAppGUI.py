import os
import time

commands_list = ['whoami', 'ipconfig','systeminfo','ping www.ynet.co.il']

start = time.perf_counter()

for command in commands_list:
    print(os.popen(command).read())

print("Total Time : ", time.perf_counter()-start)






