a = int(input("enter the number"))
b= int(input("enter the anothe number "))
print(a+b) #addtion 
print(a-b) #subtraction
print(a*b) #mutlipication
print(a/b) #division
print(a//b) #floor division
print(a%b)  #modulo division
print(a**b) #power

# relational operators 
print("a==b",a==b) # equal to 
print("a!b ",a!=b)
print("a>b",a>b)
print("a<b",a<b)
print("a>=b",a>=b)
print("a<=b",a<=b)

#assignment operators 
# a = "vishwesh"
# print(a)
a =6
a+=2
print("a+=2 :",a)
a -=3
print("a-=3",a)
a*=4
print("a*=4",a)
a/=2
print("a/=2",a)
a%=3
print("a%=3",a)
a**=2
print("a**2= ",a)
a//=2
print("a//=2",a)
a=int(a)
a&=3
print("a&=3",a)
a|=2
print("a|=2",a)
a^=2
print("a^=2",a)
a>>=2
print("a>>=2",a)
a<<=3
print("a<<=3",a)
#Logical operators
a= True
b= False
print("a and b:",a and b)
print("a or b:",a  or b)
print("not a :",not a)
#bitwise operators
a =10
b=4
print("a&b :",a&b)
print("a|b: ",a|b)
print("a^b: ",a^b)
print("negation  a :",~a)
print("a>>2 :",a>>2)
print("a<<2: ",a<<2)
#tenary operator
min_valu = a if(a<b)else b
print(min_valu)
#membership opteratos
str = "vihwesha"
print("a  in str ",'a' in str )
print("r not in str: ",'r' not in str)

#identity operators
a= [1,2,3]
b=a
c=[1,2,3]
print("a is b :",a is b)
print(" a is not c :",a is not  c)





