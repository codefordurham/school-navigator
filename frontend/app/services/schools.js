angular.module('SchoolsApp.services', [])
    .service('Schools', function($http) {
    this.get_schools = function(location) {
      //var url = 'https://schools.codefordurham.com/api/schools/';
      var url = 'http://127.0.0.1:8000/api/schools/';
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
        //var url = 'https://schools.codefordurham.com/api/schools/detail/' + id + '/';
        var url = 'http://127.0.0.1:8000/api/schools/detail/' + id + '/';
        return $http({
            method: 'GET',
            url: url
        });
    }
});
