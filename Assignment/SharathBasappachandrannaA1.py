print("Reading List 1.0 -by Sharath Basappa Chandranna")
FILENAME = 'Books.csv'


def displaymenu():
    menutext ="""Menu:
    R - List required books
    C - List completed books
    A - Add new book
    M - Mark a book as completed
    Q - Quit
    Enter an option:  """

    # Get user input
    user_input = (input(menutext)).upper()

    # Input checking
    while user_input not in ('R', 'C', 'A', 'M', 'Q'):
        print("Invalid menu choice")
        user_input = input(menutext)
        user_input = user_input.upper()

    return user_input

# read details from csv file
def readdetailsfromcsvfile(filename):
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
    x = len(itemlist)
    try:
        with open(filename, 'w') as f:
            for i in range(len(itemlist)):
                line = '{},{},{},{}\n'.format(itemlist[i][0], itemlist[i][1], itemlist[i][2], itemlist[i][3])
                f.write(line)
    except FileNotFoundError:
        print('Error occurred while saving details back to {} file.\n'.format(filename))
    print("{} books saved to {}".format(x, filename))



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

    pages = int(input("Pages:"))
    while pages < 0:
        print("Number must be >= 0")
        pages = int(input("Pages:"))
    newitem = [title,author,pages,'r']
    itemlist.append(newitem)
    print("{} by {}, ({} pages) added to the reading list".format(title,author,pages))



def main():
    itemlist = readdetailsfromcsvfile(FILENAME)
    print("{} books loaded from {}".format(len(itemlist), FILENAME))
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
            savedetailstocsvfile(FILENAME, itemlist)
            print("Have a nice day :)")
            break

main()


