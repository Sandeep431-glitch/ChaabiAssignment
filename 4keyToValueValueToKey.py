#input dictionary
userDict = {'a': 1, 'b': 2, 'c': 3}
#function definition
def swapKeyAndValue(inputDict):
    return {value: key for key, value in inputDict.items()}#using .item() method to iterate over its key-value pairs
#calling the function and storing new dictionary
newDict = swapKeyAndValue(userDict)
#printing new dictionary
print(newDict)