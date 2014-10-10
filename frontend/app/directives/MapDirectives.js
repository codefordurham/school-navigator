angular.module('SchoolsApp.directives', [])
    .directive('schoolsMap', [function() {
        var linker = function(scope, element, attrs) {
            // do all map rendering and interactions here
            var map = L.map('map', { zoomControl:false }).setView([36.002453, -78.905869], 13),
                marker,
                markerLatLng,
                schools_layers = [],
                homeIcon = L.divIcon({className: 'fa fa-home fa-2x', iconSize: '64px'}),
                schoolIcon = L.divIcon({className: 'fa fa-building fa-2x', iconSize: '64px'});
            element.css({
                "height": document.documentElement.clientHeight + "px"
            });
            L.tileLayer('https://{s}.tiles.mapbox.com/v3/vrocha.j3fib8g6/{z}/{x}/{y}.png', {
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                maxZoom: 18
            }).addTo(map);

            // resize map to fit current window
            $(window).bind('resize', function() {
                element.css({
                    "height": document.documentElement.clientHeight + "px"
                });
            });

            // variable changes
            scope.$watch(attrs.userLocation, function(location) {
                // add or move marker to map
                if (marker) {
                    markerLatLng = new L.LatLng(location.latitude, location.longitude);
                    marker.setLatLng(markerLatLng);
                } else {
                    marker = L.marker(
                        [location.latitude, location.longitude],
                        {icon: homeIcon}
                    ).addTo(map);
                }
                // center marker
                map.setView([location.latitude, location.longitude], 12);
            });

            scope.$watch(attrs.schools, function(schools) {
                // clear map
                clearMap();
                angular.forEach(schools, function(school) {
                    console.log(school);
                    var school_layer,
                        school_marker =  L.marker([school.location.coordinates['1'], school.location.coordinates['0']], {icon: schoolIcon})
                            .bindPopup(school.name);

                    school_layer = L.layerGroup([school_marker]);
                    schools_layers.push(school_layer);
                    school_layer.addTo(map);
                });
            });

            var clearMap = function() {
                angular.forEach(schools_layers, function(layer) {
                    map.removeLayer(layer)
                });
                schools_layers = [];
            }
        };
        return {
            restrict: 'A',
            link: linker
        }
    }]);
