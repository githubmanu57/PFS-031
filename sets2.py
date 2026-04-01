Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6,7,]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6,7}
SyntaxError: multiple statements found while compiling a single statement
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6,7}
a.difference_update(b)
a
{8, 9}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7}

a={3,4,5,6,7,8,9,10,11,12}
b={4,5,6,7,8,9,10,11,12,13,14}
a.symmetric_difference_update(a)
a
set()
KeyboardInterrupt
b={1,2,3,4,5,6,7
   a.symmetric_difference_update(b)
   
SyntaxError: '{' was never closed
a={3,4,5,6,7,8,9,10,11,12}
   
b={4,5,6,7,8,9,10,11,12,13,14}
   
a.symmetric_difference_update(b)
   
a
   
{3, 13, 14}
b.symmetric_difference_update(a)
   
b
...    
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
>>> a={2,3,4,5,6,7}
...    
>>> b={1,2,3,4,5,6,8}
...    
>>> a.copy()
...    
{2, 3, 4, 5, 6, 7}
>>> a
...    
{2, 3, 4, 5, 6, 7}
>>> a.clear()
...    
>>> a
...    
set()
>>> a={3,4,5,6,7,8,9}
...    
>>> a.pop()
...    
3
>>> a.remove(4)
...    
>>> a
...    
{5, 6, 7, 8, 9}
>>> #isdisjoint()
...    
>>> a={2,3,4,5,6,7,8}
...    
>>> a={7,8,9,10,11,12,13}
...    
>>> a.isdisjoint(b)
...    
False
>>> len(a)
...    
7
>>> a.count(4)
...    
Traceback (most recent call last):
... 
  File "<pyshell#38>", line 1, in <module>
    a.count(4)
AttributeError: 'set' object has no attribute 'count'
