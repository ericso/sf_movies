// Spec file for testing app.js

describe('App.Collections.Locations', function() {

  it("has default values", function() {
    expect(App.Collections.Locations).to.be.ok;
    expect(App.Collections.Locations).to.have.length(0);
  });

});


describe('App.Routers.Router', function() {

  before(function() {
    this.router = new App.Routers.Router();
  });

  after(function() {
    this.router = null;
  });

  it("has a 'home' route", function() {
    expect(this.router.routes['']).to.equal('home');
  });

  // it('triggers the "home" route', function () {
  //   // TODO(eso) write test
  // });

});


describe('App.Views.LocationList', function() {

  before(function() {
    this.$fixture = $('<div class="page"></div>');
  });

  beforeEach(function() {
    this.$fixture.appendTo($('#fixtures'));
    this.view = new App.Views.LocationList({
      el: this.$fixture
    });
  });

  afterEach(function() {
    this.view.remove();
  });

  after(function() {
    $('#fixtures').empty();
  });

  describe('render', function() {

    it("fetches locations on render", function() {
      var renderSpy = sinon.spy();

      this.view.on({'render': renderSpy});
      this.view.render();

      expect(renderSpy).to.have.been.calledOnce;
    });

  });

});
