def calculate_bill_split(amount, num_of_people):
    amount_to_pay = amount / num_of_people
    return "R" + str(amount_to_pay)
print(calculate_bill_split(1500, 5))