#importing desired methods from datetime library
from datetime import datetime, timedelta

def getDateDiffrenceResult(date1, date2, diffrenceInDates):
    # it will convert the date string into a date and time object
    dateObject1 = datetime.strptime(date1, '%y-%m-%d').date()
    dateObject2 = datetime.strptime(date2, '%y-%m-%d').date()

    # Calculating the date before mentioned days
    dateDiffrence = dateObject1 - dateObject2
    finalDiffrence = dateDiffrence.days#into integer
    #checking if the input date diffrence is less than or greater than actual date diffrence
    if (finalDiffrence < diffrenceInDates):
        return True
    else:
        return False
#printing the output
print(getDateDiffrenceResult('16-12-10', '16-11-13', 10))