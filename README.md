# RainbowText
Hello World, This is a simple python program that used to make the text to blink on several colors. You can impress your friends by running this program on your computer or your school lab's computer.

## System Requirements
```bash
python3
windows Operating System
```
## Script Here
```bash
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
    
```

# Note
Run this code in CMD, And this code runs infinitely so kindly close the CMD window when you finished!

### KeyWords (Just Ignore This)
CMD TRICKS
rainbow tricks
rainbow text
colorful text animation in python
cmd color changing code
bash tricks
impress your friends
school fun
