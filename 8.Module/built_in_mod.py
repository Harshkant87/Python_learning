# 1. time module
import time

i = 0
while True:
    print(i)
    i = i + 1
    time.sleep(3)

    if i == 2:
        break

