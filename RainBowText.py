import os
import time

i = 1
os.system('cls')
text = input("Enter a text:")

os.system('cls')

for j in range(10):
    print(text)

while i<=10:
    os.system('color 0D')
    time.sleep(0.3)
    os.system('color 03')
    time.sleep(0.3)
    os.system('color 0E')
    time.sleep(0.3)
    os.system('color 0A')
    time.sleep(0.3)
    os.system('color 08')
    time.sleep(0.3)
    os.system('color 09')
    time.sleep(0.3)
    os.system('color 04')
    time.sleep(0.3)
