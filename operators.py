Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=3
b=4
print(a+b)
7
print(a-b)
-1
print(a*b)
12
print(a//b)
0
print(a**b)
81
print(a%b)
3


#assignment

a=3
b=4
print(a+b)
7
print(a+=)
SyntaxError: invalid syntax



















print(a+=b)
SyntaxError: invalid syntax
a+=b
a
7
print(a)
7
a-=b
a
3
a*=b
a
12
a//=b
a
3
a/=b
a
0.75
a%=b
a
0.75
a+=b
b
4
a-=b
b
4
a*=b
b
4
a//=b
b
4
a/=b
b
4
a**=b
b
4
a%=b
b
4
#camparision
a=3
b=5
a>b
False
a<b
True
a<=b
True
a>=b
False
a!=b
True
#logical
a=4
b=2
a>b and b>a
False
a<b and b>a
False
a>b and b<a
True
a>=b and b>=a
False
a<=b and b<=a
False
a!=b and a==b
False
a>b or b>a
True
a<b or b<a
True
a<=b or b>=a
False
#identify

a=5
if type(a) is int:
    print("true")

    
true
if type(a) is not int:
    print("true")

    
a=7.5
if type(a) is not float:
    print("true")

    
if type(a) is float:
    print("true")

    
true

#membership
a=4,6,7,89,
print(4 in a)
True
if 4 in a:
    print(a)

    
(4, 6, 7, 89)
>>> print(20)
20
>>> if 6 in a:
...     print(6)
... 
...     
6
>>> if 50 not in a:
...     print(50)
... 
...     
50
>>> #bitwise
>>> a=3
>>> b=4
>>> a&b
0
>>> a=5b=8
SyntaxError: invalid decimal literal
>>> a=8
>>> b=5
>>> a&b
0
>>> a~b
SyntaxError: invalid syntax
>>> a^~b
-14
>>> a|b
13
>>> a=7
>>> b=3
>>> a|b
7
>>> a=5
>>> b=9
>>> a|b
13
>>> a=4
>>> b=8
>>> a^b
12
>>> a>>b
0
>>> a=4
>>> a>>3
0
