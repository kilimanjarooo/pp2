myString = str(input())
reversedString = (''.join(reversed(myString)))
if(reversedString == myString):
    print("yes")
else:
    print("no")