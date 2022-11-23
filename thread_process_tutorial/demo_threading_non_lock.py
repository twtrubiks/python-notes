import threading

a = 0

def thread_first_job():
    global a
    for _ in range(3):
        a += 1
        print("This is the first thread ", a)


def thread_second_job():
    global a
    for _ in range(3):
        a -= 1
        print("This is the second thread ", a)


first_thread = threading.Thread(target = thread_first_job)
second_thread = threading.Thread(target = thread_second_job)
first_thread.start()
second_thread.start()
first_thread.join()
second_thread.join()