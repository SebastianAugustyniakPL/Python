'''
i=10
imax=0

while i >= imax: #warunek
    print(i,"I like Python")
    i-=2
else:
    print("Now i =", i)
'''

#Zadania 1

firsRow = 1
lastRow = 31
currentRow = firsRow

while currentRow <= lastRow:
    print("Row number", currentRow)
    currentRow+=1


#Zadanie 2
start = 1
end = 13

number = start

while number<=end:
    print(number, number*number, number*number*number)
    number+=1

#Zadanie 3
start = 0
end = 13

x=start

while x<=end:
    print(x, 2**x)
    x+=1

    
#Zadanie 4
start = 1
end = 10

number = start

while number<=start:
    print(number*'x')
    number+=1
