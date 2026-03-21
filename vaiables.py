Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> print(a)
10
>>> a=3
>>> b=7
>>> print(a+b)
10
>>> a2=7
>>> print(a2)
7
>>> name="manu"
>>> print(name)
manu
>>> if=45
SyntaxError: invalid syntax
>>> else=7
SyntaxError: invalid syntax
>>> a,b=1,4
>>> print(a+b)
5
>>> 3=4
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a=1;;b=7
SyntaxError: invalid syntax
>>> print(a+b)
5
>>> a,b="python","course"
>>> print(a+b)
pythoncourse
>>> print(a+" "+b)
python course
>>> fname=manu
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    fname=manu
NameError: name 'manu' is not defined
>>> fname="manu"
>>> lname="veeram"
>>> print(fname+lname)
manuveeram
>>> print(fname+" "+lnmae)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(fname+" "+lnmae)
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
print(fname+" "+lname)
manu veeram
first_name="manu"
last_name="reddy"
print(first_name+last_name)
manureddy
_a=100
print(_a)
100
_=40
print(_)
40
 a=50
 
SyntaxError: unexpected indent
a=4
print(a)
4
del a
a
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'a2'?
