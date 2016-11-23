"""name = "gib"
year = 1922
cost = 143.5

print ("my name " + name +" "  +str(year))
print ("my guitar: {}, first made in {}".format(name, year))
print ("my guitar: {1}, first made in {0}".format(name, year))
print ("my {0} was first made in {1} (that's right, {1}!)" .format(name,year))

#formatting currency

print ("my {} would cost $ {:,.2f}".format(name,cost))

#aligning columns

numbers = [1, 19, 123, 456, -25]
print(len(numbers))

for i in range(len(numbers)):
    print ("number {0} is {1:>5}".format(i+1, numbers[i]))

    """
password= "Wabcdef12"
count=0
for char in password:
    if char is lower
        count = count + 1
print(count)