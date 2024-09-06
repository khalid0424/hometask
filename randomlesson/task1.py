import random

def gues(gues_number, b =5):  
  
  a =int(input("javob navis -> "))
  
  
  for n in range(5, b+1):
   a = int(input())
   
   if a < gues_number:
    print("-> to low")
    gues(gues_number, n)
    
   elif a >  gues_number:
    print("-> to high")
    gues(gues_number, n)
   elif a == gues_number +1:
    print("->too closer")
    gues(gues_number, n)
   elif a == gues_number -1:
    print("->too closer")
    gues(gues_number, n)
   else :
    print(f"-> tabrik {n} drust")
    

gues_number =  random.randrange(1 , 100)
print("salomalek")
print("hello ")
gues(gues_number)