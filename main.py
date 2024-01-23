total_bill = float(input("What is the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
bill_per_person = total_bill / num_of_people
#substituting the values
bill_per_person = total_bill / num_of_people * (1 + 0.12)
bill = "{:.2f}". format(bill_per_person)
print(f"${bill}")