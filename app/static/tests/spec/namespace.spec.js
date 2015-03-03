// Spec file for testing namespace.js

describe('Namespace', function() {

  it("provides the 'App' object", function() {
    expect(App).to.be.an('object');
    expect(App).to.include.keys(
      'Config',
      'Models',
      'Collections',
      'Routers',
      'Views',
      'Templates'
    );
  });

  it("provides the 'app' object", function() {
    expect(app).to.be.an('object');
  });

});
