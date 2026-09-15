Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x='computer'
x[1:4]
'omp'
x[1:6:2]
'opt'
x[-2]
'e'
x[:-2]
'comput'
x[::-2]
'rtpo'
x[:1]
'c'
x[::1]
'computer'
x[::-1]
'retupmoc'
x[-2:]
'er'
x[-2::]
'er'
>>> x[1:7:2]
'opt'
>>> x[1:8:2]
'optr'
>>> a='input'
>>> print(a)
input
>>> a=input("enter the name=")
enter the name=vala lakshyadeepsinh
>>> print(a)
vala lakshyadeepsinh
>>> a
'vala lakshyadeepsinh'
>>> 
>>> 12=int(input("enter a number"))
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> add=num+1
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    add=num+1
NameError: name 'num' is not defined. Did you mean: 'sum'?
>>> num=int(input("enter a number"))
enter a number12
>>> add=num+1
>>> add
13
