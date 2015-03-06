// Spec file for testing collections.js

describe('App.Collections.Locations', function() {

  it("has default values", function() {
    expect(App.Collections.Locations).to.be.ok;
    expect(App.Collections.Locations).to.have.length(0);
  });

});


describe('App.Collections.AutoCompleteLocations', function() {

  it("has default values", function() {
    expect(App.Collections.AutoCompleteLocations).to.be.ok;
    expect(App.Collections.AutoCompleteLocations).to.have.length(0);
  });

});
