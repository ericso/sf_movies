// Loads the Google Maps V3 API and setup up the map
$(function() {

  app.mapOptions = {
    zoom: 12,
    // Centered on San Francisco
    center: new google.maps.LatLng(37.7833, -122.4167)
  };

  // Create and render the map
  app.map = new google.maps.Map(
    document.getElementById('id_map'),
    app.mapOptions
  );

  // Array to hold all the map marks we will add
  app.markers = [];

});
