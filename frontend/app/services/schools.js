angular.module('SchoolsApp.services', [])
    .service('Schools', function($http) {
    this.get = function(location, type) {
      var url = 'https://schools.codefordurham.com/api/schools/' + type + '/';
      return $http({
          method: 'GET',
          url: url,
          params: {
              longitude: location.longitude,
              latitude: location.latitude
          }
      });
    };
});
