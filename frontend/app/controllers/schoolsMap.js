angular.module('SchoolsApp.controllers', [])
    .controller('schoolsMapCtrl', ['$scope', '$filter', '$routeParams', '$location',
        'Schools', 'Geodecoder', function($scope, $filter, $params, $location, Schools, Geodecoder) {
        $scope.address = '';
        $scope.eligibility = 'assigned';
        if ($params.latitude && $params.longitude) {
            $scope.userLocation = {
                latitude: $params.latitude,
                longitude: $params.longitude
            };
        } else {
            $scope.userLocation = {
                latitude: '35.9730',
                longitude: '-78.934'
            };
        }

        Schools.get_schools($scope.userLocation).success(function(data) {
            $scope.all_schools = data;
            $scope.filterSchools($scope.eligibility);
            $('[data-toggle="tooltip"]').tooltip();
        });

        $scope.NavigationActive = function(tab) {
            $scope.tab_name = tab;
        };

        $scope.filterSchools = function (eligibility) {
            $scope.schools = $filter('filter')($scope.all_schools, {'eligibility': eligibility});
            $scope.eligibility = eligibility;
        };

        $scope.relocate = function() {
            var lookup_address = ($scope.address.indexOf("durham") == -1) ? $scope.address + " Durham NC": $scope.address;
            Geodecoder.geocode( { 'address': lookup_address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    // always get the first result returned
                    var geo = results[0].geometry.location;
                    $location.path('/location/' + geo.lat() + '/' + geo.lng() + '/', false);
                } else {
                    alert('Geocode was not successful for the following reason: ' + status);
                }
            });
        };
    }]);
