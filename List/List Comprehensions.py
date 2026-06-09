##Create a new list containing the squares of the first 10 positive integers using a list comprehension
List = [num**2 for num in range(1,10)]
print(List)
##Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension
Even_List = [num for num in List if num%2 ==0 ]
print("Even Numbers:", Even_List)
