a=[2,5,2,7,8,9,4,5]
b=sorted(a)
print(b)

# a=[2,5,2,7,8,9,4,5]
# a.sort()
# print(a)

a=[2,5,2,7,8,9,4,5]
b=sum(a)
print(b)

highest = max([5, 12, 8, 23, 16])
print(highest)

lowest = min([5, 12, 8, 23, 16])
print(lowest)

a=[2,5,2,7,8,9,4,5]
b=len(a)
print(b)


def val1(a):
    b=a+2
    print(b)
val1(2)

c=val1(5)


def val(a,b):
    c=a+b
    print(c)
val(10,15)

c=val(5,5)


def sum(a=5, b=10):
    c=a+b
    print(c)
sum(7)

def mul(a,b):
    c=a*b
    print(c)
mul(2,'Zunaisha')

def name():
    print('Zunaisha Javaid')
name()

def none():
    pass
print('pass function')
none()



def rat(ratings):
    for index, i in enumerate(ratings):
        print('indeex',index,'has',i,'ratings' )
ratings=[4.4,5,3.5,3.8,4]
rat(ratings)

def nm(*names):
    for i in names:
        print(i)
nm('Zunaisha','Eman','Hadi')

# def aa(name):
#     for i in name:
#         print(i)
# name=['abcc','xyz','uvw']
# aa(name)


def value(limit):
    for i in range(1,limit+1):
        print(i)
value(7)


def add_num(my_list,number):
    if number not in my_list:
        my_list.append(number)
        print('num added',my_list)
    else:
        print('not added')
list=[2,3,4,5,1]
add_num(list,8)

def remove_number(my_list, number):
    if number in my_list:
        my_list.remove(number)
        print(my_list)
    else:
        print(number, "is not in the list.")
list=[3,4,6,7]
remove_number(list,4)


def type_of_album(album, year_released):
    
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("The BodyGuard", 1980)
print(x)


string= "The BodyGuard is the best album"
def check_string(text):
    if text in string:
        print('String matched')
    else:
        print('String not matched')

check_string("The BodyGuard is the best")