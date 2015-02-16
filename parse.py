class PlayerData(object) :

    def __init__(self, playerName) :
	self._playerName = playerName
        self._victLossRatio = 1
	self._victCount = 0
	self._lossCount = 0

    def addWin(self) :
	self._victCount = self._victCount + 1

    def addLoss(self) :
	self._lossCount = self._lossCount + 1

    def finalyze(self):
	if self._lossCount != 0 :
	    self._victLossRatio = self._victCount/self._lossCount

class CountryData(object):

    def __init__(self, countryName) :
       
        self._name = countryName
        self._players = {}
	self._victLossRatio = 1
	self._victCount = 0
	self._lossCount = 0

    def addWin(self, playerName) :

	self._victCount = self._victCount + 1
	if playerName not in self._players : 
		self._players[playerName] = PlayerData(playerName)
	self._players[playerName].addWin()

    def addLoss(self, playerLost) :

	self._lossCount = self._lossCount + 1
	if playerLost not in self._players :
		self._players[playerLost] = PlayerData(playerLost)
	self._players[playerLost].addLoss()

    def finalyze(self) :
	if self._lossCount != 0 : 
	    self._victLossRatio = self._victCount/ self._lossCount
	for key in self._players :
	    self._players[key].finalyze()

class GeoData(object) :

    def __init__(self) :

        self._countryData = {}

    def feedLine(self, countryWon, countryLost, playerWon, playerLost) :
	if countryWon not in self._countryData :
	    self._countryData[countryWon] = CountryData(countryWon)

	if countryLost not in self._countryData :
	    self._countryData[countryLost] = CountryData(countryLost)

	self._countryData[countryWon].addWin(playerWon)
	self._countryData[countryLost].addLoss(playerLost)

    def getData(self) :
	return self._countryData

    def finalyze(self) :
	for key in self._countryData : 
	    self._countryData[key].finalyze()
	
lines = open('11year.csv').readlines()

print "Length of lines =" + str(len(lines))
heading = lines[0]

for index, value in enumerate(heading.split(',')) :
    print index , value

winCountryIndex = 7
loseCountryIndex = 8
wonPlayerIndex = 5
lostPlayerIndex = 6

gData = GeoData()
for line in lines[1:5] :
    lineSplit = line.split(',')
    gData.feedLine(lineSplit[winCountryIndex], lineSplit[loseCountryIndex], lineSplit[wonPlayerIndex], lineSplit[lostPlayerIndex])

gData.finalyze()
print gData

import json
print json.JSONEncoder().encode(gData.getData())
