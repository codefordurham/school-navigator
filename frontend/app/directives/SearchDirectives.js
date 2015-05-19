angular.module('SchoolsApp.searchDirectives', [])
    .directive('search', ['$q', 'Schools', '$location', 'Geodecoder', function($q, Schools, $location, Geodecoder) {
        var linker = function(scope, element, attrs) {
            // do all map rendering and interactions here
            scope.selectSchool = function (school) {
                angular.forEach(scope.all_schools, function(obj) {
                    if (obj.id == school.id) {
                        obj.selected = true;
                    } else {
                        obj.selected = 'hide';
                    }
                });
            };

            scope.deselectSchool = function () {
                angular.forEach(scope.all_schools, function(school) {
                    school.selected = null;
                });
            };

            scope.relocate = function() {
                var lookup_address = (scope.address.indexOf("durham") == -1) ? scope.address + " Durham NC": scope.address;
                Geodecoder.geocode( { 'address': lookup_address}, function(results, status) {
                    if (status == google.maps.GeocoderStatus.OK) {
                        // always get the first result returned
                        var geo = results[0].geometry.location;
                        $location.path('/location/' + geo.lat() + '/' + geo.lng() + '/');
                        scope.$apply();
                    } else {
                        alert('Geocode was not successful for the following reason: ' + status);
                    }
                });
            };

            scope.NavigationActive = function(tab) {
                scope.tab_name = tab;
            };
        };

        return {
            restrict: 'AE',
            link: linker,
            templateUrl: 'app/templates/search.html'
        }
    }]);
