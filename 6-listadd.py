#6.	Write a program to find the sum of the given elements of the list. 

total = 0
list1 = [1, 2, 3, 4, 5]   
for ele in range(0, len(list1)): 
    total = total + list1[ele] 
print("Sum of all elements in given list: ", total) 