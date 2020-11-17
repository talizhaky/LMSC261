Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def x():
	print("+ - - - - + - - - - +")

	
>>> def y():
	print("|         |         |")

	
>>> def print_square():
	x()
	for in in range (4):
		
SyntaxError: invalid syntax
>>> def print_square():
	for i in range (2):
		x()
	for i in range (4):
		y()

		
>>> print_square()
+ - - - - + - - - - +
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
>>> def print_square():
	for i in range (2):
		x()
		for i in range (4):
			y()
	x()

	
>>> print_squares()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print_squares()
NameError: name 'print_squares' is not defined
>>> print_square()
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
>>> 