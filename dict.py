Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={"name":"pooja","year":2026,"month":3}
>>> print(a)
{'name': 'pooja', 'year': 2026, 'month': 3}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['name', 'year', 'month'])
>>> a.values()
dict_values(['pooja', 2026, 3])
a
>>> a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 3)])
>>> a={"name":"pooja","year":2026,"month":3}
... a.update({"date":31}
...          
SyntaxError: multiple statements found while compiling a single statement
>>> a.update({"date":31})
...          
>>> a
...          
{'name': 'pooja', 'year': 2026, 'month': 3, 'date': 31}
>>> a.update({"city":"vij","time":10})
...          
>>> a
...          
{'name': 'pooja', 'year': 2026, 'month': 3, 'date': 31, 'city': 'vij', 'time': 10}
>>> a={"mail":"manu@11"}
...          
>>> a.setdefault("name",",manu")
...          
',manu'
>>> a
...          
{'mail': 'manu@11', 'name': ',manu'}
>>> a.pop()
...          
Traceback (most recent call last):
... 
  File "<pyshell#14>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("mail")
...          
'manu@11'
>>> a
         
{'name': ',manu'}
d = {"a": 1, "b": 2}
         
d.get("a")
         
1
d.popitem()
         
('b', 2)
d
         
{'a': 1}
a={"idno":[2,4,5,6],"name":["manu","krish","ameeer"]}
         
print(a)
         
{'idno': [2, 4, 5, 6], 'name': ['manu', 'krish', 'ameeer']}
a
         
{'idno': [2, 4, 5, 6], 'name': ['manu', 'krish', 'ameeer']}
type(a)
         
<class 'dict'>
a={"name":"pooja","city":"vij","name":"pooja"}
         
print(a)
         
{'name': 'pooja', 'city': 'vij'}
a={"name":"pooja","city":"vij","name":"poojaa"}
         
print(a)
         
{'name': 'poojaa', 'city': 'vij'}
a={"name":"pooja","city":"vij","name1":"poojaa"}
         
print(a)
         
{'name': 'pooja', 'city': 'vij', 'name1': 'poojaa'}
