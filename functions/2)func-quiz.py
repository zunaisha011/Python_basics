# Come up with a function that divides the first input by the second input:
def div():
    num1=int(input('Enter num 1:'))
    num2=int(input('Enter num 2:'))
    ans=num1/num2
    print(ans)
div()


# Write a function code to find total count of word little in the given string: "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"**
def freq(string,passedkey):
    words = []
    words = string.split() 
    Dict = {}
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)   
    print("Total Count:",Dict)
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")