import threading
import time

def main():
    while 1:
        print('執行中...')
        time.sleep(1)

print("non-daemon Thread")
t1 = threading.Thread(target=main)
t1.start()
print("isDaemon:", t1.isDaemon())

time.sleep(5)
print('main thread quit')
