$(function() {
  'use strict';

  // TODO(eso) change this to account for where server is hosted
  // $ajaxPrefilter(function(options, originalOptions, jqXHR) {
  //   options.url = 'http://localhost:8000' + options.url;
  // });

  // Backbone View for the search bar
  App.Views.SearchBar = Backbone.View.extend({
    el: '#id_search_container',
    initialize: function() {
      this.render();
    },
    render: function() {
      var that = this;
      app.autocomplete_locations = new App.Collections.AutoCompleteLocations();
      app.autocomplete_locations.fetch({
        success: function(locations) {
          var template = _.template($('#search-template').html(), {});
          that.$el.html(template);

          // Clear autocomplete_tags array
          app.autocomplete_tags = [];

          // Loop through all results from Ajax query
          _.each(locations.models, function(location) {
            fields = location.get('fields');

            // Add tags to autocomplete
            // We make sure that the tag is not null and that it
            //  doesn't already exist in the tag array
            if (fields['title'] != null && $.inArray(fields['title'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['title']);
            }
            if (fields['locations'] != null && $.inArray(fields['locations'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['locations']);
            }
            if (fields['production_company'] != null && $.inArray(fields['production_company'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['production_company']);
            }
            if (fields['distributor'] != null && $.inArray(fields['distributor'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['distributor']);
            }
            if (fields['director'] != null && $.inArray(fields['director'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['director']);
            }
            if (fields['writer'] != null && $.inArray(fields['writer'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['writer']);
            }
            if (fields['actor_1'] != null && $.inArray(fields['actor_1'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['actor_1']);
            }
            if (fields['actor_2'] != null && $.inArray(fields['actor_2'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['actor_2']);
            }
            if (fields['actor_3'] != null && $.inArray(fields['actor_3'], app.autocomplete_tags) === -1) {
              app.autocomplete_tags.push(fields['actor_3']);
            }
          });

          // For auto-complete search, we will source our tag list from the
          //  most of the fields in the film location schema
          $('#id_search_input').autocomplete({
            source: app.autocomplete_tags
          });
        }
      });
    },
    events: {
      'submit': 'doSearch'
    },
    doSearch: function(event) {
      event.preventDefault();
      // Trigger the home route but now with a search term
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

          // Clear out the map
          app.map.deleteMarkers();

          // Loop through all results from Ajax query
          _.each(locations.models, function(location) {
            fields = location.get('fields');

            // Add location pins to map
            app.map.addMarker(
              fields['latitude'],
              fields['longitude'],
              fields['title']
            );
          });
        }
      });

    }
  });

  app.searchBar = new App.Views.SearchBar();
  app.locationList = new App.Views.LocationList();

});
