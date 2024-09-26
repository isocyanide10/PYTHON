a=str(input("Enter the string : "))
print(a.upper())
print(a.lower())
print(a.replace("Nirmal","Prem"))
print(a.split())
print(len(a))

# TABLE

b=int(input("Enter the table you want : "))
print("Table of ",b)
for x in  range(1,12):
    print(b,"*",x,"=",b*x)

# IF-ELSE
a=int(input("Enter the value "))
if(a==0):
    print("Number is zero ")
elif(a==-1):
    print("Number is negative ")
elif(a==2):
    print("Number is positive  ")
else :
    print("Enter valid real numberr\"")
    
    


