angular.module('SchoolsApp.services', [])
    .service('Schools', function($http) {
    this.get = function(location) {
      console.log(location);
      return $http({
          method: 'GET',
          url: 'https://schools.codefordurham.com/api/schools/eligible/',
          params: {
              longitude: location.longitude,
              latitude: location.latitude
          }
      });
    };
});
