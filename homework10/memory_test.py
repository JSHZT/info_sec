import random
import hashlib
import time
import os

def count(num):
    for i in range(num,0,-1):
        print("\r{} seconds left！".format(i),end="")
        time.sleep(1)
    print("\rtime up！")


