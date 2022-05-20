'''
age = 27

if age >= 18:
   print ("You are adult and you can bou alkohol")
else:
    print("You are too yound to buy alkohol")


isDrunk = False
if age >= 18 and not isDrunk:
   print ("You are adult and you can bou alkohol")
else:
    print("Sorry we cannot sell you alkohol")


isRestrictetArea = False

if age >= 18 and not isDrunk and not isRestrictetArea:
   print ("You are adult and you can bou alkohol")
else:
    print("You are too yound to buy alkohol")

'''


#Zadania 1

MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 40000
num_shares = 100

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print("Zaczynamy Promocję")
elif num_likes<MIN_LIKES:
    print("Brak lajków")
else:
    print("Brak udostępnień")
    

#Zadanie 2
isPizza = False

isBigDrinkOrdered = True

isWeekend = False

if(isPizza or isBigDrinkOrdered)and not isWeekend:
    print("You buy burger")
else:
    print("Zachęcamy do dalszych zakupów")

#Zadanie 3
diskSize = 140
diskSizeUsed = 300
fileSize = 10

if diskSize - diskSizeUsed >=fileSize:
    print("File can be downloaded")
else:
    print("Sorry, out of disk space")

'''

#Instrukcje if / elif
age = 22
isDrunk = True
isRestrictedArea = False

if age < 18:
    print ("You are too young to buy alkohol")
elif isDrunk:
    print ("Are you drunk? We cannot sell you alcohol")
elif isRestrictedArea:
    print("Restricted area. Alcohol is forbidden")
else:
    print("OK, you can buy alcohol")
'''
