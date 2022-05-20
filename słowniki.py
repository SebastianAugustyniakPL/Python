CountryLeaders={'PL':'DUDA', 'US': "Trump"}
print(CountryLeaders)

CountryLeaders['DE'] = 'Merkel'

print(CountryLeaders)


Chanel={'Google':1480, 'Email': 300, 'Natural Traffic':440, 'TV Spot':700}
print(Chanel['Email'])

chanelsUpdate={'Natural Traffic':520, 'News':600}
print(chanelsUpdate)
Chanel.update(chanelsUpdate)
print(Chanel)
