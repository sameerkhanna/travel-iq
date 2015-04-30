import json
import urllib2
import sys
import re
import os

class RequestHandler:

	def __init__(self):
		self.listOfOutput = []
		self.listOfOutputMap = {}
		self.shortName = ''
		self.listOfCategories = []
		self.listOfDocId = {}
		self.finalList = []
		self.indexDirectory = os.path.dirname(os.path.realpath(__file__)) + '/index'

	def locationConverter(self, location):
		j=urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?address='+location+'&sensor=true')
		result = json.load(j)
		address = result.get('results')
		shortComp = address[0].get('address_components')

		for adComp in shortComp:
			shortCompTemp = adComp.get('types')
			types = adComp.get('types')
			if types[0] == "locality":
				self.shortName = adComp.get('short_name')

	def getListOfVenues(self, city, listOfCategories):
		listOfDocIdTemp = []
		listTemp = []
		valueTemp = []

		f = open(self.indexDirectory + '/FinalIndexStructure_2.txt', 'r')
		data = f.readlines()
		for line in data:
				line = line.rstrip('\n')
				listOfDocIdTemp.append(line.split('~'))

		for i in range (0, len(listOfDocIdTemp)):
			data = listOfDocIdTemp[i]
			if data[0] == city:	
				self.listOfDocId.setdefault(data[1], []).append(str(data[2]))

		if not listOfCategories or listOfCategories[0] == "":
			for key,value in self.listOfDocId.iteritems():
				listTemp.extend(value)

		for key,value in self.listOfDocId.iteritems():
			if len(listOfCategories) > 1:
				if listOfCategories and listOfCategories[0] != "" and key == listOfCategories[0]:
					listTemp.append(value)
			else:
				if listOfCategories and listOfCategories[0] != "" and key == listOfCategories[0]:
					listTemp.extend(value)
		
		for key,value in self.listOfDocId.iteritems():
			if len(listOfCategories) > 1:
				for i in range(1, len(listOfCategories)):
					if key == listOfCategories[i]:
						valueTemp.append(set(value)&set(listTemp[0]))

			else:
				self.finalList.extend(listTemp)
				
		if len(listOfCategories) > 1 and valueTemp:
			self.finalList.extend(valueTemp[0])

	def getDetailsForOutput(self, finalList):
		listOfOutputTemp = []
		listOfVenueId = {}
		listOfOutputInt = {}
		data = []

		f = open(self.indexDirectory + '/tempIndex_4.txt', 'r')
		data = f.readlines()
		for line in data:
				line = line.rstrip('\n')
				listOfOutputTemp.append(line.split('~'))

		if len(finalList) > 0:
			for i in range (0, len(listOfOutputTemp)):
				data = listOfOutputTemp[i]
				for docId in finalList:
					if docId == data[0]:
						listOfVenueId[data[1]] = data[0]

		for key in listOfVenueId.iterkeys():
			for i in range (0, len(listOfOutputTemp)):
				data = listOfOutputTemp[i]	
				try:
					temp = data[1]
					if key == temp:
						listOfOutputInt.setdefault(data[2], []).append(data[3])
						listOfOutputInt.setdefault(data[2], []).append(data[4])
						listOfOutputInt.setdefault(data[2], []).append(data[5])
				except IndexError:
					e = 'error'


		for key,value in listOfOutputInt.iteritems():
			self.listOfOutputMap['venueName'] = key
			self.listOfOutputMap['venueURL'] = value[0]
			self.listOfOutputMap['venueImage'] = value[1]
			self.listOfOutputMap['venueDesc'] = value[2]
			self.listOfOutput.append(self.listOfOutputMap)
			self.listOfOutputMap = {}
		
		return self.listOfOutput


def getResults(location, inputList):
	req = RequestHandler()
	locationName = re.sub(' ', '+', location.rstrip())

	req.locationConverter(locationName)

	for i in range(0, len(inputList)):
		req.listOfCategories.append(inputList[i])

	req.getListOfVenues(req.shortName, req.listOfCategories)
	return req.getDetailsForOutput(req.finalList)

if __name__== '__main__':
	main()

