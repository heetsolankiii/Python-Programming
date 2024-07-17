"""WAP to accept no. of items to be ordered from the user. The rate of each item is Rs.200. 
If the no.of items are more than the discount is more as per the following table.
No. of items            Discount
1-50                    No discount
51-100                  Rs.150 discount
101-150                 Rs.200 discount
151-200                 Rs.250 discount
Above 200               10% discount
"""
numItems = int(input("Enter number of items: "))
itemRate = 200
totalCost = numItems * itemRate
if 1 <= numItems <= 50:
    print("No discount applied")
    print("Total Bill of Rs.", totalCost)
elif 51 <= numItems <= 100:
    discount = 150
    print("Discount of Rs.150 applied")
    totalCost = totalCost - discount
    print("Total Bill of Rs.", totalCost)
elif 101 <= numItems <= 150:
    discount = 200
    print("Discount of Rs.200 applied")
    totalCost = totalCost - discount
    print("Total Bill of Rs.", totalCost)
elif 151 <= numItems <= 200:
    discount = 250
    print("Discount of Rs.250 applied")
    totalCost = totalCost - discount
    print("Total Bill of Rs.", totalCost)
elif numItems > 200:
    discount = 0.10
    print("Discount of 10% applied")
    discountedCost = totalCost * discount
    finalCost = totalCost - discountedCost
    print("Total Bill of Rs.", finalCost)
else:
    print("Invalid number entered.")