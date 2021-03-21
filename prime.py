prime = []
#prime number is a int and should greater than 1 
for i in range(2,9999):
#you can change "100" to another number which should greater than 1
    for d in range(2,i):
#"i" is referred as a dividend, "d" is a divisor. 
        if (i%d==0):
           break
#Ensure that “i” cannot be divisible by other integers greater than 1 and smaller than itself.
    else:
        prime.append(i)
#else all the rest number are prime number. 
#print all the prime number in the given range.
print(prime)
