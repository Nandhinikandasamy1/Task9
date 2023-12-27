def fibonacci(n): #Creating a function
  return (lambda x, y: x + y)(0, 1) if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2) #Using lambda function adding the values of two values and creating fibonacci series.  

fib_series = list(map(fibonacci, range(1, 51))) #generating 50 elements of fibbonacci series and  storing that in variable
print(fib_series)#printing the variable
