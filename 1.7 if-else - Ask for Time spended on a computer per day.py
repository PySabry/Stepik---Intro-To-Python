# Make sure your output matches the assignment *exactly*
spend_string = input("How long do you spend on a computer per day? ")
spend = int(spend_string)
if (spend < 2):
    print("That seems reasonable")
else:
    print("You need to get outside more!")
