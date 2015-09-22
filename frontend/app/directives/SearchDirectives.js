angular.module('SchoolsApp.searchDirectives', [])
    .directive('search', ['$q', 'Schools', '$location', 'Geodecoder', function($q, Schools, $location, Geodecoder) {
        var linker = function(scope, element, attrs) {
            scope.maxHeight = function () {
                return $(window).height() - 150 + 'px';
            };

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
                var lookup_address = (scope.address.indexOf("durham") == -1) ? scope.address + " Durham County NC": scope.address;
                Geodecoder.geocode( { 'address': lookup_address}, function(results, status) {
                    if (status == google.maps.GeocoderStatus.OK) {
                        // always get the first result returned
                        var geo = results[0].geometry.location;
                        $location.path('/location/' + geo.lat() + '/' + geo.lng() + '/');
                        scope.$apply();
                    } else {
                        switch(status) {
                            /*
                             * https://developers.google.com/maps/documentation/javascript/geocoding?hl=en#GeocodingStatusCodes 
                             * */
                            case google.maps.GeocoderStatus.ZERO_RESULTS:
                                alert('No results found for address search');
                                break;
                            case google.maps.GeocoderStatus.OVER_QUERY_LIMIT:
                                alert('Over query limit');
                                break;
                            case google.maps.GeocoderStatus.REQUEST_DENIED:
                                alert('Request denied');
                                break;
                            case google.maps.GeocoderStatus.INVALID_REQUEST:
                                alert('Invalid request');
                                break;
                            case google.maps.GeocoderStatus.UNKNOWN_ERROR:
                                alert('Unknown server error');
                                break;
                            default:
                                alert('Other unknown error');
                        }
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
