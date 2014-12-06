angular.module('SchoolsApp.detailCtrl', [])
    .controller('detailCtrl', ['$scope', '$filter', '$routeParams', '$location',
        'Schools', 'Geodecoder', function($scope, $filter, $params, $location, Schools, Geodecoder) {
        $scope.name = "victor";
    }]);
