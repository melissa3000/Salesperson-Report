"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []

# opens file and assigns variable f to the opened file
f = open("sales-report.txt")
# iterates over each line in open file "f"
for line in f:
    #removes the blank spaces and new lines from the end of each line
    line = line.rstrip()
    #splits the information on the pipe symbol and assigns the variable entries
    entries = line.split("|")
    #assigns the first value in the list of entries as the salesperson
    salesperson = entries[0]
    #assigns the integer in index position 2 (the 3rd item) of entries as melons
    melons = int(entries[2])

    # if the value salesperson is found in the empty list salespeople,
    # position is the index of the salesperson in the list of salespeople.
    # Melons_sold with that index position now becomes melons (??this is weird - 
    # this just a way to create a list without duplicate salespeople?) 
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    #else, append salesperson to the salespeople list and melon to the melons sold list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# for each item in the range (0 to the length of the salespeople list), 
# print in the format: salesperson sold #sold melons. 
for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])



#*******************************************************************
""" Other ways to think through this:
Bring in the data and create a dictionary and then search among keys (name of salespeople)
for unique keys. Create value for each key, and add to that value when it occurs again.


