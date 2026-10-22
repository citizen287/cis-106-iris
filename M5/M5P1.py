QuantityOfItems = input("Enter the quantity of items: ")
if int(QuantityOfItems) >= 1000:
    UnitPrice = 3.00
else:
    UnitPrice = 5.00
ExtendedPrice = int(QuantityOfItems) * UnitPrice
Tax = ExtendedPrice * 0.07
Total = ExtendedPrice + Tax
print(f"Quantity: {QuantityOfItems}")
print(f"Unit Price: ${UnitPrice:.2f}")
print(f"Extended Price: ${ExtendedPrice:.2f}")
print(f"Tax: ${Tax:.2f}")
print(f"Total: ${Total:.2f}")
