import time
from concurrent.futures import ThreadPoolExecutor

class A:
    def __init__(self):
        self.value = 0

    def update(self):
        print("Update Started")
        time.sleep(2)
        tmp = self.value + 1
        print("Updating Value")
        self.value = tmp
        print("Updating Finished")

for i in range(10):
    # 如果輸出 1 , 就是 RaceConditions
    db = A()
    with ThreadPoolExecutor(max_workers=5) as executor:
        updates = [executor.submit(db.update) for _ in range(2)]

    if db.value != 2:
        print('Race Conditions')

    print(db.value)