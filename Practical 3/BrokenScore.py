score = float(input("Enter score: "))


def getscore(score):
    if score < 0 or score > 100:
        return ("Invalid score")
    elif score >= 90 and score <= 100:
        return ("Excellent")
    elif score >= 50 and score <= 90:
        return ("Passable")
    else:  # score <50 #
        return ("Bad")


getscore(score)
print (getscore(score))
