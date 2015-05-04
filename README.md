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
  * This class will be invoked when the local server is initiated (see instructions of Set up Flask framework and run server in Instructions section) and when any action is initiated from the front end. 


### Frontend:
Frontend is composed of two parts; angular for handling the user input/interface and flask to provide a simple layer to communicate with backend. The interface accepts two inputs; a destination text input (search box) and a series of filters based on your personal preferences using radio buttons. We decided to pick these technologies as we wanted to create a very fluid user experience by having a single page application experience. This means the page does not have to refresh when results are served to the page and the experience feels smooth and fast.

1. Angular 
  * All angular code is contained in _travel_iq/static/js_. Main functionality is stored in _controllers.js_, which will  pass user input to/from _services.js_ and templates. _Services.js_ job is to talk directly to flask backend by calling _/search_ URI and passing POST data params including the search input and filter options.
  * We used bootstrap 3 to provide user interface styling and layout. 
  * The HTML templates for angular are contained in _travel_iq/static/partials_. In angular, the templates contain logic embedded in the HTML tag properties to perform loops, conditionals and displaying of data variables. We have two main views:  _search.html_ (contains search input HTML) and _result.html_ (contains results page and filter options). To perform search, we have an _ng-click_ event binded to the search input button. This click event will call _search(term)_, contained in the _controllers.js_ file, which will make a call to _/search_ URI and hit the flask endpoint. We use JSON format for sending/receiving data. Upon return of data, the results variable is populated, which renders on _result.html_. For filtering we perform a similar operations by appending to _$scope.filterOptions_ variable and passing that along to the backend.
  * There are various error states that are handled in the angular code. For example, if no results are returned from flask, we ensure that this is displayed appropriately in the _result.html_ page using conditionals. Also, we have included visual loaders on the page so if the backend is taking some time to process and find results, the user is given feedback that results are still loading. We also take into account if foursquare did not return a venue image, instead we servce a placeholder image.
  * We provide a filter reset function to return a user to the original state and clear all filters.

2. Flask
  * We decided to pick flask, as it is an easy way to provide a basic endpoint for angular to communicate with our backend. Most of the flask code is contained in _controllers.py_ which has a function called _search_ which is our endpoint for angular. This function only accepts POST HTTP actions and takes in json data. This includes the query and filter options. We then pass this directly to our backend class (_RequestHandler.py_), which we have imported. We then return the data back to angular using JSON with appropriate HTTP status.
  * We also use angular's template engine to serve our _index.html_ which is the layout for our application. This single page includes the angular application, which allows angular to run.

3. Screenshots
![Search Box](https://www.dropbox.com/s/s850njerqi7r2w1/Screenshot%202015-05-04%2013.46.35.png?dl=1)
![Search Results](https://www.dropbox.com/s/pxtcrebajy53w3p/Screenshot%202015-05-04%2013.46.54.png?dl=1)
