#function defination
def selectionSort(num):
    #to decrease the range of sorted array
    for i in range(len(num)):
        #position of smallest element in current array
        minposition = i
        #to check if there is any element smaller than minposition element
        for j in range(i, len(num)):
            if num[j] < num[minposition]:
                minposition = j
        #in the end of the iteration swaping the current smallest element with the newly found smallest element
        temp = num[i]
        num[i] = num[minposition]
        num[minposition] = temp
#input array
inputList = [5,416,54,21,6135,15,741]
# arrayLength = int(input("Enter Array length : "))
# arrayString = input("Enter " + str(arrayLength) + " integer elements separated by space : ")
#converting string to array of numbers
# arrayList = arrayString.split()
#calling the function
selectionSort(inputList)
#printing the sorted array
print(inputList)
