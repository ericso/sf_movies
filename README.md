# sf_movies
A prototype webapp the pulls movie data from data.sfgov.org and displays it on a map. You can filter it!

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
    
    
    Tradeoffs:
    Everything was done to get a minimum viable app up and running.
    
    The front-end is composed of two views that render the map and the search bar. No Backbone.js models were used
    because they are unncessary for displaying the results. Notice that map info windows do not go away when you
    click on subsequent pins. This is because all info windows are created on data refresh. The proper way to do this
    is to create the info window at click event. However, this would require storing the location data in Backbone
    models and loading the data from the model at info window creation.
    
    Django may have been too heavy of a backend solution to use for a simple JSON API server. I used it because it
    is what I am most familiar with. The JSON API only exposes a single GET URL;it doesn't allow for returing objects
    by id, or updating objects via POST or PUT, and it does not handle DELETE requests.
    
    Future Work:
    Backbone.js models would be implemented allowing more creative things to be done such as displaying informational
    divs on the page on map click events. Also, doing a search should move and/or rescale the map.
    

Please visit the deployed site at [SF Films](sffilms.heroku.com)

Please visit my about.me page at about.me/ericso
