        #problem 1

'''a = int(input("Enter your No. "))

if(a>0):
    print("positive")
elif(a<0):
    print("negative")
else:
    print("zero")'''


      #problem 2

'''a = int(input("Enter your No. "))

if(a%2==0):
    print("even")

else:
    print("odd")'''

     #problem 3

'''a = int(input("Enter your No. "))

if(a%5==0):
    print("yes it is divisible by 5")

else:
    print("no it is not divisible by 5")'''

#problem 4

'''a = int(input("Enter your No. "))

if(a%3==0 and a%5==0):
    print("yes it is divisible by 3 and 5")

else:
    print("no it is not divisible by 3 and 5")'''

#problem 5


'''a = int(input("Enter your No. "))

if(a%4==0):
    print("yes this year is leap year")

else:
    print("no this year is not a leap year")'''

# problem 6

'''a = int(input("Enter your No. "))
b = int(input("Enter your No. "))

if(a>b):
    print(a)

else:
    print(b)'''

#problem 7

'''a = int(input("Enter your No. "))
b = int(input("Enter your No. "))
c = int(input("Enter your No. "))

if(a>b and a>c):
    print("largest no is ",a)

elif(b>a and b>c):
    print("largest no is ",b)

else:
    print(c)'''

#problem 8

'''a = int(input("Enter your No. "))

if(a<20):
    print("the temprature is Cold ")

elif(a>20 and a<30):
    print("the temprature is Warm ")

else:
    print("the temprature is Hot")'''

   #problem 9


'''b = (input("Enter your character. ")).lower()
if b in ('a','e','i','o','u'):
    print("vowel")

elif b.isalpha():
    print("consonent")


else:
    print("not character")'''


     #problem 10

'''a = input("Enter your Character. ")

if a.islower():
    print("lowercase")
elif a.isupper():
    print("uppercase")
elif a.isdigit():
    print("digit")
else:
    print("symbol")'''

        #problem 11

'''a = int(input("Enter your No. "))
b = int(input("Enter your No. "))
c = int(input("Enter your No. "))

if(a>b+c or b>a+c or c>a+b):
    print("valid traingle")

else:
    print("not valid traingle")'''


    #problem 12

'''a = int(input("Enter your No. "))
b = int(input("Enter your No. "))
c = int(input("Enter your No. "))

if(a==b==c):
    print("Traingle is equilateral")
elif(a==b  or  c==a  or  b==c ):
    print("Traingle is isoceles")
else:
    print("Traingle is scalene")'''

   #problem 13

'''a = int(input("Enter your No. "))

if(a<33):
    print("F")
elif(a >= 33 and a < 55):
    print("D")
elif(a >= 55 and a < 75):
    print("C")
elif(a >= 75 and a < 90):
    print("B")
   
else:
    print("A")'''


   #problem 14

'''a = int(input("Enter your No. "))
b = int(input("Enter your No. "))

if(a%b==0):
    print(a,"is a multiple of ",b)
elif(b%a==0):
    print(b,"is multiple of ",a)
else:
    print("Neither number is a multiple of the other")'''

   #problem 15

'''a = int(input("Enter your hour No.(0-23) "))

if(a >= 1 and a < 5 or a >= 19 and a < 24):
    print("good night")
elif(a >= 5 and a < 12):
   print("good morning")
elif(a >= 12 and a < 16):
    print("good afternoon")
    
else:
    print("good evening")'''

  #problem 16


'''a = int(input("Enter your No. "))
b = int(input("Enter your No. "))

if(a%2==0 and b%2==0):
    print(" both are even")
elif(a%2!=0 and b%2!=0):
    print("both are odd")
else:
    print("one is odd and one is even")'''


   #problem 17  ***

'''char = (input("enter your character.(a-z)")).lower()

if char.isalpha() and len(char)==1:
    if 'a' <= char <= 'm':
        print("the character lies btwn A-M ")
    elif 'n' <= char <= 'z':
        print("the character is lies btwn N-Z")
    else:
        print("enter a valid single digit character")'''


  #problem 18 ***

'''num = int(input("Enter your THREE Digit No. "))

a = num//100
b = (num//10)%10
c = num%10

if(a != b and b != c and c != a):
    print("digits are distinct")
else:
    print("digits are same")'''


    #problem 19

'''num = int(input("Enter your No. "))

a = num//100
b = (num//10)%10
c = num%10

if(b > a and b > c):
    print("largest digit")
elif(b < a and b < c):
    print("smallest digit")
else:
    print("neither largest nor smallest")'''

  #problem 20

'''num = int(input("Enter your four digit No. "))  

a = num // 1000
b = (num//100)%10
c = (num//10)%10
d = num%10

if(a==d):
    print("first and last digit are equal")
else:
    print("not equal")'''

   #problem 21

'''num = int(input("Enter your four digit No. "))  

n = abs(num)

if(n < 10):
    print("single digit")
elif(n > 10 and n < 100):
    print("double digit")
else:
    print("multi digit")'''

#problem 22

'''num = int(input("Enter your digit No. "))

a = num%10

if( num%7==0 or a == 7):
    print("yes , condition is true")
else:
    print("condition is not true")'''


  #problem 23

'''x = int(input("Enter your NO."))
y = int(input("Enter your NO."))

if(x > 0 and y > 0):
    print("first quadrant")
elif(x < 0 and y > 0):
    print("second quadrant")
elif(x < 0 and y < 0):
    print("third quadrant")
else:
    print("fourth quadrant")'''


    #problem 24

'''amount = int(input("enter your amount."))

if(amount % 2000 == 0):
    print("the amount can be evently divided into 2000 notes")
elif(amount % 500 == 0):
    print("the amount can be evently divided into 500 notes")
elif(amount % 100 == 0):
    print("the amount can be evently divided into 100 notes")
else:
    print("the amount can not be evently divided into 2000,500,100 notes")'''

   #problem 25

'''angel1 = int(input("Enter your NO."))
angel2 = int(input("Enter your NO."))

angel3 = 180-(angel1 + angel2)

print("third angel :",angel3)'''

  #problem 26 ***

'''# Take input
num = int(input("Enter a number: "))

# Initialize a flag
is_perfect_square = False

# Loop through possible factors
for i in range(1, num + 1):
    if i * i == num:
        is_perfect_square = True
        break

# Display result
if is_perfect_square:
    print(num, "is a Perfect Square.")
else:
    print(num, "is NOT a Perfect Square.")'''


   #problem 27

'''char = (input("Enter a character: ")).lower()

if char.isalpha():
    print("this is letter")
elif char.isdigit():
    print("this is digit")
else:
    print("neither")'''

   #problem 28

'''a = int(input("Enter your No. "))

if(a%3==0 and a%5!=0):
    print("Fizz")
elif(a%5==0 and a%3!=0):
    print("Buzz")
elif(a%3==0 and a%5==0):
    print("FizzBuzz")
else:
    print("no comments")'''

   #problem 29

'''a = int(input("Enter your No. "))
b = int(input("Enter your No. "))
c = int(input("Enter your No. "))

if(a>b and a<c or a>c and a<b):
    print(a,"median")
elif(b>a and b<c or b<a and b>c):
    print(b,"median")
elif(c>a and c<b or c>b and c<a):
    print(c,"median")
else:
    print("no median")'''


    #problem 30

'''a = int(input("Enter your age: "))
b = int(input("Enter your income. "))

if(a>18 and b>5):
    print("yes, he is eligible to pay tax")
else:
    print("No,he is not eligible to pay tax")'''


   #problem 31

'''elc_unit = float(input("enter your unit. "))

a = 100
b = elc_unit*10

if(elc_unit<=100):
    print("₹",a)
else:
    print("₹",b)'''

   #problem 32 ***


'''password = input("Enter your password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Valid password ✅")
else:
    print("Invalid password ❌")
    print("Password must be at least 8 characters long and contain at least one digit.")'''


   #problem 33

'''X = int(input("Enter your No: "))
Y = int(input("Enter your No. "))

if(X>0 and Y==0 or X<0 and Y==0):
    print("point lies in X axis")
elif(X==0 and Y>0 or X==0 and Y<0):
    print("point lies in Y axis")
elif(X==0 and Y==0):
    print("point lies in origin")
else:
    print("points lies btn X and Y axis")'''


    #problem 34

'''a = int(input("Enter your No: "))
b = int(input("Enter your No. "))
c = int(input("Enter your No. "))

if(a*a + b*b == c*c or c*c + b*b == a*a or a*a + c*c == b*b):
    print("yes ,its a pythagorian triplet")
else:
    print("No,its not a pythagorian triplet")'''
   

    #problem 35

'''date = int(input("Enter your No: "))
month = int(input("Enter your No. "))

if(0==date<=31 and month == 1):
    print("January")
elif(0==date<=28 and month == 2):
    print("febuary")
elif(0==date<=31 and month == 3):
    print("march")
elif(0==date<=30 and month == 4):
    print("april")
elif(0==date<=31 and month == 5):
    print("may")
elif(0==date<=30 and month == 6):
    print("june")
elif(0==date<=31 and month == 7):
    print("july")
elif(0==date<=31 and month == 8):
    print("august")
elif(0==date<=30 and month == 9):
    print("september")
elif(0==date<=31 and month == 10):
    print("october")
elif(0==date<=30 and month == 11):
    print("november")
elif(0==date<=31 and month == 12):
    print("december")
else:
    print("invalid date and month")'''

    #problem 36

'''a = int(input("Enter your No: "))

b = a//100
c = a%10
d = (a//10)%10

if(b+c==d):
    print("yes")
else:
    print("no")'''


  #problem 37

'''num = int(input("Enter your 4 digit No:(1-9999) "))

a = num//1000
b = (num//100)%10
c = (num//10)%10
d = (num%10)
sum = a+b+c+d
prod = a*b*c*d

if(sum>prod):
    print("sum is grater than product")
elif(prod==sum):
    print("sum and product are equal")
else:
    print("product is greater than sum")'''


    #problem 38

'''day1 = int(input("Enter first date day: "))
month1 = int(input("Enter first date month: "))

day2 = int(input("Enter first date day: "))
month2 = int(input("Enter first date month: "))

if(month1<month2 ):
    print("day1 and month1 come first")
elif(month1>month2):
    print("day2 and month2 come first")
else:
    print("dates are same")'''

    #problem 39 ***

'''# Take year as input
year = int(input("Enter a year: "))

# Calculate century
century = (year - 1) // 100 + 1

# Print with suffix (st, nd, rd, th)
if century % 10 == 1 and century != 11:
    suffix = "st"
elif century % 10 == 2 and century != 12:
    suffix = "nd"
elif century % 10 == 3 and century != 13:
    suffix = "rd"
else:
    suffix = "th"

print(f"{century}{suffix} century")'''


  #problem 40  loop 

'''for i in range(1,11):
   print(i)'''

   #problem  41


'''for i in range(2,100,2):
  
     print(i)

     or

for i in range(2,100):
   if(i%2==0):
     print(i)'''



   #problem 42

'''for i in range(1,100):
    if(i%2!=0):
        print(i)'''


    #problem 43

'''for i in range(10,0,-1):
    print(i)'''

  #problem 44

'''n = int(input("Enter your No: "))

for i in range(1,11):
    print(f"table of {n}X{i} =",{n*i})'''


   #problem 45

'''a = int(input("Enter your No: "))

sum = a*(a+1)/2
print(f"the sum of first",a,"natural no is",abs(sum))'''

   #problem 46

'''a = int(input("Enter your No: "))
sum = 0

for i in range(2,a+1,2):
  sum += i

  print("the sum of all  even number up to ",a, "is",sum)'''


   #problem 47


'''a = int(input("Enter your No: "))
sum = 0

for i in range(1,a+1,2):
  sum += i

  print("the odd of all  odd number up to ",a, "is",sum)'''


   #problem 48


'''n = int(input("Enter your no. "))

prod = 1

for i in range(1,n+1):
    prod = prod*i

print(f"the factorial of {n} is {prod}") '''


   #problem 49

'''n = int(input("Enter your no. "))

prod = 1

while n>0:

      digits = n%10
      prod = prod * digits
      n = n//10

      print("the product of given no digits is",prod)'''

  #problem 50

'''n = int(input("Enter your no. "))
count = 0
while n>0:

    n = n//10
    count += 1

    print(count)'''


 #problem 51


'''n = int(input("Enter your no. "))

rev = 0

while n > 0 :
     
    digit = n%10
    rev = rev *10 + digit
      
    n = n//10
    print("the reverse of digit is ",rev)

    or 

n = (input("Enter your no. "))

rev = ""

for digit in n:

 rev = digit + rev  

 print("the reverse of digit is ",rev)'''


    # problem 52

'''n = int(input("Enter your no. "))
temp = n
rev = 0

while n > 0:

    digit = n % 10
    rev = rev*10 + digit
    n = n//10

if (temp == rev):
    print("this is palindrome")
else:
    print("this is not palindrome")'''


   #problem 53


'''n = int(input("Enter your no. "))

sum = 0

while n > 0:

    digit = n%10
    sum = sum+digit
    n = n//10

    print(sum)'''


   #problem 54

'''n = int(input("Enter your no. "))
temp = n
arms_no = 0

while n > 0:
    digit = n%10
    n = n//10
    arms_no = arms_no + digit*digit*digit

if(arms_no == temp):
    print("armstrong number")
else:
    print("not armstrong number")'''


    #problem 55

'''n = int(input("Enter your no. "))
sum = 0

for i in range(1,n):
    if(n%i==0):
        
        sum = sum + i

        if(sum == n):
            print("No. is perfect square")
        else:
            print("No. is not a perfect square")'''


      #problem 56


'''print("Prime numbers between 1 and 100 are:")

for num in range(2, 101):   # start from 2 (smallest prime)
    for i in range(2, num):
        if num % i == 0:    # if divisible by any number other than 1 and itself
            break
    else:
        print(num)'''


    #problem 57

'''n = int(input("Enter your no. "))

if n<=0:
    print("not a prime no")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime no")
            break
        else:
            print("its a prime no")'''



      #problem 58


'''n = int(input("Enter your no. "))

a = 0
b = 1


for i in range(n):
    print(a,end=" ")
    c = a + b
    a = b
    b = c'''

   #problem 59


'''n = int(input("Enter number of terms: "))

a = 0
b = 1
sum = 0

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    sum = sum + a     # add each term to sum
    c = a + b
    a = b
    b = c

print("\nSum of the series:", sum)'''


     #problem 60

'''n = int(input("Enter number of terms: "))

square = 1

for i in range(1,n+1):
    square =  i**2

    print(square)'''


    #problem 61

'''n = int(input("Enter number of terms: "))

square = 1

for i in range(1,n+1):
    square =  i**3

    print(square)'''


    #problem 62

'''a = int(input("Enter number of terms: "))
b = int(input("Enter number of terms: "))

print("the divisible no btwn ",a ,"and",b, "is")

for i in range (a,b+1):
    if i%7==0:
        print(i)'''


   #problem 63

'''a = int(input("Enter number of terms: "))
b = int(input("Enter number of terms: "))

hcf = 1

for i in range(1,min(a,b)+1):
    if(a%i==0 and b%i==0):
        hcf = i

        print("the hcf of A and B is",hcf)'''
   
     #problem 64

'''a = int(input("Enter number of terms: "))
b = int(input("Enter number of terms: "))

lcm = 1

for i in range(1,min(a,b)+1):
    if(a%i==0 and b%i==0):
        lcm = lcm*i
        print(f"LCM of {a} and {b} is ",lcm)'''


     #problem 65


'''a = int(input("Enter number of terms: "))

factor = 1

for i in range(1,a+1):
    if a%i==0:
        factor = i
        print(factor)'''


   #problem 66

'''num = int(input("Enter a number: "))
temp = num
sum = 0

for digit in str(num):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    sum += fact

if sum == temp:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")'''


  # problem 67

'''a = int(input("Enter first term : "))
n = int(input("Enter common difference number: "))
d = int(input("Enter no. of terms: "))

print("Arithmetic Progression:")

for i in range(n):
    terms = a + i * n
    print(terms,end=" ")'''


    #problem 68


'''a = int(input("Enter first term (a): "))
r = int(input("Enter common ratio (r): "))
n = int(input("Enter number of terms (n): "))

print("Geometric Progression:")
for i in range(n):
    term = a * (r ** i)
    print(term, end=" ")'''


     #problem 69



'''for i in range(1,101):
    temp = i
    sum = 0

    while temp>0:
     digit = temp%10
     temp//=10
     sum = sum + digit
  

    if(sum%2==0):
        print(i)'''


    #problem 70

'''count = 0

for i in range(1,501):

    temp = i
    count += 1
    

    if(temp%7==0 and temp%5!=0):
        print(i)'''


    #problem 71

'''for i in range(1, 501):
    temp = i
    rev = 0
    
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    if i == rev:
        print(i)'''


    #problem 72


'''for i in range(1, 101):
    temp = i
    sum = 0

    # find sum of digits
    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10

    # check divisibility by 3
    if sum % 3 == 0:
        print(i)'''


    #problem 73   ***


'''num = int(input("Enter a number: "))

small = 9     
large = 0     

temp = num
while temp > 0:
    digit = temp % 10       
    if digit < small:
        small = digit       
    if digit > large:
        large = digit       
    temp = temp // 10      

print("Smallest digit:", small)
print("Largest digit:", large)'''


   #problem 74

'''n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(i * i)'''


   #problem 75


'''n = int(input("Enter a number: "))

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    print("Factorial of", i, "is", fact)'''


   #problem 76

'''num = int(input("Enter a number: "))

sum_even = 0
sum_odd = 0

while num > 0:
    digit = num % 10        # extract last digit
    if digit % 2 == 0:      # even digit
        sum_even += digit
    else:                   # odd digit
        sum_odd += digit
    num = num // 10         # remove last digit

print("Sum of even digits:", sum_even)
print("Sum of odd digits:", sum_odd)'''


   #problem 77

'''sum_nonzero = 0

for i in range(5):
    num = int(input("Enter a number: "))
    if num == 0:
        continue        # skip 0 and move to next input
    sum_nonzero += num   # add non-zero numbers

print("Sum of all non-zero numbers:", sum_nonzero)'''

    #problem 78    RECURSION


'''def print_num(n):
    if n == 0 :
        return
    print_num(n-1)
    print(n)
print_num(5) '''


   #problem 79
         

'''def print_num(n):
    if n==0:
        return
    print(n)
    print_num(n-1)
print_num(5)  '''


#problem 80

'''def even_no(n):
    if n == 0:
        return
    even_no(n-1)
    if n%2==0:
        print(n)

n = int(input("enter your no "))
print("Even no btwn 1 to ",n, "is")
odd_no(n)'''


#problem 81

'''def odd_no(n):
    if n == 0:
        return
    odd_no(n-1)
    if n%2!=0:
        print(n)

n = int(input("enter your no "))
print("odd no btwn 1 to ",n, "is")
odd_no(n)'''


#problem 82


'''def natural_no(n):
    if n==0:
        return 0
    else:
        return n + natural_no(n-1)
            

n = int(input("enter your no. "))
print("sum of n natural no is ",natural_no((n)))'''


#problem 83

'''def factorial_no(n):
    if n == 1:
        return 1
    else:
        return n*factorial_no(n-1)
    
n = int(input("enter your no. "))
print("the factorial of ",n,"is ",factorial_no(n))'''

#problem 84


'''def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
    
a = int(input("enter your no. "))
b = int(input("enter your no. "))
print(f"the value of {a} ki power  {b} is {power(a,b)} ")'''


#problem 85


'''def fibb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
    
n = int(input("enter your no. "))
print("the fibinacco series is ")
for i in range(0,n):
    print(fibb(i),end=" ")'''


#problem 86


'''def fibb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
    
n = int(input("enter your no. "))
print("the fibinacco series is ",fibb(n))'''


#problem 87


'''def sum(n):
    if n==0:
        return 0
    else:
        return n%10 + sum(n//10)
     
n = int(input("enter your no. "))
print("the sum of digit  is ",sum(n))'''



#problem 88


'''def count(n):
    if n==0:
        return 0
    else:
        return 1+count(n//10)
    
n = int(input("enter your no. "))
print("total digit",count(n))'''


#problem 89


'''def reverse(n):
    if n==0:
        return 
    print(n)
    (reverse(n-1))
    
n = int(input("enter your no. "))
(reverse(n))'''


#problem 90 ***


'''def rev_no(n,rev=0):
    if n==0:
        return rev
    else:
        return rev_no(n//10,rev*10+n%10)
    
def palindrome(n):
    if n==rev_no(n):
        return True
    else:
        return False
    
n = int(input("enter your no. "))

if palindrome(n):
    print(n,"-> this is palindrome")
else:
    print(n,"-> this is not palindrome")'''
    
    
#problem 91


'''def product(n):
    if n==0:
        return 1
    else:
        return n%10 * product(n//10)

n = int(input("enter your no. "))
print("The product of digits is ",product(n)) '''



#problem 92


'''def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
    
a = int(input("enter your no. "))
b = int(input("enter your no. "))
print(f"The HCF of {a} and {b} is {hcf(a,b)}")'''


#problem 93 ***


'''def to_binary(n):
    if n == 0:
        return ""
    else:
        return to_binary(n // 2) + str(n % 2)

n = int(input("Enter a number: "))

# handle case when n == 0 separately
if n == 0:
    print("Binary:", 0)
else:
    print("Binary:", to_binary(n))'''


#problem 94


'''def even(n):
    if n==0:
        return 0
    elif n%2==0:
        return n + even(n-1)
    else:
        return even(n-1)
    
n = int(input("Enter a number: "))
print("The sum of n even noo is ",even(n))'''


#problem 95


'''def odd(n):
    if n==0:
        return 0
    elif n%2!=0:
        return n + odd(n-1)
    else:
        return odd(n-1)
    
n = int(input("Enter a number: "))
print("The sum of n odd no is ",odd(n))'''


#problem 96


'''def print_star(n):
    if n == 0:
        return
    print("*",end="")
    print_star(n-1)
    
n = int(input("enter your no "))
(print_star(n))'''


#problem 97   ***


'''def star_square(n):
    if n == 0:
        return 
    print("*",end="")
    star_square(n-1)

def square(n,size):
    if n==0:
        return
    star_square(size)
    print()
    square(n-1,size)


n = int(input("enter your no "))
square(n,n)'''



#problem 98

'''def star_traingle(n):
    if n == 0:
        return 
    print("*",end="")
    star_traingle(n-1)

def traingle(n):
    if n==0:
        return
    star_traingle(n)
    print()
    traingle(n-1)

n = int(input("enter your no "))
traingle(n)'''


#problem 99

'''def star_traingle(n):
    if n == 0:
        return 
    
    star_traingle(n-1)
    print("*",end="")

def traingle(n):
    if n==0:
        return
    print()
    star_traingle(n)
    traingle(n-1)
    

n = int(input("enter your no "))
traingle(n)'''


#problem 100


'''def star_traingle(n):
    if n == 0:
        return 
    
    print("*",end="")
    star_traingle(n-1)
  

def bottom_star(n,current=1):
    if current>n:
        return
    star_traingle(current)
    print()
    bottom_star(n,current+1)

n = int(input("enter your no "))
bottom_star(n)'''


#problem 101

'''def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n,end="")

def num(n,current=1):
    if current>n:
        return
    print_num(current)
    print()
    num(n,current+1)

n = int(input("enter your no "))
num(n)'''



#problem 102

'''def num_traingle(n):
    if n == 0:
        return 
    
    num_traingle(n-1)
    print(n,end="")

def traingle(n):
    if n==0:
        return
    print()
    num_traingle(n)
    traingle(n-1)
    

n = int(input("enter your no "))
traingle(n)'''


#problem 103


'''def table(n,i=1):
    if i>10:
        return
    print(f"{n}*{i}={n*i}")
    table(n,i+1)

n = int(input("enter your no "))
table(n)'''


#problem 104

'''def inc_dec(n,i=1):
    if i>n:
        return
    print(i,end=" ")
    inc_dec(n,i+1)
    print(i,end=" ")

n = int(input("enter your no "))
inc_dec(n)'''


#problem 105   ARRAYS


'''n = int(input("enter your no "))

array = []

for i in range(n):
    val = int(input("enter your no "))
    array.append(val)
    print(array)'''


#problem 106


'''n = int(input("enter your no "))

array = []


for i in range(n):
    val = int(input("enter your no "))
    array.append(val)
    total = sum(array)
    print(total)'''


#problem 107


'''n = int(input("enter your no "))

array = []


for i in range(n):
    val = int(input("enter your no "))
    array.append(val)
    total = sum(array)
    avg = total/n
    print(avg)'''


#problem 108


'''n = int(input("enter your no "))

array = []


for i in range(n):
    val = int(input("enter your no "))
    array.append(val)
    print(max(array))'''


#problem 109

'''n = int(input("enter your no "))

array = []


for i in range(n):
    val = int(input("enter your no "))
    array.append(val)
    print(min(array))'''



#problem 110


'''n = int(input("enter your no "))

array = []


for i in range(n):
    val = int(input("enter your no "))
    array.append(val)

    pos = neg = zero = 0
    for x in array:
        if x>0:
            pos += 1
        elif x<0:
            neg += 1
        else:
            zero += 1

            print(f"pos value = {pos},neg value = {neg},zero value = {zero}")'''



#problem 111


'''n = int(input("enter your no "))

array = []


for i in range(n):
    val = int(input("enter your no "))
    array.append(val)

    odd = even = 0
    for x in array:
        if x%2==0:
            even += 1
        else:
            odd += 1

            print(f"even no = {even}, odd no = {odd}")'''


#problem 112


'''n = [21,45,32,56,78,61,31]

max_value = max(n)
index = n.index(max_value)

print(f"maximum value : {max_value}")
print(f"maximum value index : {index}")'''


#problem 113


'''n = [21,45,32,56,78,61,31]

min_value = min(n)
index = n.index(min_value)

print(f"minimum value : {min_value}")
print(f"minimum value index : {index}")'''



#problem 114

'''n = int(input("Enter number of elements: "))
array = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    array.append(val)

k = int(input("Enter number to compare: "))

# find all elements greater than k
greater = [x for x in array if x > k]

print("Elements greater than", k, "are:", greater)'''



#problem 115

'''n = (input("Enter number of elements: "))

if ("x" in n):
    print("exist")
else:
    print("not exist")'''


#problem 116



'''n = int(input("Enter number of elements: "))


arr = []


for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)


x = int(input("Enter element to search: "))


if x in arr:
    print(f"{x} exists in the array.")
else:
    print(f"{x} does not exist in the array.")'''



#problem 117


'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

for x in arr:
    count_x = arr.count(x)
               
    print(f"{x} is repeated {count_x} times")'''
        

#problem 118


'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

print("\nArray:",arr)

x = int(input("Enter the number to find the first occurance : "))
if x in arr:
    index = arr.index(x)
    print(f"the first occurance of {x} is at index {index}")'''


#problem 119  ***


'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

print("\nArray:",arr)

x = int(input("Enter the number to find the last occurance : "))
if x in arr:
    last_index = len(arr)-1-arr[::-1].index(x)
    print(f"the last occurance of {x} is at index {last_index}")'''


#problem 120

'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

for x in arr:
    count_x = arr.count(x)
    if count_x==1:
        print("unique")
    else:
        print("not unique")'''


#problem 121

'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

sum_even = 0
for x in arr:
    if x%2==0:
      sum_even = sum_even + x
print("sum of even element : ",sum_even)'''


#problem 122

'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

sum_odd = 0
for x in arr:
    if x%2!=0:
      sum_odd = sum_odd + x
print("sum of odd element : ",sum_odd)'''


#problem 123

'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

count = 0
for x in arr:
    if x%3==0 and x%5==0:
        count += 1
        print("count no which no is divisible by 3 and 5 ",count)'''



#problem 124  ***

'''import math
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)

count = 0
for x in arr:
    if x>= 0:
        root = int(math.sqrt(x))
        if root*root == x:
            count += 1
            print("count of perfect square no ",count)'''



#problem 125

'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)
print("\narray",arr)

new_arr = []
for x in arr:
    new_arr.append(x*x)
print("the square of old array is ",new_arr)'''



#problem 126

'''n = int(input("Enter number of elements: "))

even_list = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    if val%2==0:
       even_list.append(val)
print("even list",even_list)'''


#problem 127

'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)
print("\nOriginal array",arr)

for i in range(n):
    if arr[i]<0:
        arr[i]=0

print("the negative no replace with 0 ",arr)'''



#problem 128


'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)
print("\nOriginal array",arr)

for i in range(n):
    if arr[i]%2==0:
        arr[i]=1
    else:
        arr[i]=0
print(f"the even no replace with 1 and the odd no replace with 0",arr)'''


#problem 129


'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)
print("\nOriginal array",arr)

if n>1:
    arr[2],arr[1] = arr[1],arr[2]
print("swap an element of array",arr)'''


#problem 130


'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)
print("\nOriginal array",arr)

first = arr[0]
for i in range(len(arr)-1):
    arr[i] = arr[i+1]

arr[-1] = first

print("after left rotation",arr)'''


 #problem 131  ***

'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)
print("\nOriginal array",arr)

last = arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-1]

arr[0] = last

print("after right rotation",arr)'''


# problem 132 ***


'''n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    val = int(input(f"Enter elements {i+1}: "))
    arr.append(val)
print("\nOriginal array",arr)

for i in range(0,len(arr)-1,2):
    arr[i],arr[i+1] =arr[i+1],arr[i]
print("swap four element ",arr)'''


#problem 133

'''arr1 = [1,2,3,4,5]
arr2 = [0]*len(arr1)

for i in range(len(arr1)):
    arr2[i] =arr1[i]
print("original arr ",arr1)
print("copied arr",arr2)'''


#problem 134

'''arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5]

if arr1 == arr2:
    print("order and element are equal")
else:
    print("not equal")'''


#problem 135


'''arr1 = [1,2,3,4,5]
arr2 = [1,3,2,5,4]

if  sorted(arr1) == sorted(arr2):
    print("same element")
else:
    print("differ element")'''



#problem 136

'''arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

arr3 = []

arr3 = arr1 + arr2
print("merge two arrays ",arr3)'''


# problem 137


'''a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for x in a:
    if x in b:
        common.append(x)

print("Common elements:", common)
'''


# problem 138

'''arr1 = [1,2,3,4,5]
arr2 = [8,7,2,5,6]

arr3 = (list(set(arr1)^set(arr2)))

print(arr3)



or



a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

not_common = []

for x in a:
    if x not in b:
        not_common.append(x)

for x in b:
    if x not in a:
        not_common.append(x)

print("Not common elements:", not_common)'''



#problem 139


'''a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

count = 0

for x in a:
    if x in b:
        count += 1
       

print("Common elements:", count)'''



#problem 140


'''a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = []

for i in range(len(a)):
    c.append(a[i]+b[i])
    print(c)'''



#problem 141


'''a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = []

for i in range(len(a)):
    c.append(a[i]*b[i])
    print(c)'''



#problem 142

'''a = [1, 2, 3, 4, 4, 3 , 2 , 3]

freq = {}

for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
    print(freq,"times")'''



#problem 143  ***

'''a = [1, 2, 3, 4, 4, 3 , 2 , 3]

freq = {}

for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("Elements occur more than once")

for key,value in freq.items():
    if value>1:
        print(key)'''


#problem 144


'''arr1 = [1,2,3,4,5]
is_sorted = True

for i in range(len(arr1)-1):
    if arr1[i]>arr1[i+1]:
        is_sorted = False
        break
    if is_sorted:
        print("ascending order")
    else:
        print("not ascending order")'''


#problem 145


'''arr = [5,4,3,2,1]

is_sorted = True

for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        is_sorted = False
        break
    if is_sorted:
        print("decending order")
    else:
        print("not decending order")'''



#problem 146



'''arr = [3,4,5,2,1]

arr = list(set(arr)) #remove dublicate element

arr.sort()
print("second largest element",arr[-2])


or

arr = [3,4,5,2,1]

largest = float('-inf')
second_largest = float('-inf')

for x in arr:
    if  x > largest:
        second_largest == largest
        x == largest

    elif x < second_largest and x != largest:
        second_largest = x

print("second largest element",second_largest)'''



#problem 147


'''arr = [3,4,5,2,1]

arr = list(set(arr)) #remove dublicate element

arr.sort()
print("second largest element",arr[1])'''



#problem 148


'''arr = [3,4,5,2,1]

arr = list(set(arr)) #remove dublicate element
arr.sort()

arr1 = []
arr2 = []
diff = []

arr1.append(arr[-1])
arr2.append(arr[0])

for i in range(len(arr1)):
    diff.append(arr1[i]-arr2[i])
    print("difference btwn largest and smallest element ",diff)'''



#problem 149


'''arr = [3,4,5,2,1]

arr = list(set(arr)) #remove dublicate element

arr.sort()
arr.pop(0)
arr.pop(-1)
print(arr)

sum = 0

for x in arr:
    sum = sum + x
print(sum)'''



#problem 150


'''arr = [3,4,5,2,1]


k = 5
count = 0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):

        if arr[i]+arr[j] == k:
           count += 1
print(count)'''



#problem 151


'''arr = [3,4,5,2,1,6,7,8]


k = sum(arr)
print(k)
l = k/len(arr)
print(l)

count = 0

for i in range(len(arr)):
    if arr[i] > l:
           count += 1
print(count)'''



#problem 152 ***



'''arr = [1,2,2,3,2,4,5,3,5,7]

freq = {}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("frequency of each element")
for key,value in freq.items():
    print(key,":",value)'''



#problem 153


'''arr = [1,2,2,3,2,4,5,3,5,7]

for x in arr:
    if arr.count(x) == 1:
       print(x)'''



#problem 154  STRING



'''s = input("enter your string: ")
print(len(s))'''


#problem 155


'''s = input("enter your string: ")
print(s[0])
print(s[-1])'''


#problem 156

'''s = input("enter your string: ")
print(s.upper())'''


#problem 157


'''s = input("enter your string: ")
print(s.lower())'''



#problem 158



'''s = input("enter your string: ")

count = 0

for ch in s:
    if ch != " ":
        count += 1
print(count)'''



#problem 159


'''s = input("enter your string: ").strip()

count_words= 1

for ch in s:
    if ch == " ":
        count_words += 1
print(count_words)'''


#problem 160


'''s = input("enter your string: ").strip()
p = input("enter your string: ").strip()

result = s + " " + p
print(result)'''


# problem 161

'''s = input("enter your string: ").strip()
p = input("enter your string: ").strip()

if s == p:
    print("both string are equal")
elif s < p:
    print("first string come first")
else:
    print("second string come first")'''


#problem 162


'''
s = input("enter your string: ")

for ch in s:
    print(ch,":",ord(ch))'''


#problem 163


'''s = input("enter your string: ")

if len(s) == 0:
    print("Empty String")
else:
    print("Not Empty String")'''


#problem 164


'''s = input("enter your string: ")

vowel = "aeiouAEIOU"
vowel_count = 0
consonent_count = 0

for ch in s:
    if ch.isalpha():
       if ch in vowel:
        vowel_count += 1
       else:
        consonent_count += 1

print("vowel",vowel_count)
print("consonent",consonent_count)'''


#problem 165


'''s = input("enter your string: ")

count_digit = 0
count_alpha = 0
count_special_ch = 0

for ch in s:
    if ch.isalpha():
        count_alpha += 1
    elif ch.isdigit():
        count_digit += 1
    else:
        count_special_ch += 1

print("digit :",count_digit)
print("alphabet :",count_alpha)
print("special_character :",count_special_ch)'''


#problem 166


'''s = input("enter your string: ")

count_uppercase = 0
count_lowercase = 0

for ch in s:
    if ch.isupper():
        count_uppercase += 1
    elif ch.islower():
        count_lowercase += 1

print("uppercase :",count_uppercase)
print("lowercase :",count_lowercase)'''



#problem 167

'''s = input("enter your string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("frequency of string")
for key,value in freq.items():
    print(key,":",value)'''



#problem 168

'''s = input("enter your string: ")

count_space = 0

for ch in s:
    if ch == " ":
        count_space += 1
print("No of Spaces : ",count_space)'''


#problem 169


'''s = input("enter your string: ")
search_char = input("enter your char : ")

count_repeated_character = 0

for ch in s:
    if ch == search_char:
       count_repeated_character += 1

print("Repeated char : ",count_repeated_character)'''



#problem 170


'''s = input("enter your string: ")


count_beforeM = 0
count_afterM = 0

for ch in s.lower():
    if 'a'<=ch<='z':
        if ch < 'm':
            count_beforeM += 1
        else:
            count_afterM += 1

print("before m :",count_beforeM)
print("after m : ",count_afterM)'''


#problem 171


'''s = input("enter your string: ")

count = 0

for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i]==s[j]:
            count += 1
print("Substring",count)'''


#problem 172


'''s = input("enter your string: ")

vowel = "aeiouAEIOU"
words = s.split()
count_word = 0

for ch in words:
    if ch and ch[0] in vowel:
        count_word += 1
print("word starting with a vowel",count_word)'''



#problem 173


'''s = input("enter your string: ").lower()
words = s.split()
count_word = 0

for ch in words:
    if ch and ch[-1] in "s":
        count_word += 1

print("ending with s: ",count_word)'''


#problem 174


'''s = input("enter your string: ").lower()

rev = ""

for ch in s:
    rev = ch + rev
print(rev)'''


#problem 175


'''s = input("enter your string: ").lower()

rev = ""

for ch in s:
    rev = ch + rev
print(rev)'''


#problem 176


'''s = input("enter your string: ")

word =s.split()
word.reverse()

print(" ".join(word))'''



#problem 177


'''s = input("enter your string: ")

if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''



#problem 178

'''s = input("enter your string: ")
p = input("enter your string: ")

if s==p[::-1]:
    print("Yes,reverse of each other")
else:
    print("no")'''



#problem 179

'''s = input("enter your string: ")
n = len(s)

if n%2==1:
    print("middle character",s[n//2])
else:
    print("Middle character",s[n//2-1],s[n//2])'''



#problem 180 ***



'''s = input("enter your string: ")
mid = len(s)//2

second_half = s[mid:]
print("second half reversed =",second_half[::-1])'''




#problem 181


'''s = input("enter your string: ")

print(s[1:-1])'''



#problem 182


'''s = input("enter your string: ")
vowel = "aeiouAEIOU"
result =""

for ch in s:
    if ch not in vowel:
        result += ch
print("After removing vowel",result)'''



#problem 183


'''s = input("enter your string: ")
result =""

for ch in s:
    if ch != " ":
        result += ch
print("after removing spaces : ",result)'''



#problem 184


'''s = input("enter your string: ")
vowel = "aeiouAEIOU"
result =""

for ch in s:
    if ch  in vowel:
        result += "*"
    else:
        result += ch

print("After removing vowel",result)'''



#problem 185



'''s = input("enter your string: ")
result =""

for ch in s:
    if ch == " ":
        result += "_"
    else:
        result += ch
print("after removing spaces : ",result)'''



#problem 186


'''s = input("enter your string: ")
result = ""

for ch in s:
    if not ch.isdigit():
        result = result + ch
print(result)
'''


#problem 187


'''s = input("enter your string: ")
seen = ''


for ch in s:
    if ch not in seen:
        seen += ch
       

print(seen)
'''


#problem 188

'''s = input("enter your string: ")

res = ""

for i in range(1,len(s)):
    if s[i] != s[i-1]:
        res += s[i]

print(res)'''


#problem 189


'''s = input("enter your string: ")
res =''

for ch in s:
    if ch.islower():
        res += ch.upper()
    elif ch.isupper():
        res += ch.lower()
    else:
        res += ch
print(res)'''



#problem 190


'''s = input("enter your string: ")
words = s.split()


for ch in words:
    print(ch)'''



#problem 191


'''s = input("enter your string: ")
words = s.split()
count = 0


for ch in words:
    if len(ch) % 2 == 0 :
        count += 1
print(count)'''


#problem 192


'''s = input("enter your string: ")
words = s.split()

longest = words[0]

for ch in words:
    if len(ch)>len(longest):
        longest = ch
print("longest word",longest)'''



#problem 193


'''s = input("enter your string: ")
words = s.split()

smallest = words[0]

for ch in words:
    if len(ch)<len(smallest):
        longest = ch
print("smallest word",smallest)'''


#problem 194


'''s = input("enter your string: ")
words = s.split()

words[0],words[-1] = words[-1],words[0]

print("after swapping words "," ".join(words))'''


#problem 195


'''s = input("enter your string: ")
words = s.split()

for w in words:
    if w[0].lower() == w[-1].lower():
        print(w)'''



#problem 196


'''s = input("enter your string: ").lower()
words = s.split()

count = 0

for w in words:
    if 'a' in w :
        count += 1
print(count)'''



#problem 197

'''s = input("enter your string: ").lower()
words = s.title()

print(words)'''



#problem 198

'''s = input("enter your string: ")
print(s.title())'''


#problem 199

'''s = input("enter your string: ").lower()
words = s.split()

print(" ".join(words))'''


             #   MIXED QUESTION FINAL_DESTINATION


    # PROBLEM 201

'''a = 1
N = int(input("enter nth No. "))

for i in range(a,N+1):
    if i%3==0 and i%5==0:
        print("All No btwn 1 to N : ",i)'''


   #problem 202


'''a =int(input("enter your no. "))

sum = 0

while a>0:
    digit = a%10
    sum = sum + digit
    a = a//10

print("Sum of all digits : ",sum)'''


   # problem 203


'''a =int(input("enter your no. "))
temp = a
sum = 0

while a>0:
    digit = a%10
    cube = digit**3
    sum = sum + cube
    a = a//10

    
if temp == sum:
    print("yes , its a armstrong no")
else:
    print("No,its not a armstrong no")'''



# problem 204


'''for a in range(1,1000):
  temp = a
  sum = 0

  while temp>0:
    digit = a%10
    cube = digit**3
    sum = sum + cube
    a = a//10

    
  if temp == sum:
    print(a)'''



# problem 205


'''def factorial(n):
    if n == 0:
        return 1
    return(n* factorial(n-1))
    
    
    
n = int(input("enter your no "))
print(factorial(n))'''



# problem 206



'''a =int(input("enter your no. "))
temp = a
count = 0

while temp>0:
    digit = temp%10
    if digit%2==0:
        count += 1
        temp=temp//10
print(count)'''


#  problem 207


'''a = 1
n = int(input("enter nth term : "))

for i in range(a+1,n+1):
    for j in range(a+1,i):
        if i%j==0:
            break  
        else:
          print(i)'''


# problem 208


'''a =int(input("enter your no. "))

rev = 0

while a>0:
    digit = a%10
    rev = rev*10 + digit
    a = a//10

print(rev)'''


# problem 209

'''a =int(input("enter your no. "))
temp = a

rev = 0

while a>0:
    digit = a%10
    rev = rev*10 + digit
    a = a//10

if temp == rev:
    print("yes,it is palindrome num")
else:
    print("no,it is not palindrome num")'''


# problem 210


'''a =int(input("enter your no. "))


sum_factor = 0

for i in range(1,a):
    if a%i==0:
        sum_factor += i

if sum_factor == a:
    print("it is a perfect num")
else:
    print("it is not a perfect num")'''



    # problem 211


'''a =(input("enter your char. "))

count = 0
vowel = 'aeiouAEIOU'

for ch in a:
    if ch in vowel:
        count += 1
print(count)'''


#problem 212


'''a =(input("enter your char. "))
b =(input("enter your char. "))

if len(a)!=len(b):
    print("not alagram")
else:
    for ch in a:
     if a.count(ch) != b.count(ch):
         print("not alagram")
         break

    else:
     print("alagram")'''


# problem 213

'''a =(input("enter your char. "))
s = a.split()
res = []

for ch in s:
    if len(ch)%2==0:
     res.append(ch[::-1])
    else:
       res.append(ch)
    
print(" ".join(res))'''



#problem 214


'''a =(input("enter your char. ")).lower()
s = a.split()

vowel = {'a':'1','e':'2','i':'3','o':'4','u':'5'}
res = ""

for ch in a:
    if ch in vowel:
        res = res + vowel[ch]
    else:
        res += ch
print(res)'''


# problem 215


'''a =(input("enter your char. ")).lower()
s = a.split()
res =''

for ch in s:
    if s.count(ch)>1 and ch not in res:
       print(ch)
       res = res + ch'''


#problem 216


'''a =(input("enter your char. ")).lower()
s = a.split()

count = 0

for ch in s:
    if (ch[0]) == (ch[-1]):
        count += 1
print(count)'''


#problem 217


'''a =(input("enter your char. "))
s = a.split()

for i in range(len(s)):
    if i%2==1:
        s[i] = s[i].swapcase()
print(" ".join(s))'''



# problem 218


'''a =(input("enter your char. "))
b =(input("enter your char. "))

if len(a) != len(b):
    print("not rotation")
else:
    if b in (a+b):
        print("rotation")
    else:
        print("not rotation")'''


# problem 219



'''a =(input("enter your char. "))
s = a.split()

res = []

for ch in s:
    if ch not in res:
        res.append(ch)
print(" ".join(res))'''
      



#problem 220


'''arr = [10,20,30,40,50,60,70]

print("max",max(arr))
print("min",min(arr))'''


# problem 221

'''arr = [10,20,30,40,50,60,70]


arr.reverse()
print(arr)'''

# problem 222


'''arr = [10,20,30,40,50,50,10,30,60,70]

for x in arr:
    if arr.count(x) == 1:
        print(x)'''


# problem 223  ***


'''arr = [10,0,20,30,0,0,40,50,50,10]

res = []
for x in arr:
    if x != 0 :
     res.append(x)

zero  =  arr.count(0)
res = res + [0]*zero
print(res)'''
        
#problem 224


'''arr = [7,6,43,6,3,2,1,9,8]
arr = list(set(arr))
arr.sort()

print("second largest element",arr[-2])'''


#problem 225


'''arr = [1,2,3,4,5,6,7]

last = arr[-1]

for i in range(len(arr)-1,0,-1):
 arr[i] = arr[i-1]

arr[0] = last

print(arr)'''


#problem 226


'''arr = [1,2,3,4,5,6,7]

total = 0

for i  in range(1,len(arr),2):
 total +=  arr[i]
print(total)'''



# problem 227

'''arr = [1,2,3,4,5,6,7]

k = 10

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == k:
            print(arr[i],arr[j])'''


#problem 228


'''arr = [1,2,3,4,5,6,7]

for i in range(len(arr)):
 for j in range(i,len(arr)):

  print(arr[i:j+1])'''


#problem 229

'''arr = [7,6,3,5,8,2]

asc = True
des = True

for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        asc = False
    else:
        des = False

if asc:
    print("ascending")
elif des:
    print("desending")
else:
    print("not sorted")'''








    

    



    







    





































    




   


    

















       

    




    





    

 

    

























   
    



