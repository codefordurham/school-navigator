app.controller('schoolsMapCtrl', ['$scope','Schools', 'Geodecoder', function($scope, Schools, Geodecoder) {
    $scope.schools = Schools.getList();
    $scope.address = '';

    var map = L.map('map', { zoomControl:false }).setView([36.002453, -78.905869], 13),
        user_marker = null,
        schools_layer = null;

    $scope.renderMap = function() {
        document.getElementById("map").style.height = document.documentElement.clientHeight + "px";
        L.tileLayer('http://{s}.tiles.mapbox.com/v3/vrocha.j3fib8g6/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18
        }).addTo(map);
    };

    $scope.drawSchools = function() {
        schools_layer = L.geoJson($scope.schools, {
            style: function(feature) {
                console.log(feature.properties.SCHOOL);
                return {color: "red"};
            },
            onEachFeature: function(feature, layer) {
                console.log(feature);
                layer.bindPopup(feature.properties.SCHOOL);
            }
        });
        schools_layer.addTo(map);
    };

    $scope.relocate = function() {
        Geodecoder.geocode( { 'address': $scope.address}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                // always get the first result returned
                var geo = results[0].geometry.location;
                // clear map
                $scope.clearMap();
                map.setView([geo.lat(), geo.lng()], 18);
                user_marker = L.marker([geo.lat(), geo.lng()]);
                user_marker.addTo(map);
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    };

    $scope.clearMap = function() {
        // Removes marker and points/polygons from map
        if (user_marker != null) {
            map.removeLayer(user_marker);
        }
        if (schools_layer != null) {
            map.removeLayer(schools_layer);
        }
    }
}]);
