monthly_expense =  [2200,2350,2600,2130,2190]
print("Money extra spent in Feb", monthly_expense[1]- monthly_expense[0])
print("Total expense in first quarter",monthly_expense[0]+monthly_expense[1]+ monthly_expense[2])
if 2000 in monthly_expense :
    print("yes")
else:
    print("no")
monthly_expense.append(1980)
print(monthly_expense)
monthly_expense[3] =  monthly_expense[3] - 200
print (monthly_expense)
