import os
import threading
import time


commands_list = ['systeminfo', 'ipconfig','whoami','ping www.ynet.co.il']

def run_command(cmd):
    print( os.popen(cmd).read())


start = time.perf_counter()

for command in commands_list:
    th1 = threading.Thread(target=run_command, args=(command,))
    th1.start()



print("Total Time : ", time.perf_counter()-start)






