$(function() {
  'use strict';

  // TODO(eso) change this to account for where server is hosted
  // $ajaxPrefilter(function(options, originalOptions, jqXHR) {
  //   options.url = 'http://localhost:8000' + options.url;
  // });

  App.Collections.Locations = Backbone.Collection.extend({
    url: '/locations/',
  });

  App.Views.LocationList = Backbone.View.extend({
    el: '.page',
    render: function() {
      var that = this;
      app.locations = new App.Collections.Locations();
      app.locations.fetch({
        success: function(locations) {
          // Render table with locations
          var template = _.template(
            $('#location-list-template').html()
          )({locations: locations.models});
          that.$el.html(template);

          _.each(locations.models, function(location) {
            fields = location.get('fields');

            // Add location pins to map
            var coords = new google.maps.LatLng(
              fields['latitude'],
              fields['longitude']
            );
            var marker = new google.maps.Marker({
              position: coords,
              map: app.map,
              title: fields['title']
            });

            // app.markers.append(marker);
          });
        }
      });

    }
  });

  app.locationList = new App.Views.LocationList();

  // Set up front-end routing
  App.Routers.Router = Backbone.Router.extend({
    routes: {
      '': 'home',
    },
  });
  app.router = new App.Routers.Router();
  app.router.on('route:home', function () {
    app.locationList.render();
  });

  Backbone.history.start();

});
