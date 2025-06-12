tuple1 = ("disco",10,1.2 )
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
print(tuple1[-1])

#Concatenation
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

#Slicing
print(tuple2[3:5])

#Sorting
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
print(sorted(Ratings))

# #Nested Tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print(NestedT[2][1])
print(NestedT[2][1][0])

#count
a=(1,2,5,22,2,4,3,5,2)
print(a.count(2))

#sum
a=(1,2,5,22,2,4,3,5,2)
print(sum(a))

#min and max
numbers = (10, 20, 5, 30)
print(min(numbers))  
#Output: 5
print(max(numbers))
#Output: 30

