ApplianceName = input("Enter the name of the appliance: ")
ApplianceCost = input("Enter the cost of the appliance: ")
if float(ApplianceCost) > 1000:
    WarrantyCost = float(ApplianceCost) * 0.10
else:
    WarrantyCost = float(ApplianceCost) * 0.05
Total = float(ApplianceCost) + WarrantyCost
print(f"Appliance: {ApplianceName}")
print(f"Cost: ${float(ApplianceCost):.2f}")
print(f"Warranty: ${WarrantyCost:.2f}")
print(f"Total: ${Total:.2f}")
