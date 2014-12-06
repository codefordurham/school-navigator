angular.module('SchoolsApp.controllers', [])
    .controller('schoolsMapCtrl', ['$scope', '$filter', 'Schools', 'Geodecoder', function($scope, $filter, Schools, Geodecoder) {
        $scope.all_schools = [];  // assigned and optional schools
        $scope.schools = [];  // schools for current selected eligibility
        $scope.address = '';
        $scope.eligibility = 'assigned';
        $scope.userLocation = {
            latitude: '35.9730',
            longitude: '-78.934'
        };

        $scope.$watch('all_schools', function(newValue) {
            $scope.schools = $filter('filter')(newValue, {'eligibility': $scope.eligibility});
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
                    $scope.userLocation = {
                        latitude: geo.lat(),
                        longitude: geo.lng()
                    };
                    Schools.get_by_type($scope.userLocation).success(function(data) {
                        $scope.all_schools = data;
                    });
                } else {
                    alert('Geocode was not successful for the following reason: ' + status);
                }
            });
        };
    }]);
