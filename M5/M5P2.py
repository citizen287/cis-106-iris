Item = input("Enter the item (A or B): ")
QuantityOfItems = input("Enter the quantity of items: ")
if Item == "A":
    UnitPrice = 10.00
else:
    UnitPrice = 20.00
ExtendedPrice = int(QuantityOfItems) * UnitPrice
print(f"Item: {Item}")
print(f"Unit Price: ${UnitPrice:.2f}")
print(f"Extended Price: ${ExtendedPrice:.2f}")
