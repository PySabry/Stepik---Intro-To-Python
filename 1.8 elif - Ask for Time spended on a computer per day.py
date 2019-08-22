# Make sure your output matches the assignment *exactly*
spend = input("How long do you spend on a computer per day? ")
spe_int = int(spend)
if spe_int < 2:
    print("That seems reasonable")
elif spe_int < 4:
    print("Do you have time for anything else? ")
else:
    print("You need to get outside more!")
