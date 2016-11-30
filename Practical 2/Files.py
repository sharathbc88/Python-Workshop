#Write a program that asks the user for their name, then opens a file called “name.txt” and writes that name to it.
outFile = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=outFile)  # or outFile.write(name)
outFile.close()

#Write a program that opens “name.txt” and reads the name (as above) then prints,
#“Your name is Bob” (or whatever the name is in the file).

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

""" First, create a text file called “numbers.txt”.
Put the numbers 17 and 42 on separate lines in the file and save it.
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the result, which should be… 59.
"""

outFile = open("numbers.txt", "w")
number1 = 17
number2 = 42
print(number1,file=outFile)
print(number2,file=outFile)
outFile.close()
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print("total:",number1 + number2)
in_file.close()
