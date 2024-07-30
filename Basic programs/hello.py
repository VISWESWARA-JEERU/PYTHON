#arithematic operaters
a = int(input("enter a number "))
b = int (input(" enter a another number "))
print(a+b)# additon
print(a-b)#subtraction
print(a*b)#multiplication
print(a/b)#division
print(a%b)#modulo operator

#relational operators 

c= int(input("enter a value : "))
d = int(input("enter a value :"))
print(a>b)   #greaterthan
print(a>=b)  #greaqterthan equal to
print(a<b)   #lessthan
print(a<=b)  #lessthan equal to
print(a==b)  #equal to
print(a!=b)  #Not equal to

#logical operators 

i = int(input("enter a 1st number :"))
j = int(input("etner a 2nd number :"))
if(i>j and i!=j):   # logical "and" operator 
    print("\ni is greater than j ")
elif(i<j or i!=j):  # logical "or" operator
    print("\ni is smller than j")
else:
    print("i equal to j")
  





