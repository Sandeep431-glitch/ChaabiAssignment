#input dictionary list
data = [
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
]
#function defination for sorting the column
def sortingListFunc(data, columnKey):
    newData = sorted(data, key=lambda x: x[columnKey])# lamba is used to chage the sorting order of sorted method
    print(newData)#printing the output
    
sortingListFunc(data, "color")#calling the sorting function