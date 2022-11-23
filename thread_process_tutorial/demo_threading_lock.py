import threading

def thread_first_job():
    global a, lock
    lock.acquire()

    for _ in range(3):
        a += 1
        print("This is the first thread ", a)

    lock.release()


def thread_second_job():
    global a, lock
    lock.acquire()

    for _ in range(3):
        a -= 1
        print("This is the second thread ", a)

    lock.release()

a = 0
lock = threading.Lock()
first_thread = threading.Thread(target = thread_first_job)
second_thread = threading.Thread(target = thread_second_job)
first_thread.start()
second_thread.start()
first_thread.join()
second_thread.join()