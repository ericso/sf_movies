// Spec file for testing views.js

describe('App.Views.SearchBar', function() {

  before(function() {
    this.$fixture = $('<div class="page"></div>');
  });

  beforeEach(function() {
    this.$fixture.appendTo($('#fixtures'));
    this.view = new App.Views.SearchBar({
      el: this.$fixture
    });
    this.renderSpy = sinon.spy(this.view, 'render');
  });

  afterEach(function() {
    this.renderSpy = null;
    this.view.remove();
  });

  after(function() {
    $('#fixtures').empty();
  });

  it("renders", function() {
    this.view.render();
    expect(this.renderSpy).to.have.been.calledOnce;
  });

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
    this.renderSpy = sinon.spy(this.view, 'render');
  });

  afterEach(function() {
    this.renderSpy = null;
    this.view.remove();
  });

  after(function() {
    $('#fixtures').empty();
  });


  it("renders", function() {
    this.view.render();
    expect(this.renderSpy).to.have.been.calledOnce;
  });

});
