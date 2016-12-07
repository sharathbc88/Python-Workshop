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

"""
def getuserlogin(prompt):
    username= input(prompt)
    return username

x = input('sbc')


count = 0
vowels = ["a","i","e","o","u"]
name = input("Enter ur name already :").lower()
for each in name:
    if each in vowels:
        count+=1

print("out of {} letters, {} has {} vowels".format(len(name),name,count))



number = int(input("tell me the number already: "))

def get_day(number):
    days = ["sun", "mon", "tue", "wed", "thur", "fri", "sat"]
    return days[number]

get_day(number)
print(get_day(number))
"""