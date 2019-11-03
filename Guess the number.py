import random

a = random.randint(1,50)
print("Guess the number between 1 and 50")


while True:
    n = int(input())
    diff = a - n
    if (a > n):
        if(diff < 10):
            print("Actual number is little high")
        else:
            print("Actual number is too high")
    elif (a < n):
        if(diff > -10):
            print("Actual number is little low")
        else:
            print("Actual number is too low")
    else:
        print("Correct number")
        exit()
    print("Guess the same number:")