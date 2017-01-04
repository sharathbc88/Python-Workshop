"""
name: Sharath Basappa Chandranna
date: 1/4/2017
brief program details: This program is a simple reading list that allows a user to track books they wish to read and books
                        they have completed reading. The program maintains a list of books in a file, and each book has:
                        •	title, author, number of pages, whether it is required or completed (r or c)
                        Users can choose to see the list of required books or completed books, including a total of the number
                         of pages of the book list. The lists will be sorted by author then by number of pages (increasing).
                        Users can add new books and mark books as completed.
                        They cannot change books from completed to required.
link to my project on GitHub: https://github.com/sharathbc88/CP5632_Workshop/tree/master/Assignment
"""


# name of the CSV file stored in a constant
FILENAME = 'Books.csv'

# displays options and check correctness of the input
#	return to the menu after each action and loop until the user chooses to quit
def displaymenu():
    MENUTEXT ="Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit\n>>> "

    # Get user input
    user_input = (input(MENUTEXT)).upper()

    # Input checking
    while user_input not in ('R', 'C', 'A', 'M', 'Q'):
        print("Invalid menu choice")
        user_input = input(MENUTEXT)
        user_input = user_input.upper()

    return user_input


#	load a CSV (Comma Separated Values) file of books
# read details from csv file
def readdetailsfromcsvfile(filename):
    """
        The 'readdetailsfromcsvfile' is  a user defined function that reads details from the CSV file.
        :param filename: Name of the file
        :return: list of records
    """
    # declare record list
    itemlist = []

    try:
        with open(filename, 'r') as f: # open file
            for line in f:
                fields = line.rstrip('\n').split(',')
                itemlist.append([fields[0], fields[1], fields[2], fields[3]])
    except FileNotFoundError: #error handling
        print('Missing {} file, or missmatching file format.'.format(filename))
    import operator
    itemlist = sorted(itemlist, key=operator.itemgetter(1,2))

    return itemlist


# write details to csv file
def saveDetailstoCsvFile(filename, itemlist):
    """
        The 'savedetailstocsvfile' is  a user defined function that saves details to the CSV file.
        :param filename: Name of the file
        :param itemlist: variable list
        records of books are written to the file
        """

    try:
        with open(filename, 'w') as f: # write file
            for i in range(len(itemlist)):
                line = '{},{},{},{}\n'.format(itemlist[i][0], itemlist[i][1], itemlist[i][2], itemlist[i][3])
                f.write(line)
    except FileNotFoundError: #error handling
        print('Error occurred while saving details back to {} file.\n'.format(filename))
    import operator
    itemlist = sorted(itemlist, key=operator.itemgetter(1, 2))



#display R - List required books
def requiredbooks(itemlist):
    print("Required books:")
    total=0
    count=0
    #store item list to a varaible

    #Display requiredbooks
    for i in range(len(itemlist)):
        if 'r' in itemlist[i][3]:
            record = ' {}. {} by {} {} pages'.format(i, (itemlist[i][0]).ljust(40), (itemlist[i][1]).ljust(20),itemlist[i][2])
            print(record)
            total = total + int(itemlist[i][2])
            count = count + 1
    if count > 0:
        #if there is atleast 1 required book, then print
        print("Total pages for {} books: {}".format(count,total))
    else:
        #if there is no required books in the itemlist
        print("No books")



#Display C - List completed books
def completedbooks(itemlist):
    print("Completed books:")
    total=0
    count=0
    # store itemlist to the variable

    #display completed books
    for i in range(len(itemlist)):
        if 'c' in itemlist[i][3]:
            record = ' {}. {} by {} {} pages'.format(i, (itemlist[i][0]).ljust(40), (itemlist[i][1]).ljust(20),itemlist[i][2])
            print(record)
            total = total + int(itemlist[i][2])
            count = count + 1
    print("Total pages for {} books: {}".format(count,total))


#display M - Mark a book as completed
def markasrequired(itemlist):
    count = 0
    #store itemlist to a varaible
    #check if the record book is read, then count
    for i in range(len(itemlist)):
        if 'r' in itemlist[i][3]:
            count += 1

    if count >0:
        #f the count of required books is greater than zero, then print required books
        requiredbooks(itemlist)

        try:
            #ask the number of the book that needs to be changed
            record_number = int(input("Enter the number of a book to mark as completed \n>>> "))
        # if there is error below exception takes care
        except ValueError:
            while (True):
                try:
                    #ask again for valid number
                    record_number = input("Invalid input; enter a valid number\n>>> ")
                    # check if the value is a digit
                    if record_number.isdigit():
                        break # exists the loop
                except ValueError:
                    continue # returns to the top of loop
        record_number=int(record_number)
        # check if it is already completed or not
        if 'c' in itemlist[record_number][3]:
            print("That book is already completed")
        elif 'c' not in itemlist[record_number][3]:
            itemlist[record_number][3]='c'
            print("{} by {} marked as completed".format(itemlist[record_number][0],itemlist[record_number][0]))

    else:
        print("No required books") # there is no required books to be completed


# display A - Add new book
def addingnewbook(itemlist):
    #create a new list to add the new record that needs updation in the existing file
    newitem =[]
    # read the file and store it
    # add title and check for errors
    title = str(input("Title:"))
    while title == '':
        print("Input can not be blank")
        title = str(input("Title:"))
    # add author and check for errors
    author = str(input("Author:"))
    while author == '':
        print("Input can not be blank")
        author = str(input("Author:"))
     # Add page number and check for errors
    while True:
        try:
            pages = int(input("Pages:"))
            while pages < 0:
                print("Number must be >= 0")
                pages = int(input("Pages:"))
            newitem = [title,author,pages,'r']
            #update the new item to the existing list only to the memory but not to the file

            print("{} by {}, ({} pages) added to the reading list".format(title,author,pages))
            break
            #handles error from the input
        except ValueError:
            print("Invalid input; enter a valid number")
            continue
    itemlist = itemlist.append(newitem)

# intoduction involves reading the CSV file and print the number of books loaded
def introduction():
    itemlist = readdetailsfromcsvfile(FILENAME)
    print("{} books loaded from {}".format(len(itemlist), FILENAME))

def main():
    #	display a welcome message with your name in it
    print("Reading List 1.0 -by Sharath Basappa Chandranna")
    introduction()
    added_record =[]

    itemlist = readdetailsfromcsvfile(FILENAME)
    while True:

        # print(itemlist)
        valid_input = displaymenu()
        #	when the user chooses list required: display a neatly formatted (lined up)
        # list of all the required books with their details and a total of the number of pages of these books

        if valid_input == 'R':
            requiredbooks(itemlist)

        #	when the user chooses list completed: display a similarly formatted list of completed books
        elif valid_input == 'C':
            completedbooks(itemlist)

        #	when the user chooses add: prompt for the book’s title, author and number of pages,
        #   error-checking each of these, then add the book to the list in memory (not to the file)
        elif valid_input == 'A':
            #added_record =
            addingnewbook(itemlist)
            #itemlist = itemlist.append(added_record)
        #	when the user chooses mark completed: display the list of required books (same as for list)
        # then allow the user to choose one book (error-checked), then change that book to completed
        elif valid_input == 'M':
            markasrequired(itemlist)

        #	when the user chooses quit: save the books to the CSV file, overwriting the file contents
        else:
            saveDetailstoCsvFile(FILENAME, itemlist)
            print("{} books saved to {}".format(len(itemlist), FILENAME))
            print("Have a nice day :)")
            break

#print(readdetailsfromcsvfile.__doc__)
#print(saveDetailstoCsvFile.__doc__)
main()




