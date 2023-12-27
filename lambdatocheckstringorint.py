''' using lambda function validating all the elements in the list whether it is string or integer'''
data = [10, "STR", 22, "INGS", 100, "IN", 87, "INPUT"] #input list
int_result = filter (lambda x: isinstance(x,int), data) #Validating whether x is integer
print(list(int_result)) # printing the integers in list
str_result = filter (lambda x: isinstance(x,str), data) #Validating whether x is string
print(list(str_result)) # printing the strings in list

