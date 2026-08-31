print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? Rs."))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))      
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
print("Each person should pay: Rs." + str(bill_per_person))