#5.	Write a program to add the elements of 2 arrays that are of the same dimension.

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,2]
lst3=[]
for i in range(len(lst1)):
    lst3.append(lst1[i]+lst2[i])
print(lst3)