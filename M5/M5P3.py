NumberOfBooks = input("Enter the number of books to order: ")
CostPerBook = input("Enter the cost per book: ")
OrderTotal = int(NumberOfBooks) * float(CostPerBook)
if OrderTotal > 50.00:
    ShippingCharge = 0
else:
    ShippingCharge = 25
print(f"Order Total: ${OrderTotal:.2f}")
print(f"Shipping Charge: ${ShippingCharge:.2f}")
