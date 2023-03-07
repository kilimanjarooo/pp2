string = str(input())
cnt1 = 0
cnt2 = 0
i = 0
while(i < len(string)):
    if (string[i].islower()):
        cnt1 += 1
    elif (string[i].isupper()):
        cnt2 += 1
    i+=1
print(cnt1, cnt2)