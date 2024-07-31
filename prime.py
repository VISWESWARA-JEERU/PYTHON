print("numbers will be diplayed within in the interval ")
a = int(input("enter the numbet that is starting element of prime number :"))
b = int (input("enter the number that is ending element of prime number :"))
for i in range(a,b):
    if(i>1):
      for j in range(2,int(i/2)+1):
        if(i%j)== 0:
          break
      else:
       print(i)    
         
  