Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()

a="twinkle twinkle little it star"
count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count()
TypeError: count expected at least 1 argument, got 0
a.count(twinkle)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.count(twinkle)
NameError: name 'twinkle' is not defined
a.count("twinkle")
2
a.coutn("t")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.coutn("t")
AttributeError: 'str' object has no attribute 'coutn'. Did you mean: 'count'?
a.count("t")
6
a.count(" ")
4


#find a string

a="codw"
a.find("d")
2
a.find("e")
-1
a.find("w")
3

#escape sequences

#\n-> new line
#\t-> tab space
a="name\nmobiileno\tmailid\ncity
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobiileno\tmailid\ncity"
print(a)
name
mobiileno	mailid
city
a="name:manohar\nmobiileno:908834586\tmailid:manoar@gmIL.COM\ncity:VJA"
print(a)
name:manohar
mobiileno:908834586	mailid:manoar@gmIL.COM
city:VJA


#replace

a="wait until you secceed'
SyntaxError: unterminated string literal (detected at line 1)
a="wait until you secceed"
a.replace("wait","work")
'work until you secceed'
a="work work until you secceed"
a.replace("work","wait")
'wait wait until you secceed'
a="work work until you secceed"
a.replace("work","wait",1)
'wait work until you secceed'
'wait work until you secceed'
'wait work until you secceed'

#upper
a="hello"
a.upper()
'HELLO'
'HELLO'
'HELLO'
b="HII"
a.lower()
'hello'
a="manu reddy'
SyntaxError: unterminated string literal (detected at line 1)
a="manu reddy"
a.capitalize()
'Manu reddy'
a="manu reddy"
a.title()
'Manu Reddy'
a="pytohn"
a.islower()
True
a.isupper()
False
a.isdigits()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.isdigits()
AttributeError: 'str' object has no attribute 'isdigits'. Did you mean: 'isdigit'?
a.isdigit()
False
a.isalpha()
True

a.startswith("p")
True
a.endswith("n")
True
b="3452"
b.isdigit()
True
a="manohar"
a.isalnum()
True
b="manu12314"
b.isalnum()
True
c="manu@79823"
c.isalnum()
False
#strip
a="    manu   "
a.strip()
'manu'
a.lsstrip()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.lsstrip()
AttributeError: 'str' object has no attribute 'lsstrip'. Did you mean: 'lstrip'?
a.lstrip()
'manu   '
a.rstrip()
'    manu'
#split

a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b=" i am learning python course"
b.split()
['i', 'am', 'learning', 'python', 'course']


#join
a="html","css","js","bs"
"".join(a)
'htmlcssjsbs'
" "join(a)
SyntaxError: invalid syntax
" ".join(a)
'html css js bs'
"k".join(a)
'htmlkcsskjskbs'


#concatenation

a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="manu"
lname="reddy"
print(fname+lnmae)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print(fname+lnmae)
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
print(fname+lname)
manureddy
print(fname.title()+lnmae.title())
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    print(fname.title()+lnmae.title())
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
KeyboardInterrupt
print(fname.title()+" "+lnmae.title())
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print(fname.title()+" "+lnmae.title())
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
print((fname.title()+lnmae.title())

 print(fname.title()+lname.title())
      
SyntaxError: '(' was never closed
print((fname+" "+lnmae).title())
      
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    print((fname+" "+lnmae).title())
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
print((fname+" "+lname).title())
      
Manu Reddy
#formatting
      

a=8
      
b=5
      
print(a+b)
      
13
print("sum of a+b is",a+b)
      
sum of a+b is 13
city="vija"
      
print("city",city)
      
city vija
name="manu"
      
print("my name is",name)
      
my name is manu
#format
      
a="motu:
      
SyntaxError: unterminated string literal (detected at line 1)
a="motu"
      
b="patulu"
      
print("hello {}{}".format(a,b))
...       
hello motupatulu
>>> rint("hello {} hello {}".format(a,b))
...       
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    rint("hello {} hello {}".format(a,b))
NameError: name 'rint' is not defined. Did you mean: 'print'?
>>> print("hello {} hello {}".format(a,b))
...       
hello motu hello patulu
>>> print("hello {}\n hello{}".format(a,b))
...       
hello motu
 hellopatulu
>>> print("hello {}\nhello{}".format(a,b))
...       
hello motu
hellopatulu
>>> #fstring
...       
>>> a="chota"
...       
>>> b="bheem"
...       
>>> print(f"hello {a} {b}")
...       
hello chota bheem
>>> print(f"hello {a}{b}")
...       
hello chotabheem
>>> print(f"hello {a} hello {b}")
...       
hello chota hello bheem
>>> a=6
...       
>>> b=4
...       
>>> c=a*b
...       
>>> print(f"product of {c}")
...       
product of 24
>>> print("product is {}".format(a*b))
...       
product is 24
