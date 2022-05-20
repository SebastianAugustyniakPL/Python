Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5*3
15
five = 5
three = 3
five * three
15
type(five)
<class 'int'>
type(five * three)
<class 'int'>
five/three
1.6666666666666667
type(five/three)
<class 'float'>
import sys
sys.maxsize
9223372036854775807
veryBigValue = 9999999999999999999999999999999999
veryBigValue
9999999999999999999999999999999999
veryBigValue + 1
10000000000000000000000000000000000
type(veryBigValue)
<class 'int'>
(veryBigValue+1)/2
5e+33
type(veryBigValue+1)/2)
SyntaxError: unmatched ')'
type((veryBigValue+1)/2))
SyntaxError: unmatched ')'
type((veryBigValue+1)/2)
<class 'float'>
five//three
1
five % three
2
float('inf')
inf
float('inf') >9999999999999999999999999999999999999999999
True
-float('inf')
-inf
name = "Sebastian"
age = "21"
dayslnYear = "365"
message = "%s is %d years old, so is about %d days old"
age = 21
dayslnYear = 365
print(message.format ("%s is %d years old, so is about %d days old"))
%s is %d years old, so is about %d days old
print(message % (name,age,age*dayslnYear))
Sebastian is 21 years old, so is about 7665 days old
Sebastian is 21 years old, so is about 7665 days old
SyntaxError: invalid syntax
1234567890//1234567890
1
1234567890//12345
100005
