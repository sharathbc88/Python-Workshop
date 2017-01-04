print("Reading List 1.0 -by Sharath Basappa Chandranna")
FILENAME = 'Books.csv'

# displays options and check correctness of the input
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
    itemlist = readdetailsfromcsvfile(FILENAME)
    for i in range(len(itemlist)):
        if 'r' in itemlist[i][3]:
            record = ' {}. {} by {} {} pages'.format(i, (itemlist[i][0]).ljust(40), (itemlist[i][1]).ljust(20),itemlist[i][2])
            print(record)
            total = total + int(itemlist[i][2])
            count = count + 1
    if count > 0:
        print("Total pages for {} books: {}".format(count,total))
    else:
        print("No books")



#Display C - List completed books
def completedbooks():
    print("Completed books:")
    total=0
    count=0
    itemlist = readdetailsfromcsvfile(FILENAME)
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
    itemlist = readdetailsfromcsvfile(FILENAME)
    for i in range(len(itemlist)):
        if 'r' in itemlist[i][3]:
            count += 1

    if count >0:
        requiredbooks()

        try:
            record_number = int(input("Enter the number of a book to mark as completed \n>>> "))
        except ValueError:
            while (True):
                try:
                    record_number = input("Invalid input; enter a valid number\n>>> ")
                    if record_number.isdigit():
                        break
                except ValueError:
                    continue
        record_number=int(record_number)

        if 'c' in itemlist[record_number][3]:
            print("That book is already completed")
        elif 'c' not in itemlist[record_number][3]:
            itemlist[record_number][3]='c'
            savedetailstocsvfile(FILENAME, itemlist)
            print("{} by {} marked as completed".format(itemlist[record_number][0],itemlist[record_number][0]))

    else:
        print("No required books")

# display A - Add new book
def addingnewbook():
    newitem =[]
    itemlist = readdetailsfromcsvfile(FILENAME)
    title = str(input("Title:"))
    while title == '':
        print("Input can not be blank")
        title = str(input("Title:"))

    author = str(input("Author:"))
    while author == '':
        print("Input can not be blank")
        author = str(input("Author:"))
    while True:
        try:
            pages = int(input("Pages:"))
            while pages < 0:
                print("Number must be >= 0")
                pages = int(input("Pages:"))
            newitem = [title,author,pages,'r']
            itemlist.append(newitem)
            savedetailstocsvfile(FILENAME, itemlist)
            print("{} by {}, ({} pages) added to the reading list".format(title,author,pages))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
            continue


def introduction():
    itemlist = readdetailsfromcsvfile(FILENAME)
    print("{} books loaded from {}".format(len(itemlist), FILENAME))

def main():

    while True:
        valid_input = displaymenu()
        if valid_input == 'R':
            requiredbooks()
        elif valid_input == 'C':
            completedbooks()
        elif valid_input == 'A':
            addingnewbook()
        elif valid_input == 'M':
            markasrequired()
        else:
            itemlist = readdetailsfromcsvfile(FILENAME)
            savedetailstocsvfile(FILENAME, itemlist)
            print("{} books saved to {}".format(len(itemlist), FILENAME))
            print("Have a nice day :)")
            break

#print(readdetailsfromcsvfile.__doc__)
#print(savedetailstocsvfile.__doc__)
main()




