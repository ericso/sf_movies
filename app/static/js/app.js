$(function() {
  'use strict';

  // TODO(eso) change this to account for where server is hosted
  // $ajaxPrefilter(function(options, originalOptions, jqXHR) {
  //   options.url = 'http://localhost:8000' + options.url;
  // });

  App.Collections.Locations = Backbone.Collection.extend({
    url: '/locations/',
  });

  // Backbone View for the search bar
  App.Views.SearchBar = Backbone.View.extend({
    el: '#id_search_container',
    initialize: function() {
      this.render();
    },
    render: function() {
      var template = _.template($('#search-template').html(), {});
      this.$el.html(template);
    },
    events: {
      'submit': 'doSearch'
    },
    doSearch: function(event) {
      event.preventDefault();
      // alert("search for " + $('#id_search_input').val());
      app.router.navigate('/' + $('#id_search_input').val(), {trigger: true});
    }
  });

  // Backbone View for Map and Table
  App.Views.LocationList = Backbone.View.extend({
    el: '.page',
    render: function(search) {
      var that = this;
      app.locations = new App.Collections.Locations();
      app.locations.fetch({
        data: $.param({'search': search}),
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
  app.searchBar = new App.Views.SearchBar();

  // Set up front-end routing
  App.Routers.Router = Backbone.Router.extend({
    routes: {
      '': 'home',
      ':search': 'home',
    },
  });
  app.router = new App.Routers.Router();
  app.router.on('route:home', function (search) {
    app.locationList.render(search);
  });

  Backbone.history.start();

});
