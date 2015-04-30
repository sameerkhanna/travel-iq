import json
import urllib2


class ApiParser:

	def __init__(self):
		self.listOfCategoryId = []
		self.listOfVenueId = {}
		self.listOfVenue = []
		self.NyZipCode = {}
		self.SfZipCode = {}
		self.BostonZipCode = {}

	def mapCityAndZipCodes(self):
		NyZip = []
		NyZip.append('10001')
		NyZip.extend(('10026', '10027', '10030', '10037', '10039', '10001', '10018',
			 '10019', '10020', '10036', '10029', '10035', '10010', '10016', '10017', '10022',
			 '10012', '10013', '10014', '10004', '10005', '10006', '10007', '10038', '10280',
			 '10002', '10003', '10009', '10021', '10028', '10044', '10128', '10023', '10024',
			 '10025', '10031', '10032', '10033', '10034', '10040'))
		self.NyZipCode['NY'] = NyZip

		SfZip = []
		SfZip.append('94102')
		SfZip.extend(('94103', '94104', '94105', '94107', '94108', '94109', '94110', '94111', '94112', '94114'
					   ,'94115', '94116', '94117', '94118', '94121', '94122', '94123', '94124', '94127'
					   ,'94129', '94130', '94131', '94132', '94133', '94134', '94158'))

		self.SfZipCode['SF'] = SfZip

		BostonZip = []
		BostonZip.append('02108')
		BostonZip.extend(('02109', '02110', '02111', '02113', '02114', '02115', '02116', '02118', '02119'
						  ,'02120', '02121', '02122', '02124', '02125', '02126', '02127', '02128', '02129'
						  ,'02130', '02131', '02132', '02134', '02135', '02136', '02151', '02152', '02163'
						  , '02199', '02203', '02210', '02215', '02467'))

		self.BostonZipCode['Boston'] = BostonZip

		print self.NyZipCode
		print self.SfZipCode
		print self.BostonZipCode

	def categoryParser(self):
		j=urllib2.urlopen('https://api.foursquare.com/v2/venues/categories?oauth_token=CFKRBCTL24DCHGC0DZSLCVKF1JM5IPBMG1SBSMZCA201UPUM&v=20131011')
		result = json.load(j)
		category = result['response']['categories']
	
		for i in range (0, len(category)):
			print category[i]['id']
			print category[i]['name']

	def writeToFile(self,listOfVenue):
		fo = open('tempIndex_3.txt', 'ab')
		#0: city, 1: docId, 2:venueId, 3: venue name, 4: link, 5: photo url , 6:desc
		fo.write(str(listOfVenue[1] + '~' + str(listOfVenue[2] + '~' + str(listOfVenue[3] + '~' + str(listOfVenue[4] + '~' + str(listOfVenue[5] + '~' +str(listOfVenue[6])))))) +'\n')
		fa = open('docIdCategory_3.txt', 'ab')
		fa.write(str(listOfVenue[0]+ '~' + str(listOfVenue[1]) + '~' +str(listOfVenue[2])) +'\n')

	def getVenueFromCategory(self, listOfCategoryId):
		listOfValueNY = []
		listOfValueSF = []
		listOfValueBoston = []

		for key,value in self.NyZipCode.iteritems():
				listOfValueNY.append(value)

		for data in listOfValueNY[0]:
			for i in range(0 , len(listOfCategoryId)):
				try:
					j=urllib2.urlopen('https://api.foursquare.com/v2/venues/search?&near='+str(data)+'&categoryId='+str(listOfCategoryId[i])+'&client_id=Y4SSCFTDL4QXOHSJEU0JSJT0ACWVWWPQCO0ZGMYRWHY0UVMQ&client_secret=P4DGMCRS3QCLWNEVXFWZTP2BWJ5XRBVHNE1PLUGRSI4NXNA0&v=20131011')
					result = json.load(j)
					venue = result['response']['venues']

					for i in range(0, len(venue)):
						self.listOfVenueId.setdefault('NY', []).append(str(venue[i]['id']))
				except urllib2.HTTPError:
					print 'There was an error with the request'
				except urllib2.URLError:
					print 'There was an error with the request'

		for key,value in self.SfZipCode.iteritems():
				listOfValueSF.append(value)

		for data in listOfValueSF[0]:
			for i in range(0 , len(listOfCategoryId)):
				try:
					j=urllib2.urlopen('https://api.foursquare.com/v2/venues/search?&near='+str(data)+'&categoryId='+listOfCategoryId[i]+'&client_id=Y4SSCFTDL4QXOHSJEU0JSJT0ACWVWWPQCO0ZGMYRWHY0UVMQ&client_secret=P4DGMCRS3QCLWNEVXFWZTP2BWJ5XRBVHNE1PLUGRSI4NXNA0&v=20131011')
					result = json.load(j)
					venue = result['response']['venues']

					for i in range(0, len(venue)):
						self.listOfVenueId.setdefault('SF', []).append(str(venue[i]['id']))
				except urllib2.HTTPError:
					print 'There was an error with the request'
				except urllib2.URLError:
					print 'There was an error with the request'

		for key,value in self.BostonZipCode.iteritems():
				listOfValueBoston.append(value)

		for data in listOfValueBoston[0]:
			for i in range(0 , len(listOfCategoryId)):
				try:
					j=urllib2.urlopen('https://api.foursquare.com/v2/venues/search?&near='+str(data)+'&categoryId='+listOfCategoryId[i]+'&client_id=Y4SSCFTDL4QXOHSJEU0JSJT0ACWVWWPQCO0ZGMYRWHY0UVMQ&client_secret=P4DGMCRS3QCLWNEVXFWZTP2BWJ5XRBVHNE1PLUGRSI4NXNA0&v=20120609')
					result = json.load(j)
					venue = result['response']['venues']

					for i in range(0, len(venue)):
						self.listOfVenueId.setdefault('Boston', []).append(str(venue[i]['id']))
				except urllib2.HTTPError:
					print 'There was an error with the request'
				except urllib2.URLError:
					print 'There was an error with the request'


	def getVenueDetail(self, listOfVenueId):
		count = 0

		for key in self.listOfVenueId:
			for value in self.listOfVenueId[key]:
				j=urllib2.urlopen('https://api.foursquare.com/v2/venues/'+str(value)+'?client_id=Y4SSCFTDL4QXOHSJEU0JSJT0ACWVWWPQCO0ZGMYRWHY0UVMQ&client_secret=P4DGMCRS3QCLWNEVXFWZTP2BWJ5XRBVHNE1PLUGRSI4NXNA0&v=20131011')
				result = json.load(j)
				venue = result['response']['venue']
				photos = venue['photos']
				photoURL = photos.get('groups')

				try:
					if photoURL[0] != None:
						photoURL2 = photoURL[0].get('items')
				except IndexError:
					e = 'error'
					
				try: 
					if venue['rating'] != None:
						if venue['ratingSignals'] > 200:
							count = count + 1
							self.listOfVenue.append(str(key))
							self.listOfVenue.append(str(count))
							self.listOfVenue.append(str(venue['id']))
							self.listOfVenue.append(str(venue['name'].encode('utf-8', 'ignore')))
							self.listOfVenue.append(str(venue['url']))
							
							try:
								if photoURL != None:
									self.listOfVenue.append(str(photoURL2[0].get('prefix')) + '200x125' + str(photoURL2[0].get('suffix')))
							except KeyError:
								self.listOfVenue.append('No photo URL available')
								print 'no photo'

							try:
								if venue['page']['pageInfo']['description'] != None:
									desc = venue['page']['pageInfo']['description']
									self.listOfVenue.append(desc.encode('utf-8', 'ignore'))
							except KeyError:
								self.listOfVenue.append('No description for this place from Foursquare, visit url for more detail')
								print 'no description found'

							self.writeToFile(self.listOfVenue)
							self.listOfVenue = []
				except KeyError: 
					print 'no rating found... skipping venue'
		

def main():
	api = ApiParser()
	api.listOfCategoryId.append('4d4b7104d754a06370d81259')
	api.listOfCategoryId.append('4d4b7105d754a06373d81259')
	api.listOfCategoryId.append('4d4b7105d754a06374d81259') 
	api.listOfCategoryId.append('4d4b7105d754a06376d81259')
	api.listOfCategoryId.append('4d4b7105d754a06377d81259')


	api.mapCityAndZipCodes()
	api.getVenueFromCategory(api.listOfCategoryId)
	api.getVenueDetail(api.listOfVenueId)


if __name__== '__main__':
	main()


#categoryId = 4d4b7104d754a06370d81259
#categoryName = Arts & Entertainment

#categoryId = 4d4b7105d754a06373d81259
#categoryName = Event

#categoryId = 4d4b7105d754a06374d81259
#categoryName = Food

#categoryId = 4d4b7105d754a06376d81259
#categoryName = Nightlife Spot

#categoryId = 4d4b7105d754a06377d81259
#categoryName = Outdoors & Recreation 

