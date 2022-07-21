
while True:
    Num = int(input("please Enter your positive Number: "))
    M = 0
    for i in range(1, Num):
        if Num % i == 0:
            M += i
    if M == Num:
        print(f"yes :{Num} is a perfect number")
    else:
        print(f"No: {Num} is not a perfect number")

