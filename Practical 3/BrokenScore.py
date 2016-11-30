score = float(input("Enter score: "))


def getscore(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90 and score <= 100:
        print("Excellent")
    elif score >= 50 and score <= 90:
        print("Passable")
    else:  # score <50 #
        print("Bad")


getscore(score)