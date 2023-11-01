while True:
 n = int(input("enter a number bigger than 0  "))
 if n<=0: 
    
    continue
  
 elif n==1:
    print ("there is no prime number before 1")
 elif n==2:
    print ("there is no prime number before 2 and 2 is a prime number")     

 else:

  TAB=[]

  for i in range(n,2, -1):
        if i%2 !=0 :
            TAB.append(i)
  print(TAB)
