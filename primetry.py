# user input number
num = int(input("Do you want to determine prime numbers？ \nPlease enter a number(Between 1 ~ 999999): "))
 
#prime number is a int and should greater than 1 
if num > 1:
   for d in range(2,num):
#"num" is referred as a dividend, "d" is a divisor. 
       if (num % d) == 0:
           print(num,"Is not a prime number!")
#explain why this num is not a prime number
           print("Because",d," * ",num//d," = ",num)
           break
   else:
       print(num,"Is a prime number!")

# if num <= 1, this num is not a prime number
else:
   print(num,"is not a prime number!Prime number should greater than 1!")