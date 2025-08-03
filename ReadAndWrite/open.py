# a=open(r'C:\Users\Hp\Desktop\Python\file.txt','r')
# print(a.read())
# a.close()



# b=open(r'C:\Users\Hp\Desktop\Python\file.txt','r')
# c=b.readline()
# print(c)
# b.close()


with open(r'C:\Users\Hp\Desktop\Python\file.txt', 'r') as z:
    n = z.read()
    print(n)



with open(r'C:\Users\Hp\Desktop\Python\file.txt', 'r') as k:
    file=k.read()
    print(file)