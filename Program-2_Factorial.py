# Part1 - Calculate the factorial of a given number
# Part2 - Find the number of trailing zeroes in that factorial

# Part - 1 code starts
def fact(n):
    sum=1
    for i in range(1, n+1):
        sum*=i
    return sum

# num = int(input("Enter the number whose factorial you want: "))
# print(fact(num))
# Part - 1 code ends

def trail_zeroes(n):
    sum=1
    for i in range(1, n+1):
        sum*=i
    s = str(sum)
    a=s[::-1]
    count=0
    for i in a:
        if i!='0':
            break
        count+=1
    return count
    
num = int(input("Enter the number whose factorial you want: "))
print(trail_zeroes(num))
