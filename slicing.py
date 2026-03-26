Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> b="work until you succeed"
>>> b[0:4]
'work'
>>> b[12:15]
'ou '
>>> b[11:14]
'you'
>>> b[6:11]
'ntil '
>>> b[5:11]
'until '
>>> b[15:]
'succeed'
>>> c="simple is better than complex"
>>> c[16:21]
' than'
>>> a="codegnan it solutions"
>>> a[-9:-1]
'solution'
>>> a[-12:-10]
'it'
>>> a[-20:-10]
'odegnan it'
>>> a[-20:-12]
'odegnan '
>>> a[-21:-10]
'codegnan it'
>>> a[-21:-12]
'codegnan '
>>> a[-21:-11]
'codegnan i'
>>> a[-21:-14]
'codegna'
>>> a[-21:-13]
'codegnan'
>>> b="beautiful is better than ugly"
>>> b[-4:]
'ugly'
>>> b[-16:-10]
'better'
>>> b[-29:-20]
'beautiful'
