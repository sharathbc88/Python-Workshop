#text = {"this is a collection of words of nice words this is a fun thing it is"}

sentence = str(input("Enter a sentence: ")).split()
count = {}
for each in sentence:
    if each in count: #if it exist in count dict
        count[each] += 1
    else: #first time
        count[each] = 1

for each in count:
    print("{:11s} : {:2d}".format(each,count[each]))



