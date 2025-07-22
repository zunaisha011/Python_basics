colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    print(color)
# Output
# red
# orange
# yellow
# green
# blue
# indigo
# violet

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    print(colors)
# OUTPUT
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# 1 - 10
for i in range(1,11):
    print(i)


for i in range(11):
    print(i)

# Enumerate
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")


list1=['one','two','three','four']
for index, i in enumerate(list1, start=1):
    print(index,i)

for i in range(3):
    print("Hi")


dates = [1982,1980,1973]
N = len(dates)
print(N)
# for i in dates:
#     print(i)
for i in range(N):
    print(dates[i]) 

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

