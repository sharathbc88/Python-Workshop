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
        with open(filename, 'r') as f:
            for line in f:
                fields = line.rstrip('\n').split(',')
                itemlist.append([fields[0], fields[1], fields[2], fields[3]])
    except FileNotFoundError:
        print('Missing {} file, or missmatching file format.'.format(filename))
    import operator
    itemlist = sorted(itemlist, key=operator.itemgetter(1,2))

    return itemlist


# write details to csv file
def savedetailstocsvfile(filename, itemlist):
    """
        The 'savedetailstocsvfile' is  a user defined function that reads details from the CSV file.
        :param filename: Name of the file
        :param itemlist: variable list
        :return: list of records
        """
    x = len(itemlist)
    try:
        with open(filename, 'w') as f:
            for i in range(len(itemlist)):
                line = '{},{},{},{}\n'.format(itemlist[i][0], itemlist[i][1], itemlist[i][2], itemlist[i][3])
                f.write(line)
    except FileNotFoundError:
        print('Error occurred while saving details back to {} file.\n'.format(filename))




#display R - List required books
def requiredbooks():
    print("Required books:")
    total=0
    count=0
    #store item list to a varaible
    itemlist = readdetailsfromcsvfile(FILENAME)
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
def completedbooks():
    print("Completed books:")
    total=0
    count=0
    # store itemlist to the variable
    itemlist = readdetailsfromcsvfile(FILENAME)
    #display completed books
    for i in range(len(itemlist)):
        if 'c' in itemlist[i][3]:
            record = ' {}. {} by {} {} pages'.format(i, (itemlist[i][0]).ljust(40), (itemlist[i][1]).ljust(20),itemlist[i][2])
            print(record)
            total = total + int(itemlist[i][2])
            count = count + 1
    print("Total pages for {} books: {}".format(count,total))


#display M - Mark a book as completed
def markasrequired():
    count = 0
    #store itemlist to a varaible
    itemlist = readdetailsfromcsvfile(FILENAME)
    #check if the record book is read, then count
    for i in range(len(itemlist)):
        if 'r' in itemlist[i][3]:
            count += 1

    if count >0:
        #f the count of required books is greater than zero, then print required books
        requiredbooks()

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
            savedetailstocsvfile(FILENAME, itemlist)
            print("{} by {} marked as completed".format(itemlist[record_number][0],itemlist[record_number][0]))

    else:
        print("No required books") # there is no required books to be completed

# display A - Add new book
def addingnewbook():
    #create a new list to add the new record that needs updation in the existing file
    newitem =[]
    # read the file and store it
    itemlist = readdetailsfromcsvfile(FILENAME)
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
            itemlist.append(newitem)

            print("{} by {}, ({} pages) added to the reading list".format(title,author,pages))
            break
            #handles error from the input
        except ValueError:
            print("Invalid input; enter a valid number")
            continue
    return newitem

# intoduction involves reading the CSV file and print the number of books loaded
def introduction():
    itemlist = readdetailsfromcsvfile(FILENAME)
    print("{} books loaded from {}".format(len(itemlist), FILENAME))

def main():
    #	display a welcome message with your name in it
    print("Reading List 1.0 -by Sharath Basappa Chandranna")
    introduction()
    added_record =[]

    while True:
        valid_input = displaymenu()
        #	when the user chooses list required: display a neatly formatted (lined up)
        # list of all the required books with their details and a total of the number of pages of these books
        if valid_input == 'R':
            requiredbooks()

        #	when the user chooses list completed: display a similarly formatted list of completed books
        elif valid_input == 'C':
            completedbooks()

        elif valid_input == 'A':
            added_record = addingnewbook()

        elif valid_input == 'M':
            markasrequired()
        else:
            itemlist = readdetailsfromcsvfile(FILENAME)
            itemlist.append(added_record)
            savedetailstocsvfile(FILENAME, itemlist)
            print("{} books saved to {}".format(len(itemlist), FILENAME))
            print("Have a nice day :)")
            break

#print(readdetailsfromcsvfile.__doc__)
#print(savedetailstocsvfile.__doc__)
main()




