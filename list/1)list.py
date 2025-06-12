list = ["The Bodyguard", 7.0, 1992]
print(list)

#Nested list
list2=["The Bodyguard", 7.0, 1992, [1, 2], ("A", 1)]
print(list2)

#Slicing
list3=L = ["The Bodyguard", 7.0,1992,"BG",1]
print(list3[3:5])
print(list3[3][1])

#Extend
list3=L = ["The Bodyguard", 7.0,1992,"BG",1]
list3.extend(['pop',10])
print(list3)

#Append
L = [ "The Bodyguard", 7.0]
L.append(['a','b'])
print(L)

#copy()
my_list = [1, 2, 3, 4, 5] 
new_list = my_list.copy() 
print(new_list) 
# Output: [1, 2, 3, 4, 5]

#count()
my_list = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list.count(2) 
print(count) 
# Output: 4

#insert
my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) 
print(my_list)

#pop it prints the element that is removed
a=[1,2,'hi',9]
print(a.pop(2))

#remove()
b=['hi',12,1,5,3,'new']
b.remove(12)
print(b)

#reverse
my_list = [1, 2, 3, 4, 5] 
my_list.reverse() 
print(my_list)

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
a='hard rock'.split()
print(a)

# Split the string by comma
a='A,B,C,D'.split(',')
print(a)

#QUIZ QUESTIONS
new_list=[1, 'hello', [1,2,3], True]
print(new_list)
print(new_list[1])
print(new_list[1:4])
A = [1, 'a'] 
B = [2, 1, 'd']
print(A+B)
