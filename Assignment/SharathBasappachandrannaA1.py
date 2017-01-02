print("Welcome Sharath Basappa Chandranna")
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
        user_input = input(menutext)
        user_input = user_input.upper()

    return user_input

# read details from csv file
def readdetailsfromcsvfile(filename):
    # declare item list
    itemlist = []

    try:
        with open(filename, 'r') as f:
            for line in f:
                if len(line) == 0:
                    continue
                else:
                    fields = line.rstrip('\n').split(',')
                    itemlist.append([fields[0], fields[1], fields[2], fields[3]])
    except FileNotFoundError:
        print('Missing {} file, or missmatching file format.'.format(filename))
    import operator
    itemlist = sorted(itemlist, key=operator.itemgetter(1, 2),reverse=True)
    return itemlist

readdetailsfromcsvfile(FILENAME)
itemlist = readdetailsfromcsvfile(FILENAME)

# write details to csv file
def savedetailstocsvfile(filename, itemlist):
    try:
        with open(filename, 'w') as f:
            for i in range(len(itemlist)):
                line = '{},{},{},{}\n'.format(itemlist[i][0], itemlist[i][1], itemlist[i][2], itemlist[i][3])
                f.write(line)
    except FileNotFoundError:
        print('Error occured while saving details back to {} file.\n'.format(filename))


savedetailstocsvfile(FILENAME,itemlist)