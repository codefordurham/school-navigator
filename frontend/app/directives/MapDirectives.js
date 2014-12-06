angular.module('SchoolsApp.directives', [])
    .directive('schoolsMap', ['$q', 'Schools', function($q, Schools) {
        var linker = function(scope, element, attrs) {
            console.log("Linker");
            // do all map rendering and interactions here
            var map = L.map('map', { zoomControl:true }).setView([36.002453, -78.905869], 13),
                marker,
                markerLatLng,
                schools_layers = [],
                current_highlight,
                homeIcon = L.divIcon({className: 'fa fa-home fa-3x', iconSize: '64px'});
            element.css({
                "height": document.documentElement.clientHeight + "px"
            });
            // default zoom controls position
            map.zoomControl.setPosition("bottomright");

            d = $q.defer();
            d.resolve({
                'map': map
            });
            d.promise.then(function() {
                console.log("what?");
                L.tileLayer('https://{s}.tiles.mapbox.com/v3/vrocha.j3fib8g6/{z}/{x}/{y}.png', {
                    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                    maxZoom: 18
                }).addTo(map)
            });

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
                    schoolIcon = L.divIcon({className: school.type + ' school_point ' + school.level, iconSize: '64px', html: school.short_name});
                    var school_layer,
                        school_marker =  L.marker([school.location.coordinates['1'], school.location.coordinates['0']], {icon: schoolIcon})
                            .bindPopup(school.name);

                    school_marker.school_id = school.id;
                    school_marker.on('mouseover', function() {
                        highlight_school(this.school_id);
                    });

                    school_layer = L.layerGroup([school_marker]);
                    schools_layers.push(school_layer);
                    school_layer.addTo(map);
                });
            });

            var highlight_school = function(school_id) {
                // remove current highlight
                if (current_highlight) {
                    map.removeLayer(current_highlight);
                }
                Schools.get(school_id).success(function(school) {
                    var district_bounderies = [];
                    if (school.district) {
                        angular.forEach(school.district.coordinates[0], function(coordinates, key) {
                            // HACK: coordinates need to be inverted.
                            // just the django things.
                            district_bounderies.push([coordinates[1], coordinates[0]]);
                        });
                    }
                    if (district_bounderies) {
                        current_highlight = L.polygon(district_bounderies, {color: school.color});
                        current_highlight.addTo(map);
                    }
                })
            };
            $('.nav li a').click(function() {
                // remove current highlight
                if (current_highlight) {
                    map.removeLayer(current_highlight);
                }
            });

            var clearMap = function() {
                angular.forEach(schools_layers, function(layer) {
                    map.removeLayer(layer)
                });
                schools_layers = [];
            };

            

        };
        return {
            restrict: 'A',
            link: linker
        }
    }]);
