class PlayerData(object) :

    def __init__(self, playerName) :
	self._playerName = playerName
        self._victLossRatio = 1
	self._victCount = 0
	self._lossCount = 0
	self._json = {}

    def addWin(self) :
	self._victCount = self._victCount + 1

    def addLoss(self) :
	self._lossCount = self._lossCount + 1

    def getJsonAble(self) :
	return self._json

    def finalyze(self):
	if self._lossCount != 0 :
	    self._victLossRatio = float((self._victCount * 1.0)/self._lossCount)
#	print "For " , self._playerName , " WinLoss Ratio = " , self._victLossRatio
	self._json = {
		"PlayerName" : self._playerName,
		"Ratio"	     : self._victLossRatio,
		"Victories"  : self._victCount,
		"Loss"       : self._lossCount
	}

class CountryData(object):

    def __init__(self, countryName) :
       
        self._name = countryName
        self._players = {}
	self._victLossRatio = 1
	self._victCount = 0
	self._lossCount = 0
	self._json = {
		"CountryName" : self.mapRecogName(countryName),
		"Players"     : [],
	}

    def mapRecogName(self, countryAbbr) :

	countryName = {
		"ABW" : "Aruba",
		"AFG" : "Afghanistan",
		"AGO" : "Angola",
		"AIA" : "Anguilla",
		"ALB" : "Albania",
		"AND" : "Andorra",
		"ARE" : "United Arab Emirates",
		"ARG" : "Argentina",
		"ARM" : "Armenia",
		"ASM" : "American Samoa",
		"ATA" : "Antarctica",
		"ATF" : "French Southern Territories",
		"ATG" : "Antigua and Barbuda",
		"AUS" : "Australia",
		"AUT" : "Austria",
		"AZE" : "Azerbaijan",
		"BDI" : "Burundi",
		"BEL" : "Belgium",
		"BEN" : "Benin",
		"BES" : "Bonaire, Sint Eustatius and Saba",
		"BFA" : "Burkina Faso",
		"BGD" : "Bangladesh",
		"BGR" : "Bulgaria",
		"BHR" : "Bahrain",
		"BHS" : "Bahamas",
		"BIH" : "Bosnia and Herzegovina",
		"BLR" : "Belarus",
		"BLZ" : "Belize",
		"BMU" : "Bermuda",
		"BOL" : "Bolivia, Plurinational State of",
		"BRA" : "Brazil",
		"BRB" : "Barbados",
		"BRN" : "Brunei Darussalam",
		"BTN" : "Bhutan",
		"BVT" : "Bouvet Island",
		"BWA" : "Botswana",
		"CAF" : "Central African Republic",
		"CAN" : "Canada",
		"CCK" : "Cocos (Keeling) Islands",
		"CHE" : "Switzerland",
		"CHL" : "Chile",
		"CHN" : "China",
		"CMR" : "Cameroon",
		"COD" : "Congo, the Democratic Republic of the",
		"COG" : "Congo",
		"COK" : "Cook Islands",
		"COL" : "Colombia",
		"COM" : "Comoros",
		"CPV" : "Cabo Verde",
		"CRI" : "Costa Rica",
		"CUB" : "Cuba",
		"CXR" : "Christmas Island",
		"CYM" : "Cayman Islands",
		"CYP" : "Cyprus",
		"CZE" : "Czech Republic",
		"DEU" : "Germany",
		"DJI" : "Djibouti",
		"DMA" : "Dominica",
		"DNK" : "Denmark",
		"DOM" : "Dominican Republic",
		"DZA" : "Algeria",
		"ECU" : "Ecuador",
		"EGY" : "Egypt",
		"ERI" : "Eritrea",
		"ESH" : "Western Sahara",
		"ESP" : "Spain",
		"EST" : "Estonia",
		"ETH" : "Ethiopia",
		"FIN" : "Finland",
		"FJI" : "Fiji",
		"FLK" : "Falkland Islands (Malvinas)",
		"FRA" : "France",
		"FRO" : "Faroe Islands",
		"FSM" : "Micronesia, Federated States of",
		"GAB" : "Gabon",
		"GBR" : "United Kingdom",
		"GEO" : "Georgia country",
		"GGY" : "Guernsey",
		"GHA" : "Ghana",
		"GIB" : "Gibraltar",
		"GIN" : "Guinea",
		"GLP" : "Guadeloupe",
		"GMB" : "Gambia",
		"GNB" : "Guinea-Bissau",
		"GNQ" : "Equatorial Guinea",
		"GRC" : "Greece",
		"GRD" : "Grenada",
		"GRL" : "Greenland",
		"GTM" : "Guatemala",
		"GUF" : "French Guiana",
		"GUM" : "Guam",
		"GUY" : "Guyana",
		"HKG" : "Hong Kong",
		"HMD" : "Heard Island and McDonald Islands",
		"HND" : "Honduras",
		"HRV" : "Croatia",
		"HTI" : "Haiti",
		"HUN" : "Hungary",
		"IDN" : "Indonesia",
		"IMN" : "Isle of Man",
		"IND" : "India",
		"IOT" : "British Indian Ocean Territory",
		"IRL" : "Ireland",
		"IRN" : "Iran, Islamic Republic of",
		"IRQ" : "Iraq",
		"ISL" : "Iceland",
		"ISR" : "Israel",
		"ITA" : "Italy",
		"JAM" : "Jamaica",
		"JEY" : "Jersey",
		"JOR" : "Jordan",
		"JPN" : "Japan",
		"KAZ" : "Kazakhstan",
		"KEN" : "Kenya",
		"KGZ" : "Kyrgyzstan",
		"KHM" : "Cambodia",
		"KIR" : "Kiribati",
		"KNA" : "Saint Kitts and Nevis",
		"KOR" : "Korea",
		"KWT" : "Kuwait",
		"LAO" : "Lao People's Democratic Republic",
		"LBN" : "Lebanon",
		"LBR" : "Liberia",
		"LBY" : "Libya",
		"LCA" : "Saint Lucia",
		"LIE" : "Liechtenstein",
		"LKA" : "Sri Lanka",
		"LSO" : "Lesotho",
		"LTU" : "Lithuania",
		"LUX" : "Luxembourg",
		"LVA" : "Latvia",
		"MAC" : "Macao",
		"MAF" : "Saint Martin (French part)",
		"MAR" : "Morocco",
		"MCO" : "Monaco",
		"MDA" : "Moldova, Republic of",
		"MDG" : "Madagascar",
		"MDV" : "Maldives",
		"MEX" : "Mexico",
		"MHL" : "Marshall Islands",
		"MKD" : "Macedonia, the former Yugoslav Republic of",
		"MLI" : "Mali",
		"MLT" : "Malta",
		"MMR" : "Myanmar",
		"MNE" : "Montenegro",
		"MNG" : "Mongolia",
		"MNP" : "Northern Mariana Islands",
		"MOZ" : "Mozambique",
		"MRT" : "Mauritania",
		"MSR" : "Montserrat",
		"MTQ" : "Martinique",
		"MUS" : "Mauritius",
		"MWI" : "Malawi",
		"MYS" : "Malaysia",
		"MYT" : "Mayotte",
		"NAM" : "Namibia",
		"NCL" : "New Caledonia",
		"NER" : "Niger",
		"NFK" : "Norfolk Island",
		"NGA" : "Nigeria",
		"NIC" : "Nicaragua",
		"NIU" : "Niue",
		"NLD" : "Netherlands",
		"NOR" : "Norway",
		"NPL" : "Nepal",
		"NRU" : "Nauru",
		"NZL" : "New Zealand",
		"OMN" : "Oman",
		"PAK" : "Pakistan",
		"PAN" : "Panama",
		"PCN" : "Pitcairn",
		"PER" : "Peru",
		"PHL" : "Philippines",
		"PLW" : "Palau",
		"PNG" : "Papua New Guinea",
		"POL" : "Poland",
		"PRI" : "Puerto Rico",
		"PRK" : "Korea, Democratic People's Republic of",
		"PRT" : "Portugal",
		"PRY" : "Paraguay",
		"PSE" : "Palestine, State of",
		"PYF" : "French Polynesia",
		"QAT" : "Qatar",
		"ROU" : "Romania",
		"RUS" : "Russian Federation",
		"RWA" : "Rwanda",
		"SAU" : "Saudi Arabia",
		"SDN" : "Sudan",
		"SEN" : "Senegal",
		"SGP" : "Singapore",
		"SGS" : "South Georgia and the South Sandwich Islands",
		"SHN" : "Saint Helena, Ascension and Tristan da Cunha",
		"SJM" : "Svalbard and Jan Mayen",
		"SLB" : "Solomon Islands",
		"SLE" : "Sierra Leone",
		"SLV" : "El Salvador",
		"SMR" : "San Marino",
		"SOM" : "Somalia",
		"SPM" : "Saint Pierre and Miquelon",
		"SRB" : "Serbia",
		"SSD" : "South Sudan",
		"STP" : "Sao Tome and Principe",
		"SUR" : "Suriname",
		"SVK" : "Slovakia",
		"SVN" : "Slovenia",
		"SWE" : "Sweden",
		"SWZ" : "Swaziland",
		"SXM" : "Sint Maarten (Dutch part)",
		"SYC" : "Seychelles",
		"SYR" : "Syrian Arab Republic",
		"TCA" : "Turks and Caicos Islands",
		"TCD" : "Chad",
		"TGO" : "Togo",
		"THA" : "Thailand",
		"TJK" : "Tajikistan",
		"TKL" : "Tokelau",
		"TKM" : "Turkmenistan",
		"TLS" : "Timor-Leste",
		"TON" : "Tonga",
		"TTO" : "Trinidad and Tobago",
		"TUN" : "Tunisia",
		"TUR" : "Turkey",
		"TUV" : "Tuvalu",
		"TWN" : "Taiwan, Province of China",
		"TZA" : "Tanzania, United Republic of",
		"UGA" : "Uganda",
		"UKR" : "Ukraine",
		"UMI" : "United States Minor Outlying Islands",
		"URY" : "Uruguay",
		"USA" : "United States",
		"UZB" : "Uzbekistan",
		"VAT" : "Holy See (Vatican City State)",
		"VCT" : "Saint Vincent and the Grenadines",
		"VEN" : "Venezuela, Bolivarian Republic of",
		"VGB" : "Virgin Islands, British",
		"VIR" : "Virgin Islands, U.S.",
		"VNM" : "Viet Nam",
		"VUT" : "Vanuatu",
		"WLF" : "Wallis and Futuna",
		"WSM" : "Samoa",
		"YEM" : "Yemen",
		"ZAF" : "South Africa",
		"ZMB" : "Zambia",
		"ZWE" : "Zimbabwe",

		"NED" : "Nederlands",
		"URU" : "Uruguay",
		"TPE" : "Chinese Taipei",
		"SUI" : "Switzerland",
		"CRC" : "CostaRica",
		"DEN" : "Denmark",
		"CRO" : "Croatia",
		"GER" : "Germany",
		"POR" : "Portugal",
		"BUL" : "Bulgaria",
		"CHI" : "Chile",
		"SLO" : "Slovenia",
		"PHI" : "Philippines",
		"ALG" : "Algeria",
		"RSA" : "South Africa",
		"GRE" : "Greece",
		"MON" : "Myanmar",
		"LAT" : "Latvia",
	}
	if countryAbbr in countryName :
		return countryName[countryAbbr]
	else :
		return countryAbbr

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


    def getJsonAble(self) :
	return self._json

    def finalyze(self) :
	if self._lossCount != 0 : 
	    self._victLossRatio = float(self._victCount * 1.0/ self._lossCount)
	self._json["PlayerCount"] = len(self._players)
	for key in self._players :
	    self._players[key].finalyze()
	    self._json["Players"].append(self._players[key].getJsonAble())
	self._json["Ratio"] = self._victLossRatio

class GeoData(object) :

    def __init__(self) :

        self._countryData = {}
	self._json = {
		"GeoData" : {}
	}

    def addToDicts(self, countryName) :
	    self._countryData[countryName] = CountryData(countryName)
	    self._json["GeoData"][countryName] = self._countryData[countryName].getJsonAble()

    def feedLine(self, countryWon, countryLost, playerWon, playerLost) :
	if countryWon not in self._countryData :
		self.addToDicts(countryWon)

	if countryLost not in self._countryData :
		self.addToDicts(countryLost)

	self._countryData[countryWon].addWin(playerWon)
	self._countryData[countryLost].addLoss(playerLost)

    def getData(self) :
	return self._countryData

    def finalyze(self) :
	for key in self._countryData : 
	    self._countryData[key].finalyze()

    def getJsonAble(self) :
	return self._json
		
	
lines = open('11year.csv').readlines()

#print "Length of lines =" + str(len(lines))
heading = lines[0]

#for index, value in enumerate(heading.split(',')) :
 #   print index , value

winCountryIndex = 7
loseCountryIndex = 8
wonPlayerIndex = 5
lostPlayerIndex = 6

gData = GeoData()
for line in lines[1:] :
    lineSplit = line.split(',')
    gData.feedLine(lineSplit[winCountryIndex], lineSplit[loseCountryIndex], lineSplit[wonPlayerIndex], lineSplit[lostPlayerIndex])

gData.finalyze()
#print gData

import json
print json.dumps(gData.getJsonAble())
