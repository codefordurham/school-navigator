angular.module('SchoolsApp.navDirectives', [])
    .directive('navMenu', [function() {
        return {
            restrict: 'AE',
            templateUrl: 'app/templates/nav-menu.html'
        }
    }]);
