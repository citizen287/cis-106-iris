LastName = input("Please enter your last name: ")
MidtermScore = input("Please enter your midterm score(0–100 points): ")
FinalScore = input("Please enter your final exam score(0–100 points): ")
TotalExamPoint = int(MidtermScore) * 0.4 - int(FinalScore) * 0.6
print(f"{LastName} your total exam points is {TotalExamPoint}.")