i=1
while i<=5:
    print(i)
    i+=1

# Print even numbers from 2 to 10
i=2
while i<=10:
    print(i)
    i+=2

# Countdown from 5 to 1
i=5
while i>=1:
    print(i)
    i-=1

# Sum of first 5 natural numbers
i=1
sum=0
while i<=5:
    sum+=i
    i+=1
print('Sum',sum)


dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
print("It took ", i ,"repetitions to get out of loop.")