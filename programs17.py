a=input("enter any string:")
l=a.split()
#for i in l:
   #lenth=len(l)
print(l)
print("palidrome string is {}",format(a))
if(a==a[::-1]):
    print("this is a palidrome")
else:
    print("this is not a palidrome")
