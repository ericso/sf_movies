$(function() {
  'use strict';

  App.Collections.Locations = Backbone.Collection.extend({
    url: '/locations/',
  });

});
