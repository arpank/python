import concurrent.futures
import random
import threading
import time
import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age






executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

def func(x):
    time.sleep(random.random())
    print (x)
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12),  # year, month, day
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com"
    )
    print(threading.current_thread().name)
    return 2000+x

def callback(future):
    time.sleep(random.random())
    x = future.result()
    cur_thread = threading.current_thread().name
    if (cur_thread != x):
        print(cur_thread, x)

print('main thread: %s' % threading.current_thread())
temp=0
for i in range(3):
    future = executor.submit(func, i)
    future.add_done_callback(callback)
    try:
        data = future.result()
        temp = temp + data
    except Exception as exc:
        print('error')
    else:
        print('good')


print (temp)
