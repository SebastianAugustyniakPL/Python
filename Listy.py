
'''
countries = ['FR', 'US', 'DE', 'RU']
print(countries)
countries[1]='GB'
countries.append('PL') #dodawanie do listy
countries.insert(2, 'ES')
countries.remove('RU') #usuwanie elementów
countries.sort() #sortowanie
countries.reverse() #odwrócenie listy

print(countries.pop(2)) #zwracanie
print(countries.index('PL')) #Sprawdzanie czy element istnieje
print(countries.count('DE')) #Sprawdzenie ile razy dana wartość występuje na liście 


newList = ['FI', 'SE']
countries.extend(newList) #dodawanie do listy nowych obiektów

countriesCopy = countries.copy()
countriesCopy.clear() #wyczyszcza listę

print(countries)
print(countriesCopy)

'''

#Zadania 1
hitsTitle = ['Brothers in arms', 'Bohemian rhapsody', 'starway to heaven', 'riders on the storm', 'wish you were here']
print(hitsTitle)

#Zad 2 
hitsTitle.append('Child in time')
hitsTitle.append('Again')
print(hitsTitle)

#Zad 3
hitsTitle[2] = 'Hotel California'
print(hitsTitle)

#Zad 4
hitsTitle[0] = 'The sound of silence'
print(hitsTitle)

#Zad5
print(hitsTitle.index('Hotel California'))

#Zad6 
hitsTitle.remove('Hotel California')
print(hitsTitle)

#Zad8
hitsRead = hitsTitle.copy()
print(hitsRead)
