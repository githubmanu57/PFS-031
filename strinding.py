Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #striding
>>> 
>>> a="cloud computing"
>>> a[::4]
'cdmi'
>>> a[::2]
'codcmuig'
>>> a[::6]
'cci'
>>> a[5:]
' computing'
>>> a[3:11]
'ud compu'
>>> a[:9]
'cloud com'
>>> b="machine learning"
>>> b[2:12:4]
'cea'
>>> b[3:15:6]
'he'
>>> a[1:14:3]
'ldoun'
>>> b[1:14:3]
'ai ai'
>>> a="python course"
>>> a[-1:-9:-2]
'ero '
>>> a[-3:-12:-4]
'r t'
