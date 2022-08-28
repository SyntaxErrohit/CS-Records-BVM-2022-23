from math import pi
from random import randint

def sintaylor():
    n = int(input("Enter the value of n in degrees: "))
    x = (pi/180)*n
    summ = 0
    sign = 1
    for i in range(1, n+1, 2): 
        f = 1
        for j in range(i):
            f *= j+1
        summ += ((x**i)/f)*sign
        sign *= -1
    print("The result of the series =", summ)

def dice():
    ch = int(input("Enter 0 to main menu or 1 to roll the dice: "))
    while ch == 1:
        print("The number for you is...")
        print(randint(1, 6))
        ch = int(input("Enter 0 to main menu or 1 roll the dice: "))

while True:
    print("Main menu\n1. Sin Series - Taylor's series")
    print("2. Simulate a dice\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sintaylor()
    if choice == 2:
        dice()
    if choice == 3:
        break
