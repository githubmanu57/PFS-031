#functions
'''a=10
b=20
print("the sum iS",a+b)
print("the difference iS",a-b)
print("te mul iS",a*b)
a=1000
b=2000
print("the sum iS",a+b)
print("the difference iS",a-b)
print("the mul iS",a*b)'''

'''def calculate(a,b):
    print("the sum iS",a+b)
    print("the difference iS",a-b)
    print("the mul iS",a*b)
calculate(3,6)
calculate(100,2000)'''


'''def calculate(a,b):
    print("the div iS",a%b)
    print("the modules iS",a//b)
    print("the interger div iS",a/b)
    print("the power iS",a**b)
calculate(3,6)
calculate(10,20)'''

'''def add(a,b):
    print(a+b)
add(4,5)'''

'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    cal()'''

'''while True:
    def fullname():
        fname=input("first name")
        lname=input("last name")
        print((fname+" "+lname).title())
    fullname()'''

#print just show the human resourse and return is used to turminate the fun and gives back val from the fun

#print v/s return

'''def mul(a,b):
    print(a*b)
mul(4,6)'''

'''def mul(a,b):
    return a*b
print(mul(3,7))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(8,8))'''

def cal():
    a=int(input("a vlaue"))
    b=int(input("b value"))
    
    print("options:")
    print("1 add")
    print("2 sub")
    print("3 mul")
choice=input("select one option:")
if choice == "1":
    print(a+b)
elif choice == "2":
    print(a-b)
elif choice == "3":
    print(a*b)
cal()

      



    









