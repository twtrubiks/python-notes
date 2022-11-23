import multiprocessing as mp
import time


def main(url, num):
    print('開始執行', url)
    time.sleep(2)
    print('結束', num)


url_list1 = ['www.yahoo.com.tw, www.google.com']
url_list2 = ['www.yahoo.com.tw, www.google.com']
url_list3 = ['www.yahoo.com.tw, www.google.com']

# 定義線程
p_list = []
p1 = mp.Process(target=main, args=(url_list1, 1))
p_list.append(p1)

p2 = mp.Process(target=main, args=(url_list2, 2))
p_list.append(p2)

p3 = mp.Process(target=main, args=(url_list3, 3))
p_list.append(p3)

# 開始工作
for p in p_list:
    p.start()

print('main process quit')