newList = [];#taking a empty list
#declaring the function
def everyOtherSublist(inputList, indices1, indices2):
    for i in range(indices1, indices2, 2):#incrementing value of i by 2 with each iteration
        newList.append(inputList[i])#appending each second element into the empty list
    return newList#returning the resultant list
#calling the function
print(everyOtherSublist([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9))
        