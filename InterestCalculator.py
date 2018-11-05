print("Interest Calculator")
amount = float(input("Principal Amount? "))
roi = float(input("Rate of Interest? "))
years = int(input("Duration (number of years)? "))

total = (amount * pow(1 + roi/100, years))
interest = total - amount
print("\nAmount of Interest Earned = $%0.2f" %interest)

