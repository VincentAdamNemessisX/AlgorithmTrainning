import os
import datetime

current_dir = os.getcwd()
now_time = datetime.datetime.now()
for i in range(1,20):
    os.makedirs(current_dir + f'/{now_time.year}-{now_time.month}-{now_time.day + i}',
                exist_ok=True)
