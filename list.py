Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list

a=[4,6.7,"pooja",5+4j,True,False]
print(a)
[4, 6.7, 'pooja', (5+4j), True, False]
type(a)
<class 'list'>

#append
a=["python","html
   
SyntaxError: unterminated string literal (detected at line 1)
a=["python","html","java","css"]
   
a.append("js")
   

a
   
['python', 'html', 'java', 'css', 'js']
a.append("sript","java")
   
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("sript","java")
TypeError: list.append() takes exactly one argument (2 given)

#extend
   
a=["apple","banana","grapes"]
   
a.extend(["mango","kiwi"])
   
a
   
['apple', 'banana', 'grapes', 'mango', 'kiwi']
#insert
   
a.insert(2,"berry")
   
a
   
['apple', 'banana', 'berry', 'grapes', 'mango', 'kiwi']
#index
   
a.index("banana")
   
1
#sort
   
a=["red","blue","green"]
   
a.sort()
   
a
   
['blue', 'green', 'red']
b=[3,5,6,7,93,5,6,23,7]
   
b.sort()
   
b
   
[3, 5, 5, 6, 6, 7, 7, 23, 93]
#reverse
   
b.reverse()
   
b
   
[93, 23, 7, 7, 6, 6, 5, 5, 3]
#pop
   
a=["html","js","bs","css"]
   
a.pop()
   
'css'
a
   
['html', 'js', 'bs']
a.pop("js")
   
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.pop("js")
TypeError: 'str' object cannot be interpreted as an integer
#remove
   
a.remove("bs")
   
a
   
['html', 'js']
a=["pooja","courese","codegnan"]
   
>>> a.clear()
...    
>>> a
...    
[]
>>> a=[]
...    
>>> a.append("js")
...    
>>> a
...    
['js']
>>> #length
...    
>>> a=["js","html","css"]
...    
>>> len(a)
...    
3
>>> #count
...    
>>> a.count()
...    
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count("css")
...    
1
>>> #tuple()
...    
>>> a=(5,6.6,"python",True,False)
...    
>>> type(a)
...    
<class 'tuple'>
>>> a.count(True)
...    
1
>>> len(a)
...    
5
>>> a.index("python")
...    
2
