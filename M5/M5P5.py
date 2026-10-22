LastName = input("Enter your last name: ")
NumberOfDependents = input("Enter the number of dependents: ")
GrossIncome = input("Enter your gross income: ")
AdjustedGrossIncome = float(GrossIncome) - int(NumberOfDependents) * 12000
if AdjustedGrossIncome > 50000:
    TaxRate = 0.20
else:
    TaxRate = 0.10
IncomeTax = AdjustedGrossIncome * TaxRate
if IncomeTax < 0:
    IncomeTax = 100
print(f"Last Name: {LastName}")
print(f"Gross Income: ${float(GrossIncome):.2f}")
print(f"Dependents: {NumberOfDependents}")
print(f"Adjusted Gross Income: ${AdjustedGrossIncome:.2f}")
print(f"Income Tax: ${IncomeTax:.2f}")
