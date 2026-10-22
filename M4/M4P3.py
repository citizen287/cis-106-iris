MealTotal = input("Enter the total for the meal: ")
Tip15Percent = float(MealTotal) * 0.15
TotalWithTip15 = float(MealTotal) + Tip15Percent
Tip18Percent = float(MealTotal) * 0.18
TotalWithTip18 = float(MealTotal) + Tip18Percent
Tip20Percent = float(MealTotal) * 0.20
TotalWithTip20 = float(MealTotal) + Tip20Percent
print(f"With 15% Tip:\n\n{'Total:':<15}{float(MealTotal):5.2f}\n{'Tip:':<15}{Tip15Percent:5.2f}\n{'Total with Tip':<15}{TotalWithTip15:5.2f}\n")
print(f"With 18% Tip:\n\n{'Total:':<15}{float(MealTotal):5.2f}\n{'Tip:':<15}{Tip18Percent:5.2f}\n{'Total with Tip':<15}{TotalWithTip18:5.2f}\n")
print(f"With 20% Tip:\n\n{'Total:':<15}{float(MealTotal):5.2f}\n{'Tip:':<15}{Tip20Percent:5.2f}\n{'Total with Tip':<15}{TotalWithTip20:5.2f}")
