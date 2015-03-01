jQuery(document).ready(function($) {

  // TODO(eso) change this to account for where server is hosted
  // $ajaxPrefilter(function(options, originalOptions, jqXHR) {
  //   options.url = 'http://localhost:8000' + options.url;
  // });

  var Locations = Backbone.Collection.extend({
    url: '/locations/',
  });

  var LocationList = Backbone.View.extend({
    el: '.page',
    render: function() {
      var that = this;
      var locations = new Locations();
      locations.fetch({
        success: function(locations) {
          var template = _.template(
            $('#location-list-template').html()
          )({locations: locations.models});
          that.$el.html(template);
        }
      });

    }
  });

  var locationList = new LocationList();

  var Router = Backbone.Router.extend({
    routes: {
      '': 'home',
    },
  });

  var router = new Router();
  router.on('route:home', function () {
    locationList.render();
  });

  Backbone.history.start();

});
