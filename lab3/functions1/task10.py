def uniqueList(input_list):
    unique = []
    for element in input_list:
        if element not in unique:
            unique.append(element)
    return unique

myList = input().split()
print(uniqueList(myList))