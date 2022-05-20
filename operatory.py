'''
IsWeekend = True
print("Is Weekend =", IsWeekend)

Temperature = 30
print("Temperature =",Temperature)

ToDoList=''
print("ToDoList =", ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList ==''
print("IsHappy=",IsHappy)

IsHappy = not IsWeekend and Temperature < 20 and ToDoList != '' #ToDoList coś musimy zrobić
print("IsHappy =", IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList =='' \
or not IsWeekend and Temperature < 20 and ToDoList != '' #ToDoList coś musimy zrobić
print("IsHappy =", IsHappy)

'''

#Zadanie

isAutomaticMode = True
print("is the level of day-lighr above 80% :", isAutomaticMode)

is80PercentLight = True
print("is the Sun ligthing directly into the driver's face :", is80PercentLight)

isDirectLight = True
print("is it rainy, foggy or other weather conditions are present :", isDirectLight)

isRainy = False
print("is it Rainy :", isRainy)

turnLightsOn = True
print("turnLightsON :", turnLightsOn)

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
