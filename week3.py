#Amount after discount calculation
#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
amount=int(input("Enter sale price: "))
#calculating discount based on sales
if(amount>0):
    if amount>=10000:
        dis=20
    elif(amount<=9999):
        dis=0
#finding discounted amount
    dis=(0.2* amount)

    print("discount : ", dis)
    print("Net Pay : ", amount-dis)
else:
    print("Invalid amount")
