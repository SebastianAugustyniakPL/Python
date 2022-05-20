Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:/Users/sebik/OneDrive/Pulpit/Python/string2.py ==========
drive = 'c:\'
SyntaxError: unterminated string literal (detected at line 1)
drive = 'c:\\'
folder = 'scripts\\pythpn\\'
file = 'myscript.py'
path = drive + folder + file
print(path)
c:\scripts\pythpn\myscript.py
path
'c:\\scripts\\pythpn\\myscript.py'
justText = "text with\nnewline
SyntaxError: unterminated string literal (detected at line 1)
justText = "text with\nnewline"
print(justText)
text with
newline
justText = "Macdonald's"
print(justText)
Macdonald's
line ='he sad "I like Python"'
print(line)
he sad "I like Python"
firstName = 'Kasia'
FamillyName = 'Sowa'
lasName = 'Mrugała'
path = firstName + FamillyName + lasName
print(path)
KasiaSowaMrugała
newName = firstName"+"FamillyName"+"lasName
SyntaxError: invalid syntax
newName = firstName+""+FamillyName+""+lasName
print(newName)
KasiaSowaMrugała
music = "Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood
SyntaxError: invalid syntax
music = "Universal Fanfare" 'Jerry Goldsmith' "Happy Together" 'Garry Bonner' "I'm a Man" 'Steve Winwood'
print(music)
Universal FanfareJerry GoldsmithHappy TogetherGarry BonnerI'm a ManSteve Winwood

music = "Universal Fanfare" 'Jerry Goldsmith' "Happy Together"\n 'Garry Bonner' "I'm a Man" 'Steve Winwood'
SyntaxError: unexpected character after line continuation character
music = '"Universal Fanfare" Jerry Goldsmith\n" "Happy Together" Garry Bonner\n" I\'m a Man" Steve Winwood\a'
print(music)
"Universal Fanfare" Jerry Goldsmith
" "Happy Together" Garry Bonner
" I'm a Man" Steve Winwood
print('(\(\)')
(\(\)
print('(\\(\\)')
(\(\)
print('-.-')
-.-
print(0_(")(")
      
SyntaxError: invalid decimal literal
print('0_(")(")')
      
0_(")(")
