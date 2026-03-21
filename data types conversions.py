Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #data types conversions
>>> int(3)
3
>>> int(4.6)
4
>>> int('str')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int('str')
ValueError: invalid literal for int() with base 10: 'str'
>>> int(2+4j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(2+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> 
>>> 

>>> 
>>> #float
>>> float(4)
4.0
>>> float(4,6)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(4,6)
TypeError: float expected at most 1 argument, got 2
>>> float(6.9)
6.9
>>> float('str')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float('str')
ValueError: could not convert string to float: 'str'
>>> float(3+4j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(3+4j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0


#string
str(7)
'7'
str(7.7)
'7.7'
str('manu')
'manu'
str(+5j)
'5j'
KeyboardInterrupt
str(True)
'True'


#complex

complex(77)
(77+0j)
complex(7.7)
(7.7+0j)
complex('str')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex('str')
ValueError: complex() arg is a malformed string
complex(2+3j)
(2+3j)
complex(True)
(1+0j)
complex(False)
0j


#boolen

bool(4)
True
bool(8.8)
True
bool('str')
True
bool(3+3j)
True
bool(True)
True
bool(False)
False
