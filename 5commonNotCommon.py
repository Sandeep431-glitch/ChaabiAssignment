#predefined user input lists
Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]
#function defination to compate to list
def comparingTwoList(list1, list2):
    #creating sets out of lists
    firstSet = set(list1)
    secondSet = set(list2)
    #using predefined intersection method to find the common elements between two sets
    commonElements = firstSet.intersection(secondSet)
    #using predefined symmetric_difference method to find the uncommon elements between two sets
    notCommonElements = firstSet.symmetric_difference(secondSet)
    #returning the output lists
    return commonElements, notCommonElements

print(comparingTwoList(Mainstream , must_watch))
