$(function() {
  'use strict';

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
