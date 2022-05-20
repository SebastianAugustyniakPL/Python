Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
message1 = 'Processing file %s'
print(message1 % ('file_1.txt'))
Processing file file_1.txt
message2 = 'File %s has size %d KB'
print(message2 % ('file1.txt' ,100))
File file1.txt has size 100 KB
print(message2 % ('file1.txt' ,100))
File file1.txt has size 100 KB
message3 = 'File %20s has sieze %10d KB'
print(message3 % ('file1.txt', 100))
File            file1.txt has sieze        100 KB
message4 = 'Processing file {0:s}'
message4.format('file1.txt')
'Processing file file1.txt'
message5 = 'File {0:s} has size {1:d}'
message5.format('file1.txt', 100)
'File file1.txt has size 100'
message5.format('file1.txt', 100)
'File file1.txt has size 100'
message5 = 'File {1:s} has size {0:d}'
message5.format(100, 'file1.txt')
'File file1.txt has size 100'
message6 = 'File {0:20s} has size {1:10d}'
messgae6.format('file1.txt', 100)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    messgae6.format('file1.txt', 100)
NameError: name 'messgae6' is not defined. Did you mean: 'message6'?
message6.format('file1.txt', 100)
'File file1.txt            has size        100'
helloMaessage = 'Hello %s!'
print(helloMaessage % ('Kate', 'Chris'))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(helloMaessage % ('Kate', 'Chris'))
TypeError: not all arguments converted during string formatting
print(helloMaessage % ('Kate',))
Hello Kate!
print(helloMaessage % ('Chris',))
Hello Chris!
helloMessage = "Hello {0:s}!"
helloMessage.format('Kate')
'Hello Kate!'
helloMessage.format('Chis')
'Hello Chis!'
helloMessage = "%s has %d %s"
helloMessage.format('Kate', 1, 'animal')
'%s has %d %s'
print(helloMessage.format('Kate', 1, 'animal'))
%s has %d %s
helloMessage.format('Kate', 1, 'animal')
'%s has %d %s'
print(helloMessage % ('Kate', 1, 'animal'))
Kate has 1 animal
helloMessage.format('Chris', 100000, '$')
'%s has %d %s'
print(helloMessage %('Chris', 100000, '$'))
Chris has 100000 $
helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format ('Kate', 1, 'animal'))
Kate has 1 animal
line = "{0:20} costs {1:6}€"
line = "{0:20} costs {1:6}€"
line = "{0:20} costs {1:6}€"
print(line.format ('ice cream', 3))
ice cream            costs      3€
print(line.format ('trip to venice', 119))
trip to venice       costs    119€
print(line.format ('pizza hawai', 6))
pizza hawai          costs      6€
