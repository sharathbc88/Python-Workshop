"""def getuserlogin(prompt):
    username= input(prompt)
    return username

x = input('sbc')

"""
def main():
    lhs = getnum("enter the first number")
    rhs= getnum("enter the second number")
    displayresults(lhs,rhs)

def getnum(prompt):
    num = int(input(prompt))
    return num

def displayresults(num1,num2):
    print("sum of " + str(num1) +" and " + str(num2) + " is " + str(num1+num2))

main()

