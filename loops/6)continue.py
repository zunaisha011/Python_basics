# I want to skip two values here, so I will use or, I can't use and because i can't be both 1 and 6 at the same time.
for i in range(1,20):
    if i==6 or i==1:
        continue
    print(i)

colors = ["red", "blue", "pink", "green", "yellow"]
for a in colors:
    if a == 'green':
        continue
    print(a)

i=1
while i<=7:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1
