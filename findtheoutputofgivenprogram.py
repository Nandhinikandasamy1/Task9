data = [10, 501, 22, 37, 100, 999, 87, 351] #input list
result = filter (lambda x: x > 4, data) #Validating whether x is greater than 4 or not. If it is greater appending to result
print(list(result)) # printing the result

#Answer: Since all the values of list are greater than 4, all elements from input list will be printed in output
#output: [10, 501, 22, 37, 100, 999, 87, 351]
