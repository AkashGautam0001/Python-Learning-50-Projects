number_of_people = int(input("How many people are there in the group? "))
people_name = []

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

for i in range(number_of_people):
    name = input("Enter name : ")
    people_name.append(name)

amount = get_float("Enter Amount : ")

slip_amount = amount/number_of_people

for i in people_name:
    print(f"{i} owes {round(slip_amount, 2)} rupees")

print("Total Amount : ", amount)