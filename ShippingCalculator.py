"""" A shipping company requires a small program that would allow them to quickly work out total
shipping charge for a number of items, each with different prices.
The program allows the user to enter the number of items and the shipping cost for each different item.
Then the program computes and displays the total shipping cost.
If the total shipping cost is over $100, then a 10% discount is applied to the total shipping cost before
the amount is displayed on the screen."""


quantity = int(input("Enter quantity in numbers: "))
count = 0
Total_shipping_cost = 0
if quantity >0:
    while quantity != count:
        shipping_cost = float(input("Enter the shipping cost of item %s:"%(count+1)))
        count = count + 1
        Total_shipping_cost = shipping_cost + Total_shipping_cost
    if Total_shipping_cost > 100:
        Total_shipping_cost = Total_shipping_cost *.9
        print ("Total shipping cost:%s"%(Total_shipping_cost))
    else:
        print ("Total_shipping_cost:%s"% (Total_shipping_cost))
else:
    print ("Invalid number of items!")
    quantity = int(input("Enter quantity in positive numbers: "))
