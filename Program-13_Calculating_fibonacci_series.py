n = int(input("Enter the number of terms you want: "))
if n == 0:
    print(0)
elif n == 1:
    print(1)
else: 
    prev = 0
    nextt = 1
    for i in range(1,n):
        sum1 = prev+nextt
        prev=nextt
        nextt=sum1
    print(sum1)
