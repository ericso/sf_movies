$(function() {
  'use strict';

  App.Collections.Locations = Backbone.Collection.extend({
    url: '/locations/',
  });

  App.Collections.AutoCompleteLocations = Backbone.Collection.extend({
    url: '/locations/',
  })

});
