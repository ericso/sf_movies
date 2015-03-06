// Spec file for testing routers.js

describe('App.Routers.Router', function() {

  before(function() {
    this.router = new App.Routers.Router();
  });

  beforeEach(function() {
    this.callSpy = sinon.spy();
    this.router.bind('route:home', this.callSpy);
  });

  afterEach(function() {
    this.callSpy = null;
  });

  after(function() {
    this.router = null;
  });


  it("has a 'home' route", function() {
    expect(this.router.routes['']).to.equal('home');
  });

  it('triggers the "home" route', function () {
    this.router.navigate('/', {trigger: true});
    expect(this.callSpy).to.have.been.called;
  });

});
