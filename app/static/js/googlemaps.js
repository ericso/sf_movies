// Loads the Google Maps V3 API and setup up the map

function initialize() {

  var mapOptions = {
    zoom: 12,
    // Centered on San Francisco
    center: new google.maps.LatLng(37.7833, -122.4167)
  };

  var map = new google.maps.Map(
    document.getElementById('map-canvas'),
    mapOptions
  );
}

function loadScript() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp' +
               '&signed_in=true&callback=initialize';
  document.body.appendChild(script);
}

window.onload = loadScript;
