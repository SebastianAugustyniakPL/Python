Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
atext.upper('')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    atext.upper('')
NameError: name 'atext' is not defined. Did you mean: 'anext'?
quote.upper()
'A GOOD PROGRAMMER IS SOMEONE WHO ALWAYS LOOKS BOTH WAYS BEFORE CROSSING A ONE-WAY STREET'
quote.lower()
'a good programmer is someone who always looks both ways before crossing a one-way street'
quote.find('5')
-1
quote.find('steer', '5')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    quote.find('steer', '5')
TypeError: slice indices must be integers or None or have an __index__ method
quote.find('steet', '5')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    quote.find('steet', '5')
TypeError: slice indices must be integers or None or have an __index__ method
quote.endswith('street')
True
quote.isupper()
False
quote.upper().isupper()
True
quote.find('50')
-1

quote.find('one')
25
quote.replace('one','1')
'A good programmer is some1 who always looks both ways before crossing a 1-way street'
quote.replace('one','1').replace('both','2')
'A good programmer is some1 who always looks 2 ways before crossing a 1-way street'
quote.split(' ')
['A', 'good', 'programmer', 'is', 'someone', 'who', 'always', 'looks', 'both', 'ways', 'before', 'crossing', 'a', 'one-way', 'street']
quote.isdigit()
False
quote.isdecimal()
False
quote.isalpha()
False
quote.isalnum()
False
