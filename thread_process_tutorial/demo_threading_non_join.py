import threading
import time

def main(num):
    print('開始執行', num)
    time.sleep(2)
    print('結束', num)

t_list = []

t1 = threading.Thread(target=main, args=(1,))
t_list.append(t1)
t2 = threading.Thread(target=main, args=(2,))
t_list.append(t2)
t3 = threading.Thread(target=main, args=(3,))
t_list.append(t3)

for t in t_list:
    t.start()

print('main thread quit')

"""
開始執行 1
開始執行 2
開始執行 3
main thread quit
結束 3
結束 1
結束 2
"""