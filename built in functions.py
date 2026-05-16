#built-in functions
#fromkeys

'''a="codegnan"
print(list(a))
print(tuple(a))
print((set))
#print(dict(a))

b=dict.fromkeys(a)
print(b)

b==dict.fromkeys(a,"pooja")
print(a)'''

#eval()
''''while True:
    a=int(input("s value"))
    b=int(input("b value"))
    print(a+b)

while True:
    a=float(input("s value"))
    b=float(input("b value"))
    print(a+b)

    
while True:
    a=eval(input("s value"))
    b=eval(input("b value"))
    print(a+b)

#zip() -> we can combine collection into one collection

a=[10,20,30,40,50]

names = ["dahtri","meghana","indhu","ashika"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

#enumerate
#we can give counter to the collection
names=["praveen","manohar","jash","krishna","amar"]
for i in range(len(names)):
    print(i,names[i])


b=list(enumerate(names))
print(b)

b=dict(enumerate(names,100))
print(b)

b=tuple(enumerate(names,100))
print(b)

b=set(enumerate(names,100))
print(b)'''


#anonymous functons is name less funtions we use lamda()
#lamda()


'''def cal():
    x=5
    c=2*x+5
    print(c)
cal()    

#syntax
#a=lambda arg:expr

a=lambda x : 2*x+5
print(a(5))'''


'''a=lambda x,y:x*y
print(a(4,6))'''


'''a=lambda x:x.upper()
print(a("codegnan"))

a=lambda x:x.title()
print(a("python course"))'''


'''a=input()
b=lambda x:x.upper()
print(b(a))'''

'''a=input()
b=lambda x:x.title()
print(b(a))'''

'''fname="manohar"
lname="reddy"
a=lambda fname,lname:fname+" "+lname
print(a(fname,lname))'''



for i in range(65,91):
    print(chr(i),end=" ")
    

for i in range(97,123):
    print(chr(i),end=" ")


name=input("enter the name")
for i in name:
    print(i,"-",ord(i))


    





