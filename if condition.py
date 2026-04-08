#conditiona
#if  conditions by
#camparision >,<,<=,>=,==,!=

'''a=4
b=8
if a<b:
    print("true")'''


'''a=4
b=8
if a>b:
    print("true")'''

'''a=4
b=8
if a>=b:
    print("true")'''

'''a=4
b=8
if a<=b:
    print("true")'''

'''a=4
b=8
if a!=b:
    print("true")'''

'''a=4
b=8
if a==b:
    print("true")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a>30:
    print("false")'''

'''a="python"
if a=="python":
    print("true")'''

#if condition by using logical operator
#and , or , not
'''a=3
b=8
if a<b and b>a:
    print("true")'''

'''a=3
b=8
if a<=b and b>=a:
    print("true")'''

'''a=3
b=8
if a!=b and b==a:
    print("true")'''

'''a=3
b=8
if a<b or b>a:
    print("true")'''

'''a=11
b=8
if a<b or b>a:
    print("true")'''

'''a=3
b=8
if a<=b or b>=a:
    print("true")'''

'''a=3
b=8
if a!=b or b==a:
    print("true")'''

'''a=12
b=15
if not a<b:
    print("less")'''

'''a=12
b=15
if not a>b:
    print("less")'''


'''a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("less")'''

'''a=int(input("a value"))
if a!=9 or a==6:
    print("true")'''

''''a=input("enter the data")
if a=="python" or a=="java":
    print("true")'''''



#if condition by using identify operators
#is ,is not


'''a=8
if type(a) is int:
    print("it is int")'''

'''a=8
if type(a) is not int:
    print("it is int")'''


'''a=int(input("a value"))
if type(a) is int:
    print("true")'''


'''a=8.5
if type(a) is float:
    print("it is float")'''

'''a=8.4
if type(a) is not float:
    print("it is float")'''


'''a=float(input("a value"))
if type(a) is float:
    print("true")'''


#if condition by using memership operators
#in , not in
'''a=[1,3,4,5,6,7,8,]
if 10 in a:
    print("true")'''

'''a=[1,3,4,5,6,7,8,]
if 10 not in a:
    print("true")'''

''''a=[1,3,4,5,6,7,8,]
b=int(input("value"))
if b in a:
    print("true")'''

#if-else conditions by using comparision

'''a=4
b=8
if a<b:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if a>b:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if a>=b:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if a<=b:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if a<b and b>a:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if a<b or b<a:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if a<b and b<a:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if not b<a:
    print("less")
else:
    print("true")'''


'''a=4
b=8
if a<b is b<a:
    print("less")
else:
    print("true")'''

'''a=4
b=8
if a<b is not b<a:
    print("less")
else:
    print("true")'''


'''a=4
b=8
if a<b is not b<a:
    print("less")
else:
    print("true")'''


'''a=[2,3,4,5,6,7]
b=2
if b in a:
    print("less")
else:
    print("true")'''


'''a=[2,3,4,5,6,7]
b=2
if b not in a:
    print("less")
else:
    print("true")'''

#if-elif condition by using comparision
'''a=2
b=4
if a>b:
    print("less")
elif b>a:
    print("greater")'''

'''a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greater")'''

'''a=2
b=4
if a>b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''

'''a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''


#if-elif-else condition

'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("true")
else:
    print("true")'''

'''a=2
b=4
if a<=b:
    print("less")
elif b>=a:
    print("greater")
else:
    print("true")'''


'''a=2
b=4
if a<b and a>b:
    print("less")
elif b>a and b>a:
    print("greater")
else:
    print("true")'''


''''a=2
b=4
if a<b or a>b:
    print("less")
elif b>a or b>a:
    print("greater")
else:
    print("true")'''


'''a=2
b=4
if not a>b:
    print("less")
elif  not b>a:
    print("greater")
else:
    print("true")'''

#multiple if  conditions

'''a=8
b=12
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=8
b=12
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''



#nested-if  conditions

'''a=10
b=20
if a<b:
    print("less")
    if b>a:
        print("graeter")'''


'''a=10
b=20
if a>=b:
    print("less")
    if b>a:
        print("graeter")'''

'''a=10
b=20
if a<=b:
    print("less")
    if b>=a:
        print("graeter")'''

'''a=10
b=20
if a<b:
    print("less")
    if b>a:
        print("graeter")
    else:
        print("false")'''

'''a=10
b=20
if a==b:
    print("less")
    if b>a:
        print("graeter")
    else:
        print("false")'''

'''a=10
b=20
if a==b:
    print("less")
    if b>a:
        print("graeter")
else:
     print("false")'''


'''a=10
b=20
if a==b:
    print("less")
    if b>a:
        print("graeter")
    else:
        print("false")        
else:
     print("false")'''


'''a=10
b=20
if a!=b:
    print("less")
    if b>a:
        print("graeter")
    else:
        print("false")        
else:
     print("false")'''

#swapping of two variables
'''a=10
b=20
a,b=b,a
print(a)
print(b)'''

'''a=10
b=20
c=a
a=b
b=c
print(a)
print(b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d"%(a,b))'''
#float

'''a=10.5
b=20.9
a,b=b,a
print(a)
print(b)'''


'''a=10.5
b=20.9
c=a
a=b
b=c
print(a)
print(b)'''


'''a=10.5
b=20.9
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''



a=10.5
b=20.9
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f"%(a,b))



    
    
    
    
    
    
    
    


    
    




    








    
    



    

    
    


    
    

    
    
    
    
      
    
    


    




    
