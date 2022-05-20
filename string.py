Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
atext="This i a text."
atext.endswith('ext')
False

KeyboardInterrupt
atext.endswith('ext.')
True

KeyboardInterrupt
Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

atext.find('is')
2

 
atext.find('is',3)
-1
atext.replace('a',4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    atext.replace('a',4)
TypeError: replace() argument 2 must be str, not int
atext.replace('a',"4")
'This i 4 text.'
atext.replace('a',"4").replace('i','1')
'Th1s 1 4 text.'
atext.split(' ')
['This', 'i', 'a', 'text.']
somethingLikeNumber.isdigit()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    somethingLikeNumber.isdigit()
NameError: name 'somethingLikeNumber' is not defined
