#importing desired methods from datetime library
from datetime import datetime, timedelta

def getDateResult(date, numberOfDays):
    # it will convert the date string into a date and time object
    dateObject = datetime.strptime(date, '%y-%m-%d').date()
    # Calculating the date before mentioned days
    dateResult = dateObject - timedelta(days = numberOfDays)
    # Converting the date object into a string
    finalDateString = dateResult.strftime('%y-%m-%d')
    #returning the result
    return finalDateString

#printing the output
print(getDateResult('16-12-10', 11))