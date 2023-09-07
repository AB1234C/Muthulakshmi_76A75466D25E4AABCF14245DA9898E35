#1.1 implement a recursive function to calculate the factorial of a given number
def factorial(n):
     

    if (n==1 or n==0):
         
        return 1
     
    else:
         
        return (n * factorial(n - 1))
 
num = 8;
print("number : ",num)
print("Factorial : ",factorial(num))

