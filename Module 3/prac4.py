print("Price List")
print("MINI BURGER - ₹99")
print("NORMAL BURGER - ₹129")
print("LARGE BURGER  - ₹149")

order_size=input("Enter M/N/L for your order")

price=0

if order_size == 'M' or order_size =='m':
    print("Order Size Mini Confirmed ")
    price+=99
    
elif order_size == 'N' or order_size =='n':
    print("Order Size Normal Confirmed ")
    price+=129
    
elif order_size == 'L' or order_size =='l':
    print("Order Size Large Confirmed ")
    price+=149
    
else:
    print("Invalid Order Size")
    exit(0)

add_mushroom = input("Want To Add Mushroom Y/N ? ₹10 For M , ₹15 for N/L ")

if add_mushroom=='Y' or add_mushroom=='y':
    if order_size == 'M' or order_size =='m':
        print("Added Mushroom ₹10 ")
        price+=10
        
    elif order_size == 'N' or order_size =='n' or order_size == 'L' or order_size =='l' :
        print("Added Mushroom ₹15 ")
        price+=15
    else:
        print("Invalid Choice")
        exit(0)
    
elif add_mushroom =='N' or add_mushroom =='n':
        price+=0
        
else:
    print("Invalid Input")
    exit(0)

extra_cheese = input("Want Extra Cheese Y/N ? ₹25 "  )    
    


if extra_cheese=='Y' or extra_cheese=='y':
    print("Added Cheese ₹15 ")
    price+=25
elif extra_cheese!='N' or extra_cheese!='n':
    exit(0)    
        


print(f"Please Pay ₹{price} at the counter")

