import random


while True:
    print(random.randint(1,6))
    print("Would you like to roll dice again: ")
    n = input() 
    if (n in ('Y','y')):
        continue
    elif (n in ('N','n')):
        exit()
    else:
        print("Invalid option. Please enter y or n")


