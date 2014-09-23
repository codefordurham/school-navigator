app.service('Schools', function($http) {
    this.get = function(location) {
      return $http({
          method: 'GET',
          url: 'https://schools.codefordurham.com/api/schools/eligible/',
          params: {location: '-78.934,35.9730'}
      });
    };
});
