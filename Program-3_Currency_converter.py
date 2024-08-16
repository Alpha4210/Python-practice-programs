#Currency converter - Rupees to any other currency

# with open("currencyData.txt") as f:
#     inr_amt = int(input("Enter the amount in rupees: "))
#     ask_curr = input("In which currency do you want to convert: ")
#     conv_amt=0
#     l1 = f.readlines()
#     for i in l1:
#         x = i.split('\t')
#         if i==x[0]:
#             conv_amt=int(x[1])*inr_amt
#             print(f"{inr_amt}rupees in {ask_curr} = {conv_amt}")
#         else:
#             continue
    
with open('currencyData.txt') as f:
	lines = f.readlines()

currencyDict = {}
for line in lines:
	parsed = line.split("\t")
	currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:\n"))
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")