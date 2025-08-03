# a=open(r'C:\Users\Hp\Desktop\Python\file.txt','r')
# print(a.read())
# a.close()



# b=open(r'C:\Users\Hp\Desktop\Python\file.txt','r')
# c=b.readline()
# print(c)
# b.close()


# with open(r'C:\Users\Hp\Desktop\Python\file.txt', 'r') as z:
#     n = z.read()
#     print(n)



# with open(r'C:\Users\Hp\Desktop\Python\file.txt', 'r') as k:
#     file=k.read()
#     print(file)


# with open(r'C:\Users\Hp\Desktop\Python\textfile.txt','r') as new:
#     print(new.readlines())
#     print(new.name)
#     print(new.mode)
#     new.close()




# with open(r'C:\Users\Hp\Desktop\Python\textfile.txt',"r") as file1:
#         for line in file1:
#             print( line)
            


# with open(r'C:\Users\Hp\Desktop\Python\textfile.txt',"r") as file1:
#         i = 0;
#         for line in file1:
#             print("Iteration", str(i), ": ", line)
#             i = i + 1



with open(r'C:\Users\Hp\Desktop\Python\textfile.txt',"r") as file1:
    a=file1.read()
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    for i in a:
        print(i)




      