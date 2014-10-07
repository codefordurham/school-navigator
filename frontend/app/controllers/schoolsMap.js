angular.module('SchoolsApp.controllers', [])
    .controller('schoolsMapCtrl', ['$scope','Schools', 'Geodecoder', function($scope, Schools, Geodecoder) {
        $scope.schools = [];
        $scope.address = '';
        $scope.userLocation = {
            latitude: '35.9730',
            longitude: '-78.934'
        };

        $scope.relocate = function() {
            if ($scope.address.indexOf("durham") == -1) {
                var lookup_address = $scope.address + " Durham";
            }
            Geodecoder.geocode( { 'address': lookup_address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    // always get the first result returned
                    var geo = results[0].geometry.location;
                    $scope.userLocation = {
                        latitude: geo.lat(),
                        longitude: geo.lng()
                    };
                    Schools.get($scope.userLocation).success(function(data) {
                        $scope.schools = data;
                    });
                } else {
                    alert('Geocode was not successful for the following reason: ' + status);
                }
            });
        };
    }]);
