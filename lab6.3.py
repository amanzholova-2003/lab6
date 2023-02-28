expenses = ((8000,500,1444),
          (3300,100,4356),
          (1123,100,1246),
          (10043,1000,900),
          )
sum_of_expense = 0
for expense in expenses:
    for expense_2 in expense:
        sum_of_expense+=expense_2
    

print(f"\nExpenses: {sum_of_expense}")


