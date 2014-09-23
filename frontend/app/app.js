var app = angular.module("schoolsApp", [
    'ngRoute',
    'SchoolsApp.directives',
    'SchoolsApp.geoDecoder',
    'SchoolsApp.services',
    'SchoolsApp.controllers'
]);

app.config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $routeProvider
        .when('/', {
            controller: 'schoolsMapCtrl',
            templateUrl: 'app/partials/map.html'
            })
        .when('search', {

        })
        .otherwise({
            redirectTo: '/'
            })
}]);
