#  Q1. Print numbers 5 to 10 using a for loop.
for i in range(5,11):
    print(i)

# Q2. Print all even numbers between 1 and 20.
for numbers in range(1,21):
    if numbers%2==0:
        print(numbers)

# Q3. Loop through this list and print each fruit:
# fruits = ["apple", "banana", "cherry", "grape"]
fruits = ["apple", "banana", "cherry", "grape"]
for fruit in fruits:
    print(fruit)


# Q4. Print this pattern using a for loop:
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print('*' * i)

# Q5. Count how many vowels are in this string using a for loop:
# text = "I love programming"
text = "I love programming"
a='aeiousAEIOUS'
count=0
for i in text:
    if i in a:
        count+=1
print('No. of vowels are:',count)

#  Q6. Use a for loop with enumerate() to print each subject with its number:

# subjects = ["Math", "Science", "English"]
subjects = ["Math", "Science", "English"]
for index, i in enumerate(subjects, start=1):
    print(index,i)

# Write a for loop that prints out all the elements between -5 and 5 using the range function.
for i in range(-5,5):
    print(i)