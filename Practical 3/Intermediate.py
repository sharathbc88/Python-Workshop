def get_number(lower,upper):
    while (True):
        try:
            user_input = int(input("enter the number between {}-{}:".format(lower,upper)))
            if user_input < lower:
                print("number is too low")
            elif user_input > upper:
                print ("number is too large")
            else:
                return user_input
        except ValueError:
            print("error in number")

returned_value = get_number(10, 50)
print("the returned value is {}".format(returned_value))