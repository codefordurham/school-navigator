app.controller('schoolsMapCtrl', ['$scope','Schools', 'Geodecoder', function($scope, Schools, Geodecoder) {
    $scope.schools = [];
    $scope.address = '';
    $scope.userLocation = {
        latitude: '35.9730',
        longitude: '-78.934'
    };

    $scope.relocate = function() {
        Geodecoder.geocode( { 'address': $scope.address}, function(results, status) {
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
