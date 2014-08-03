var app = angular.module("schoolsApp", ['ngRoute']);

app.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'schoolsMapCtrl',
            templateUrl: 'app/partials/map.html'
            })
        .otherwise({
            redirectTo: '/'
            })
});
