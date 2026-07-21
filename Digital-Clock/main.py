import time
import os

while True:
    os.system("clear")
    print(f"Current Date : {time.strftime('%d %B %Y')}")
    print(f"Current Time : {time.strftime('%H:%M:%S')}")
    time.sleep(1)