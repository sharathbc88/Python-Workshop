"""def convert_farhenheit(celcius):
    return celcius * 9/ 5 + 32

print(convert_farhenheit(12))"""


num= int(input(prompt))
print (1)
def main():
    lhs = getNum("Enter the first number")
    rhs= getNum("Enter the second number")
    displayResults(lhs, rhs)
print(2)
def getNum(prompt):
    num= int(input(prompt))
    return num
print(3)
def displayResults(num1, num2):
    print ("Sum of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2))
    print("Product of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2))
    print (str(num1) + " to the power of " + str(num2) + " is " + str(num1 ** num2))
print(4)
main()