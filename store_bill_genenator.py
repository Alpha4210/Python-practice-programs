#You are a shop owner, user will keep on entering price of item and keep on entering the items and stop when the user enters q.

print("This program will help you to generate your store bill")
sum = 0
while True:
    price = input("Enter the price: ")
    if price.isdigit():
        intprice = int(price)
        sum+=intprice
    elif price=='q':
        break
    else:
        print("Please enter a valid value")
print(f"Total price: {sum}")