import random
picks = []

userinput = int(input("How many quick picks?"))

for i in range(userinput):
    temp_picks = []
    for j in range (6):
        rand_no = random.randint(1,45)
        while rand_no in temp_picks:
            rand_no = random.randint(1, 45)
        temp_picks.append(rand_no)
    picks = (sorted(temp_picks))

    for each in picks:
        print("{:3}".format(each), end="")
    print()
        # ensuring no duplication

