numbers = []
for i in range(1,6):
    x = int(input("Number:"))
    numbers.append(x)

print("The first number is :",(numbers[0]))
print("The last number is :",(len(numbers)))
print("The smallest number is :",(min(numbers)))
print("The largest number is :", (max(numbers)))
print("The average of the numbers is:",((sum(numbers))/len(numbers)))