#1.	Start new file, asciiTable.py,
# and rewrite the cumbersome print line to do the same thing but using string formatting with the str.format() method

lower = 10
upper = 100
print("Enter a number {}-{}:".format(lower,upper))

"""
Now write code that displays a table with two columns, one for the numeric ASCII value and the other for the character itself. Use the str.format() method to align the text in the columns nicely.
To figure out the formatting, use this for loop as a test in your program:
"""

for i in range(10,120,11):
    print("{:3}{:^3}".format(i,chr(i)))
