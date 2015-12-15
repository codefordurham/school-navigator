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
            templateUrl: 'app/templates/map.html',
            reloadOnSearch: false
            })
        .when('/location/:latitude/:longitude/', {
            controller: 'schoolsMapCtrl',
            templateUrl: 'app/templates/map.html'
            })
        .when('/schools/:school/', {
            templateUrl: 'app/templates/details.html'
            })
        .when('/about', {
            templateUrl: 'app/templates/about.html'
            })
        .when('/navigating', {
            templateUrl: 'app/templates/navigating.html'
            })
        .when('/navigating/neighborhood', {
            templateUrl: 'app/templates/neighborhood.html'
            })
        .when('/navigating/charter', {
            templateUrl: 'app/templates/charter.html'
            })
        .when('/navigating/magnet', {
            templateUrl: 'app/templates/magnet.html'
            })
        .when('/schools', {
            templateUrl: 'app/templates/navigating.html'
            })
        .when('search', {
        })
}]);

angular.module('SchoolsApp.services', [])
    .service('Schools', ['$http', function($http) {
        var endpoint = location.search.indexOf('env') === -1? 'https://schools.codefordurham.com' : 'http://localhost:8001',
            url;

        this.get_schools = function(location) {
          url = endpoint + '/api/schools/';
          return $http({
              method: 'GET',
              url: url,
              params: {
                  longitude: location.lng,
                  latitude: location.lat
              }
          });
        };
        this.get = function(id) {
          url = endpoint + '/api/schools/detail/' + id + '/';
          return $http({ method: 'GET', url: url });
        }
}]);

angular.module('SchoolsApp.geoDecoder', [])
    .service('Geodecoder', google.maps.Geocoder);

angular.module('SchoolsApp.controllers', ["leaflet-directive"])
    .controller('schoolsMapCtrl', ['$scope', '$filter', '$routeParams', '$location', 'Geodecoder', 'Schools',
        function($scope, $filter, $params, $location, Geodecoder, Schools) {
          angular.extend($scope, {
            defaults: {
              maxZoom: 18,
              minZoom: 11,
              zoomControlPosition: 'bottomright'
            },
            eligibility: "assigned",
            selectSchool: function (school) {
                angular.forEach($scope.all_schools, function(obj) {
                  obj.selected = (obj.id === school.id) || "hide";
                });
            },
            deselectSchools: function() {
              angular.forEach($scope.schools, function(school) {
                school.selected = false;
              })
            },
            maxHeight: function () {
                return $(window).height() - 220 + 'px';
            },
            NavigationActive: function(tab) {
                $scope.tab_name = tab;
            },
            userLocation: function() {
              $scope.durham.autoDiscover = true;
              var unbindWatch = $scope.$watch('durham.autoDiscover', function() {
                if(!$scope.durham.autoDiscover) {
                  $scope.address = '';
                  $scope.durham.zoom = 15;
                  moveLoc($scope.durham.lat, $scope.durham.lng);
                  unbindWatch();
                }
              });
            },
            relocate: function() {
              var lookup_address = ($scope.address.indexOf("durham") == -1) ? $scope.address + " Durham County NC": $scope.address;
              Geodecoder.geocode( { 'address': lookup_address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                  var geo = results[0].geometry.location;
                  moveLoc(geo.lat(), geo.lng());
                } else {
                  alert('Geocode was not successful for the following reason: ' + status);
                }
              });
            },
            durham: {
              //TODO Decide whether we want to limit map scrolling to Durham county area
              /*
              maxbounds: {
                southWest: { lat: 35.83, lng: -79.1},
                northEast: { lat: 36.28, lng: -78.6}
              },
              */
              lat: 36, lng: -78.9, zoom: 13
            },
            markers: {
              home: {
                //TODO Decide whether to allow for dragging before address input
                //TODO Where to put icon before having an address? Near search input?
                //lat: 36, lng: -78.9, // center of default map
                focus: false, draggable: true, mouseover: false,
                zIndexOffset: 1000,
                icon: {
                  type: 'div',
                  iconSize: [32, 32],
                  iconAnchor: [16, 16],
                  className: 'fa fa-home fa-3x'
                }
              }
            },
            position: { lat: 36, lng: -78.9 },
            tiles: {
              name: 'School Mapbox',
              url: 'https://{s}.tiles.mapbox.com/v4/vrocha.j3fib8g6/{z}/{x}/{y}.png32?access_token=pk.eyJ1IjoidnJvY2hhIiwiYSI6Ijc4VTRqNlkifQ.IAL1V6TtIekAMo2sP61J3Q',
              attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
              type: 'xyz'
            },
            events: { markers:{ enable: [ 'click', 'dragend', 'mouseover', 'mouseout' ] } },
            highlight_school: function(schoolId) {
              $scope.schools.forEach(function(school) {
                school.hover = (school.id === schoolId);
              });
              $scope.districts.forEach(function(district) {
                if(district.id === schoolId) {
                  $scope.geojson.data.push(district);
                }
              });
            },
            clear_highlight: function() {
              $scope.schools.forEach(function(school) {
                school.hover = false;
              });
              $scope.geojson.data = [];
            },
            prevDistricts: [],
            districts: [],
            switchTab: function (eligibility) {
              $scope.eligibility = eligibility;
              loadMarkers($scope.all_schools);
              $scope.deselectSchools();
            },
            levelStyles: {
              'elementary': '#48BC6B',
              'secondary': '#3F899E',
              'middle': '#3F899E',
              'high': '#4F61AD'
            },
            levels: ['elementary', 'secondary', 'middle', 'high'],
            zoneTypes: {
              'district': 'black',
              'traditional_option_zone': 'purple',
              'year_round_zone': 'blue',
              'priority_zone': 'red',
              'choice_zone': 'yellow',
              'walk_zone': 'green'
            },
            legend: {
              position: 'topright',
              colors: [ 'black', 'purple', 'blue', 'red', 'yellow', 'green' ],
              labels: [ 'Neighborhood', 'Traditional Option', 'Year Round', 'Priority', 'Choice', 'Walk' ]
            },
            geojson: {
              data: [],
              style: function(feature) {
                return {
                  fillColor: $scope.levelStyles[feature.properties.level],
                  color: $scope.zoneTypes[feature.properties.zoneType]
                };
              },
            }
          });
          if ($params.addr) {
              $scope.address = $params.addr;
          }
          if($params.lat && $params.lng) {
            moveLoc($params.lat, $params.lng);
          }

          function moveLoc(lat, lng) {
            $scope.markers.home.lat = $scope.durham.lat = $scope.position.lat = Number(lat);
            $scope.markers.home.lng = $scope.durham.lng = $scope.position.lng = Number(lng);
            $location.search({lat: lat, lng: lng, addr: $scope.address});
            Schools.get_schools($scope.position).success(function(data) {
              loadMarkers(data);
            });
          }
          function loadMarkers(data) {
              $scope.markers = { home: $scope.markers.home };
              $scope.all_schools = data;
              $scope.schools = [];
              data.filter(function(a) {
                return a.eligibility === $scope.eligibility || (a.eligibility === "option" && a.type === $scope.eligibility);
              }).forEach(function(school) {
                var schoolObj = {
                  id: school.id,
                  message: school.name,
                  lat: school.location.coordinates[1],
                  lng: school.location.coordinates[0],
                  icon: {
                    type: 'div',
                    iconSize: [50, 50],
                    iconAnchor: [25, 25],
                    popupAnchor:  [0, -10],
                    html: school.short_name,
                    className: "school_point " + school.level,
                  }
                };
                this[school.name.replace(/[\.\-\W]/g,'')] = schoolObj;
                $scope.schools.push(school);
              }, $scope.markers);
              data.filter(function(a) {
                return $scope.prevDistricts.indexOf(a.id) === -1 && // Have we already fetched district?
                  a.type !== 'charter' && // Is it a charter? (doesn't have a geographic zone)
                  (a.eligibility === $scope.eligibility || // Is eligibility 'assigned'?
                  (a.eligibility === "option" && a.type === $scope.eligibility)); // Is type 'magnet' or 'charter'?
              }).forEach(function(school) {
                $scope.prevDistricts.push(school.id);
                var districtArray = this;
                Schools.get(school.id).success(function(this_school) {
                  Object.keys($scope.zoneTypes).forEach(function(zone) {
                    if(this_school.hasOwnProperty(zone)) {
                      var district = {
                        id: school.id, type: 'Feature',
                        properties: { level: this_school.level, zoneType: zone },
                        geometry: this_school[zone]
                      };
                      districtArray.push(district);
                    }
                  });
                });
              }, $scope.districts);
          }
          $scope.$on("leafletDirectiveMarker.dragend", function(event, args) {
            moveLoc(args.model.lat, args.model.lng);
            $scope.address = '';
          });
          $scope.$on("leafletDirectiveMarker.mouseover", function(event, args) {
            $scope.highlight_school(args.model.id);
          });
          $scope.$on("leafletDirectiveMarker.mouseout", function(event, args) {
            $scope.clear_highlight();
          });
        }]);

angular.module('SchoolsApp.directives', [])
    .directive('simpleNav', [function() {
        return {
            restrict: 'AE',
            templateUrl: 'app/templates/simpleNav.html'
        }
    }])
    .directive('search', [function() {
        return {
            restrict: 'AE',
            templateUrl: 'app/templates/search.html'
        }
    }])
    .directive('tooltip', [function(){
      return {
          restrict: 'A',
          link: function(scope, element, attrs){
              $(element).hover(function(){
                  // on mouseenter
                  $(element).tooltip('show');
              }, function(){
                  // on mouseleave
                  $(element).tooltip('hide');
              });
          }
      };
    }]);

app.filter('gradeString', [function() {
    var gradeNames = ['PreK3', 'PreK4', 'K', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    return function (gradeNumber) {
      //-2 = preK3, -1 = preK4, 0 = K, 1 = 1, ...
      return gradeNames[gradeNumber + 2];
    }
}]);
