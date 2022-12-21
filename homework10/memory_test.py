import random
import hashlib
import time
import os

def count(num):
    for i in range(num,0,-1):
        print("\r{} seconds left！".format(i),end="")
        time.sleep(1)
    print("\rtime up！")

if __name__ == "__main__":
    num = 10
    number = random.randint(100000000, 1000000000)
    hash_value = hashlib.sha256(str(number).encode()).hexdigest()
    print("Please memorize the number within {} seconds:".format(num), number)
    count(num)
    os.system('cls')
    answer = input("What was the number? ")
    hash_answer = hashlib.sha256(str(answer).encode()).hexdigest()
    if hash_answer == hash_value:
        print("Correct!")
    else:
        print("Incorrect. The correct answer was", number)
