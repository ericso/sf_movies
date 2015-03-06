# sf_movies
A prototype webapp the pulls movie data from data.sfgov.org and displays it on a map. You can filter it!

Please visit the deployed site at [SF Films](http://sffilms.heroku.com).


Problem/Solution
-----------

The problem is to create an app that displays San Francisco filming locations on a map.
The data is obtained at

[DataSF](https://data.sfgov.org/): [Film Locations](https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?).
    
The solution uses Django on the back-end to query the DataSF API, store it and expose another API to serve it.
Backbone.js and Google's Maps Javascript API is used on the front-end to create a UI to display the data on
a map and to make the data filterable.


Architecture
-----------

Back-end:
Django app serves a single page to the browser; this is a Single Page App (SPA). The Django app also exposes
a JSON API that serves a response to 
    
      GET /locations/ 
    
with a search string URL parameter. The response contains a list of JSON objects representing filming locations
for movies in SF.
    
During testing, a Sqlite3 database is used. In production deployed on Heroku, Postgres is used.
To populate the database, a management command
    
      python manage.py populate_db
    
is run. The command makes a GET request to the DataSF: Film Locations API and parses the JSON response.
The command also takes the locations field from the DataSF response objects and makes a query to the Google
Geocoding API to get latitude and longitude coordinates for each object. Note: the queries to the Geocoding
API are limited by a python wait() call since the API is rate-limited to 5 queries per second.
    
Front-end:
Backbone.js is used on the front-end to make queries to the /locations/ url with a search parameter, parse the
response into a collection, and render the results on a map provided by the Google Maps Javascript API.
    
The search bar is a Backbone.js view that also does a query to the /locations/ url. It does this to build a list
of terms to use in the auto-complete functionality of the search bar. A query is executed everytime the searchbar
is rendered.
    
JQuery and Underscore.js are dependencies of Backbone.js. JQuery-UI is used for the auto-complete searchbar.
Twitter Bootstrap is used for page styling.

Testing:
On the backend, Django's TestCase was used for the unit tests and LiveServerTestCase was used for the functional tests. To run the tests

      python manage.py test 

On the front-end, Chai is the testing framework, Mocha is the test runner and SinonJS was used to create spies.
To run the front-end tests, load the file sf_movies/app/static/tests/test.html in the browser.


Tradeoffs
-----------
Everything was done to get a minimum viable app up and running.
    
The front-end is composed of two views that render the map and the search bar. No Backbone.js models were used
because they are unncessary for displaying the results. Notice that map info windows do not go away when you
click on subsequent pins. This is because all info windows are created on data refresh. The proper way to do this
is to create the info window at click event. However, this would require storing the location data in Backbone
models and loading the data from the model at info window creation.
    
Django may have been too heavy of a backend solution to use for a simple JSON API server. I used it because it
is what I am most familiar with. The JSON API only exposes a single GET URL;it doesn't allow for returing objects
by id, or updating objects via POST or PUT, and it does not handle DELETE requests.


Challenges
-----------
I learned a lot building this app prototype. Backbonejs was a new framework for me and as such, I used the minium I
had to in order to get a via app running. As such, front-end testing was new for me as well.

Regarding the tests, they are somewhat incomplete. Test-driven design (TDD) is what I strive for. However, since I
was learning much to build this app, a fair amount of write code then run tests was performed.

Deployment on Heroku proved to be a challenge as well, specifically getting the static files to work. Much
modification of Django's settings.py file was necessary to deploy. In the future, using something like Fabric
to automate deployment would be ideal.


Future Work
-----------
Backbone.js models would be implemented allowing more creative things to be done such as displaying informational
divs on the page on map click events. Also, doing a search should move and/or rescale the map would be cool.

Better handing of the geocoding process is necessary. Most addresess were geocoded well but some ended up elsewhere
in California and there are a lot of "No Results". Currently, the "No Results" locations are still being returned
by the API. This would not be a problem if it weren't that they also show up in the autocomplete search.

The app takes a little bit of time, on the order of seconds for the javascript to load and the server to return
data. Optimization of this would be desirable. A possibility could be to not query until a search is performed.
Adding the coordinates of the map bounding viewport to filter results would increase speed as well. Also, a loading
indicator would give the user feedback and prevent them from wondering if the app crashed or something.
    

Please visit the deployed site at [SF Films](http://sffilms.heroku.com)

Please visit my about.me page at about.me/ericso
