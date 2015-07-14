var app = angular.module("schoolsApp", [
    'ngRoute',
    'SchoolsApp.directives',
    'SchoolsApp.geoDecoder',
    'SchoolsApp.services',
    'SchoolsApp.controllers',
    'SchoolsApp.detailCtrl',
    'SchoolsApp.searchDirectives',
    'SchoolsApp.navDirectives'
]);

app.config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $routeProvider
        .when('/', {
            controller: 'schoolsMapCtrl',
            templateUrl: 'app/templates/map.html'
            })
        .when('/location/:latitude/:longitude/', {
            controller: 'schoolsMapCtrl',
            templateUrl: 'app/templates/map.html'
            })
        .when('/schools/:school/', {
            controller: 'detailCtrl',
            templateUrl: 'app/templates/details.html'
            })
        .when('/about', {
            templateUrl: 'app/templates/about.html'
            })
        .when('/navigating', {
            templateUrl: 'app/templates/navigating.html'
            })
        .when('/navigating/neighborhood', {
            templateUrl: 'app/templates/neighborhood.html'
            })
        .when('/navigating/charter', {
            templateUrl: 'app/templates/charter.html'
            })
        .when('/navigating/magnet', {
            templateUrl: 'app/templates/magnet.html'
            })
        .when('/schools', {
            templateUrl: 'app/templates/navigating.html'
            })
        .when('search', {

        })
}]);

app.filter('gradeString', [function() {
    var gradeNames = ['PreK3', 'PreK4', 'K', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    return function (gradeNumber) {
        //-2 = preK3, -1 = preK4, 0 = K, 1 = 1, ...
	return gradeNames[gradeNumber + 2];
    }
}]);
