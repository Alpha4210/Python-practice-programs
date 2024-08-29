#Check if a number is an armstrong number - the numner is equal to the sum of the digits of the number raised to the power of the number of digits of the number.

while True:
    x = 0
    print("enter q to exit")
    num = input("Enter the number to check if it is an armstrong number ")
    if num=="q":
        exit()
    else:
        # Used to get the number of digits
        count=0
        for i in num:
            count+=1
            
        # Used to calculate the number
        for i in num:
            i = int(i)
            x+=i**count
            print(x)
        
        # Checking if its armstrong number
        if x==int(num):
            print(f"{num} is an armstrong number")
        else:
            print("It is not a armstrong number")
            continue