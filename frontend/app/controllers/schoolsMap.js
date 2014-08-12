app.controller('schoolsMapCtrl', ['$scope','Schools', 'Geodecoder', function($scope, Schools, Geodecoder) {
    $scope.name = "victor rocha";
    $scope.schools = Schools.getList();
    $scope.address = '';
    var map = L.map('map', { zoomControl:false }).setView([36.002453, -78.905869], 13);

    $scope.alert = function() {
        alert("This is a nice alert!");
    };

    $scope.renderMap = function() {
        document.getElementById("map")
            .style.height = document.documentElement.clientHeight + "px";
        L.tileLayer('http://{s}.tiles.mapbox.com/v3/vrocha.j3fib8g6/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18
        }).addTo(map);

        var features = $scope.schools;
        L.geoJson(features, {
            style: function(feature) {
                console.log(feature.properties.SCHOOL);
                return {color: "red"};
            },
            onEachFeature: function(feature, layer) {
                console.log(feature);
                layer.bindPopup(feature.properties.SCHOOL);
            }
        }).addTo(map);
    };

    $scope.relocate = function() {
        Geodecoder.geocode( { 'address': $scope.address}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var geo = results[0].geometry.location;
                map.setView([geo.lat(), geo.lng()], 18);
                L.marker([geo.lat(), geo.lng()]).addTo(map);
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    }
}]);
