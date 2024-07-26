# Find Gross Pay - Prompt User To Enter The Price/Ltr, and Then Prompt Them To Enter Total Litres. Finally Print The Total Amount

price = float(input("Enter The Price of Disel/Litre in ₹"))
quantity = float(input("Enter The Amount Consumed"))

print(f"The Total Price is ₹ {price*quantity}")