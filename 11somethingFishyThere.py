def f(x, l=[]):# here if we dont provide 2nd argument, than the function will take a empty list as its 2nd default argument
    for i in range(x):# x is the range for the iteration so the loop will run x times, from 0 to (x-1)
        l.append(i*i)#here it's appending the squared value of current iteration index into the list
    print(l)#printing the list
    
f(2)#here we did not provided the second argument, so the expected out of list is [0, 1]

f(3,[3,2,1])#here we provided the 2nd argument, 
            #so the append function will simply 
            # append the square value of current 
            # iteration index to end of [3, 2, 1].
            #so the expected out put for this [3, 2, 1, 0, 1, 4]

f(3)#here for loop will run for 3 times(0-(3-1)) and 
    #the output should be [0*0, 1*1, 2*2] = [0, 1, 4]
    #but we are getting [0, 1, 0, 1, 4].  So the reason behind this is, 
    # we have taken a mutable type as a default argument, so because 
    # we are calling the same function multiple time in a same run time 
    # the first result of function call will be stored in the default list and 
    # next time when we called the function with value 3, the result will be append after the f(2) result, 
    # so thats why we are getting the previous value in this list
    
#this code will solve the problem  
def newf(x, l=None):
    if l is None:
        l = []
    for i in range(x):
        l.append(i*i)
    print(l)

newf(2)
newf(3, [3,2,1])
newf(3)
