"""
Debugging:
Someone (it’s not polite to say who) was trying to write a program to tell the user if their score is
 invalid, bad, passable or excellent, but their code is in the “bad” category and doesn’t work.
Rewrite the following programming attempt (in a file called fixedScore.py) using the most efficient
 if-elif-else ‘ladder’ you can. The code is also available at: """

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90 and score <= 100:
    print("Excellent")
elif score >= 50 and score <=90:
    print("Passable")
else:  # score <50 #
    print("Bad")
