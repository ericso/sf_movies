// Loads the Google Maps V3 API and setup up the map
$(function() {
  'use strict';

  var mapOptions = {
    zoom: 12,
    // Centered on San Francisco
    center: new google.maps.LatLng(37.7833, -122.4167)
  };

  // Create and render the map
  app.map = new google.maps.Map(
    document.getElementById('id_map'),
    mapOptions
  );

  // Array to hold all the map marks we will add
  app.markers = [];

  // Add a marker to the map and push to the array.
  google.maps.Map.prototype.addMarker = function(lat, lng, title) {
    var coords = new google.maps.LatLng(lat, lng);
    var marker = new google.maps.Marker({
      position: coords,
      map: app.map,
      title: title
    });
    app.markers.push(marker);
  }

  // Add all pushed markers to the map
  google.maps.Map.prototype.setAllMap = function(map) {
    for (var i = 0; i < app.markers.length; i++) {
      app.markers[i].setMap(map);
    }
  }

  // Clear all markers
  google.maps.Map.prototype.clearMarkers = function() {
    this.setAllMap(null);
  }

  // Show any markers currently in the array.
  google.maps.Map.prototype.showMarkers = function() {
    this.setAllMap(app.map);
  }

  // Deletes all markers in the array by removing references to them.
  google.maps.Map.prototype.deleteMarkers = function() {
    this.clearMarkers();
    app.markers = [];
  }

});
