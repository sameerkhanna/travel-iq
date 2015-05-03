# Travel-IQ
##### CS6913 Devika and Sameer

## Instructions:

1. clone this repo

2. install all the necessary packages (best done inside of a virtual environment)
> pip install -r requirements.txt

3. run parser
> python travel_iq/engine/CategoryParser.py

4. build index
> python travel_iq/engine/IndexBuilder.py

5. run the app
> python runserver.py

6. check out site
> http://localhost:5000


## Project component specifications:

The project is created in two parts: backend and frontend. Backend component is built in Python and the main purpose of it is to crawl the API for gathering data, build the index structure and determine the categories as well as ranks of the venues. 

### Backend:
Backend component has three classes, the completion of index structure will be achieved if these three classes are run in their order:

1. CategoryParser.py
 * This class will crawl the Foursquare API and gather the info of venues in 3 different cities (for this phase we decide to go with New York, San Francisco and Boston). After gathering the venues info, this class will also determine which venues have higher ranks and then write them into tempIndex.txt file.
 * This class will determine the venue ID for further analysis and map each ID to the document ID (docIdCategory.txt)
 * This class is the first to be run in order to build the temporary index. (Run from command line: python CategoryParser.py)

2. IndexBuilder.py
  * This class will build the final index structure based on tempIndex and docIdCategory files from the first result. 
  * This class will categorize each of the venue if they belong to the categories we determine to be selected by the users. The categories are done by setting similar keywords and building a dictionary of each category and the related keywords. This class will parse the venues’ tips and texts to determine the category.
  * This class will then write the venue and the category into FinalIndexStructure.txt file.
  * This class is the second to be run in order to build the final index. (Run from command line: python IndexBuilder.py)

3. RequestHandler.py
  * This class is responsible for taking the parameters from the front end (location and list of categories based on users’ selections).
  * This class will then go to final index structure file to parse the category and the document ID and will get the venue’s detailed information based on the matching document ID. 
  * This class will return the results in dictionary and the frontend will display the results.
  * This class will be invoked when the local server is initiated (see instructions of Set up Flask framework and run server in How To Get Started section) and when any action is initiated from the front end. 


### Frontend:


