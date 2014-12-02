angular.module('SchoolsApp.services', [])
    .service('Schools', function($http) {
    this.get_by_type = function(location) {
      var url = 'https://schools.codefordurham.com/api/schools/';
      return $http({
          method: 'GET',
          url: url,
          params: {
              longitude: location.longitude,
              latitude: location.latitude
          }
      });
    };
    this.get = function(id) {
        var url = 'https://schools.codefordurham.com/api/schools/detail/' + id + '/';
        return $http({
            method: 'GET',
            url: url
        });
    }
});
