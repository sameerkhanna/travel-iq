import json
import urllib2

class IndexBuilder:

	def __init__(self):
		self.listOfCategoryId = []
		self.listOfVenueId = {}
		self.listOfCity = {}
		self.listOfFilterCategory = []
		self.listOfFinalFilter = {}
		self.indexStructure = {}
		self.indexWithCity = {}

	def openTempIndex(self):
		f = open('docIdCategory_3.txt', 'r')
		data = f.readlines()
		for line in data:
				line = line.rstrip('\n')
				self.listOfCategoryId.append(line.split('~'))

		#print len(self.listOfCategoryId)

		for i in range (0, len(self.listOfCategoryId)):
			data = self.listOfCategoryId[i]
			self.listOfVenueId[data[1]] = str(data[2])	
			self.listOfCity.setdefault(data[0], []).append(str(data[1]))

		#print self.listOfCity

	def buildListFilter(self):
		self.listOfFilterCategory.append('loud')
		self.listOfFilterCategory.extend(('relaxed', 'friendly', 'outdoor', 'indoor', 'solo', 'groups', 'couple'))

		listOfRelaxedAtm = []
		listOfFriendlyAtm = []
		listOfOutdoorAtm = []
		listOfIndoorAtm = []
		listOfLoudAtm = []
		listOfSoloAtm = []
		listOfGroupsAtm = []
		listOfCoupleAtm = []

		listOfRelaxedAtm.append('quiet')
		listOfRelaxedAtm.extend(('park', 'museum', 'chill', 'secluded', 'relaxing'))

		listOfLoudAtm.append('bar')
		listOfLoudAtm.extend(('lounge', 'dance club', 'loud', 'loud music', 'concert', 'beer'))
	
		listOfFriendlyAtm.append('family')
		listOfFriendlyAtm.extend(('friendly', 'kids', 'children'))

		listOfOutdoorAtm.append('outdoor')
		listOfOutdoorAtm.extend(('balcony', 'patio', 'park', 'rooftop'))

		listOfIndoorAtm.append('restaurants')
		listOfIndoorAtm.extend(('cafe', 'coffee shop', 'coffee', 'museum', 'lounge'))

		listOfSoloAtm.append('solo')
		listOfSoloAtm.extend(('alone', 'individual', 'solitude'))

		listOfGroupsAtm.append('groups')
		listOfGroupsAtm.extend(('family', 'energetic'))

		listOfCoupleAtm.append('date')
		listOfCoupleAtm.extend(('date night', 'couple', 'romantic'))


		self.listOfFinalFilter[self.listOfFilterCategory[0]] = listOfLoudAtm
		self.listOfFinalFilter[self.listOfFilterCategory[1]] = listOfRelaxedAtm
		self.listOfFinalFilter[self.listOfFilterCategory[2]] = listOfFriendlyAtm
		self.listOfFinalFilter[self.listOfFilterCategory[3]] = listOfOutdoorAtm
		self.listOfFinalFilter[self.listOfFilterCategory[4]] = listOfIndoorAtm
		self.listOfFinalFilter[self.listOfFilterCategory[5]] = listOfSoloAtm
		self.listOfFinalFilter[self.listOfFilterCategory[6]] = listOfGroupsAtm
		self.listOfFinalFilter[self.listOfFilterCategory[7]] = listOfCoupleAtm

		#print self.listOfFinalFilter

	def buildPreIndex(self, category, docId):
		listOfCityTemp = []
		listOfCategoryTemp ={}

		self.indexStructure.setdefault(category, []).append(docId)

		for key,value in self.listOfCity.iteritems():
			listOfCityTemp.append(value)
			for i in value:
				if docId == i:
					#listOfCategoryTemp.setdefault(category, []).append(docId)
					#self.indexWithCity.setdefault(key, {}).update(listOfCategoryTemp)
					#self.indexWithCity.setdefault(key, {}).update(listOfCategoryTemp.setdefault(category, []).append(docId))
					self.writeToFile(key, category, docId)
		
		print self.indexStructure
		#print listOfCategoryTemp

	def writeToFile(self, city, category, docId):
		f= open("FinalIndexStructure_1.txt", "ab")
		f.write(str(city) + '~' + str(category) +'~'+ str(docId) +'\n')
		#for key, value in indexStructure.iteritems():
		#	f.write(str(key) +'~'+str(value)+'\n')


	def mapToKeywords(self):
		for keyVenue, valueVenue in self.listOfVenueId.iteritems():
			j=urllib2.urlopen('https://api.foursquare.com/v2/venues/'+valueVenue+'/tips?client_id=Y4SSCFTDL4QXOHSJEU0JSJT0ACWVWWPQCO0ZGMYRWHY0UVMQ&client_secret=P4DGMCRS3QCLWNEVXFWZTP2BWJ5XRBVHNE1PLUGRSI4NXNA0&v=20131011')
			result = json.load(j)
			items = result['response']['tips']['items']

			desc = items[0]['text']
			
			count = 0

			for key,value in self.listOfFinalFilter.iteritems():
				for i in range (0, len(value)):
					if value[i] not in desc:
						continue
					else:
						count = count + 1
						self.buildPreIndex(key,keyVenue)
						if count > 0:
							break

			#print self.indexStructure

def main():
	index = IndexBuilder()
	index.openTempIndex()
	index.buildListFilter()
	index.mapToKeywords()
	#print index.indexWithCity
	index.writeToFile(index.indexStructure)


if __name__== '__main__':
	main()
