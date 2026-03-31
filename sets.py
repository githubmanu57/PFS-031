Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#
#sets{}
a={3,4.5,"java",True,False}
type(a)
<class 'set'>
print(a)
{False, True, 3, 4.5, 'java'}
#add
a={2,4,5,6,7}
a.add(50)
a
{2, 50, 4, 5, 6, 7}
#subset
a={4,5,6,78,3,6}
b={3,2,4,5,6,7,9}
a.issubset(b)
False
a={4,5,6,78,3,6}
b={3,2,4,5,6,7,9}
b.issubset(a)
SyntaxError: multiple statements found while compiling a single statement
a
{3, 4, 5, 6, 78}
b.issubset(a)
False
a={1,2,3,4,5,6,7,}
b={1,2,3,4}
a.issubset(a)
True
a.issuperset(b)
True
#union
>>> a={3,4,5,6,7,8}
>>> b={3,4,5,6,7,8,9}
>>> a.union(b)
{3, 4, 5, 6, 7, 8, 9}
>>> #intersection
>>> a={3,4,5,6,7,8,9}
>>> b={3,4,5,6,7,8}
>>> a.intersection(b)
{3, 4, 5, 6, 7, 8}
>>> #difference
>>> a={1,3,4,5,6}
>>> b={4,6,7,8,9}
>>> a.difference(b)
{1, 3, 5}
>>> b.difference(a)
{8, 9, 7}
>>> #update
>>> a={1,3,4,5,6}
... b={4,6,7,8,9}
SyntaxError: multiple statements found while compiling a single statement
>>> a={1,3,4,5,6}
>>> b={4,6,7,8,9}
>>> a.update(b)
>>> a
{1, 3, 4, 5, 6, 7, 8, 9}
>>> b
{4, 6, 7, 8, 9}
>>> b.update(a)
>>> b
{1, 3, 4, 5, 6, 7, 8, 9}
>>> #symmetric_difference
>>> a={4,5,6,7,5,6,7}
>>> b={1,3,4,5,6,7}
>>> a.symmetric_difference(b)
{1, 3}
>>> b.symmetric_difference(a)
{1, 3}
>>> b
{1, 3, 4, 5, 6, 7}
>>> #difference_update
>>> a={2,4,6,12,23,12,14}
>>> b={2,4,12,3,4,5,6,7}
>>> a.difference_update(a)
>>> a.difference_update(b)
>>> b
{2, 3, 4, 5, 6, 7, 12}
