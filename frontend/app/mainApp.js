var app = angular.module("schoolsApp", ["leaflet-directive", 'SchoolsApp.geoDecoder']);
app.controller('MarkersSimpleController', [ '$scope', '$http', '$location', 'Geodecoder', function($scope, $http, $location,  Geodecoder) {

  function moveLoc(lat, lng) {
    $scope.markers.home.lat = $scope.durham.lat = $scope.position.lat = lat;
    $location.url = $scope.markers.home.lng = $scope.durham.lng = $scope.position.lng = lng;
    $http.get("https://schools.codefordurham.com/api/schools/?latitude=" + lat + "&longitude=" + lng).then(function(response) {
      var data = response.data;
      $scope.markers = { home: $scope.markers.home };
      $scope.districts = [];
      data.filter(function(a) {
        return a.eligibility === 'assigned';
      }).forEach(function(school) {
        this[school.name.replace('-','')] = {
          id: school.id,
          message: school.name,
          lat: school.location.coordinates[1],
          lng: school.location.coordinates[0],
          icon: {
            type: 'div',
            iconSize: [32, 32],
            iconAnchor: [16, 16],
            html: school.short_name,
            className: "school_point " + school.level
          }
        };
      }, $scope.markers);
      data.filter(function(a) {
        return a.eligibility === 'assigned';
      }).forEach(function(school) {
        var districtArray = this;
        $http.get("https://schools.codefordurham.com/api/schools/detail/" + school.id + "/").then(function(response) {
          var data = response.data;
          var district = {
            id: school.id,
            type: 'Feature',
            properties: {
              level: data.level
            },
            geometry: {
              type: 'Polygon',
              coordinates: data.district.coordinates
            }
          };
          districtArray.push(district);
        });
      }, $scope.districts);
    });
  };

  angular.extend($scope, {
    defaults: {
      zoomControlPosition: 'bottomright'
    },
    userLocation: function() {
      $scope.durham.autoDiscover = true;
      var unbindWatch = $scope.$watch('durham.autoDiscover', function() {
        if(!$scope.durham.autoDiscover) {
          $scope.durham.zoom = 18;
          moveLoc($scope.durham.lat, $scope.durham.lng);
          unbindWatch();
        }
      });
    },
    placeAddress: function() {
      var lookup_address = ($scope.address.indexOf("durham") == -1) ? $scope.address + " Durham NC": $scope.address;
      Geodecoder.geocode( { 'address': lookup_address}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
          // always get the first result returned
          var geo = results[0].geometry.location;
          moveLoc(geo.lat(), geo.lng());
        } else {
          alert('Geocode was not successful for the following reason: ' + status);
        }
      });
    },
    durham: {
      lat: 36,
      lng: -78.9,
      zoom: 13
    },
    markers: {
      home: {
        lat: 36,
        lng: -78.9,
        focus: false,
        draggable: true,
        mouseover: false,
        icon: {
          iconUrl: 'img/marker.png',
          iconSize: [32, 32],
          iconAnchor: [16, 16]
        }
      }
    },
    position: {
      lat: 36,
      lng: -78.9
    },
    events: { // or just {} //all events
      markers:{
        enable: [ 'click', 'dragend', 'mouseover', 'mouseout' ]
        //logic: 'emit'
      }
    },
    tiles: {
      name: 'School Mapbox',
      url: 'https://{s}.tiles.mapbox.com/v3/vrocha.j3fib8g6/{z}/{x}/{y}.png',
      type: 'xyz'
    },
    districts: [],
    geojson: {
      data: [],
      style: function(feature) {
        switch(feature.properties.level) {
          case 'middle': return {color: '#3F899E'};
          case 'high': return {color: '#4F61AD'};
          case 'elementary': return {color: '#48BC6B'};
        }
      },
    }
  });

  $scope.$on("leafletDirectiveMarker.dragend", function(event, args){
    moveLoc(args.model.lat, args.model.lng);
  });
  $scope.$on("leafletDirectiveMarker.mouseover", function(event, args) {
    var district = $scope.districts.filter(function(a) {
      return a.id === args.model.id;
    }).pop();
    $scope.geojson.data.push(district);
  });
  $scope.$on("leafletDirectiveMarker.mouseout", function(event, args) {
    $scope.geojson.data = [];
  });
}
]);
