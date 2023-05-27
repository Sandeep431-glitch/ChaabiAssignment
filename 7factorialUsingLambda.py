#function defination
factorial = lambda a: 1 if a <= 1 else a*factorial(a-1)#calling factorial function recursivly using lambda 
#printing the result
print(factorial(5))