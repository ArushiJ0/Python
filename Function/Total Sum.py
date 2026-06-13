def total_sum(List):
    total_cost=0
    for item in List:
        total_cost=+ item['Price']*item['Quantity']
    return total_cost

List = [{'item':'Milk', 'Quantity':4,'Price':45}, {'item':'Sugar', 'Quantity':2,'Price':75}]
print(total_sum(List))
