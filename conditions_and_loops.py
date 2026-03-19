Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 4384
>>> b = 9046
>>> result = 0
>>> for i in ramge (a,b+1):
...     if i % 2 ==1:
...         result +=i
... 
...         
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for i in ramge (a,b+1):
NameError: name 'ramge' is not defined. Did you mean: 'range'?
>>> [DEBUG ON]
>>> [DEBUG OFF]
>>> a = 4384
... b = 9046
... result = 0
... for i in range (a,b+1):
...     if i % 2 ==1:
...         result +=i
...         
SyntaxError: multiple statements found while compiling a single statement
>>> result = 0
... for i in range (a,b+1):
...     if i % 2 ==1:
...         result +=i
...         
SyntaxError: multiple statements found while compiling a single statement
>>> for i in range (a,b+1):
...     if i % 2 ==1:
...         result +=i
... 
...         
>>> print (result)
15652665
