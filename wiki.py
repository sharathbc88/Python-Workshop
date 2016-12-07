""" Get a filename from user with extension.
Try open the file using the filename.
Prompt error message if the file does not exist.
Or else, read out the content of the file.


outFile.close()
in_file = open(" ", "r")


in_file.close()

flag = True
while(flag):
    try:
        filename = input("enter a file name:")
        print(1)
        filepointer = open(filename)
        print(2)
        for each in filepointer:
            print(each)
        filepointer.close()
        flag = False
    except FileNotFoundError:
        print("enter a valid filename")

"""
a = 1,2,3
print(a)

