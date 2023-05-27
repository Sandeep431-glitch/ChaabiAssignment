#function defination
def fileExtensionAndTypeFunction(extensionDetailsString, filenamesList):
    #spliting extension input string, using ";" as delimeter, it will return a list
    extensionDetailsList = extensionDetailsString.split(';')
    #empty dictionary for extensions and file types
    dictionaryOfExtensionType = {}
    dictionaryOfFileType = {}
    #spliting element of extentionDetailsList into extension and filetype
    for i in extensionDetailsList:
        extension, fileType = i.split(',')
        #storing extension and filetype as key value pair in dictionaryOfExtensionType
        dictionaryOfExtensionType[extension] = fileType
    #spliting element of filenamesList into dictionary into small list
    for j in filenamesList:
        fileParts = j.split('.')
        #if length of fileParts is less than 2, that means its not a valid filename
        if len(fileParts) == 2:
            #storing small lists index 1 element into fileExtension
            fileExtension = fileParts[1]
            #if the file extension present in dictionaryOfExtensionType than it will proceed
            if fileExtension in dictionaryOfExtensionType:
                #assigning dictionaryOfFileType as a key with fileExtension as it's value
                dictionaryOfFileType[j] = dictionaryOfExtensionType[fileExtension]
            else:
                dictionaryOfFileType[j] = "unknown"#for invalid extension type
        else:
            dictionaryOfFileType[j] = "unknown"#for invalid extension type
            
    return dictionaryOfFileType


inputExtensionDetailsString = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
inputFilenamesList = ["abc.jpg", "xyz.xls", "text.csv", "123"]

#calling the function and printing the output
print(fileExtensionAndTypeFunction(inputExtensionDetailsString, inputFilenamesList))
