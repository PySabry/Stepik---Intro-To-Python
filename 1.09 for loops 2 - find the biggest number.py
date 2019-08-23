# this first line will take a input of numbers separated by spaces and convert them into a "list"
mylist = map(int, input().split())

# print(mylist) # you can uncomment this line to see the list in Thonny

biggestnum = -1 # why do I set the biggest number to be -1 at the start? Does it have something to do with the fact that I know my input numbers are between 0 and 1000?

for mynumber in mylist: # this will go trhough the whole list one at a time
    if (mynumber>biggestnum): #...if mynum is the biggest number so far...: CHANGE THIS LINE
       biggestnum = mynumber  #...set biggestnum to that...  AND THIS LINE, THAT'S IT!!!!
print (biggestnum)