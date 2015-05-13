angular.module('SchoolsApp.controllers', [])
    .controller('schoolsMapCtrl', ['$scope', '$filter', '$routeParams', '$location',
        'Schools', function($scope, $filter, $params, $location, Schools) {
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

        $scope.filterSchools = function (eligibility) {
            $scope.schools = $filter('filter')($scope.all_schools, {'eligibility': eligibility});
            $scope.eligibility = eligibility;
            $scope.levels = ['elementary', 'middle', 'high'];
        };
    }]);
