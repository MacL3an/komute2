'use strict';   // See note about 'use strict'; below

var myApp = angular.module('myApp', [
 'ngRoute'
]);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/listings.html',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);

myApp.controller('booliUrlController', function($rootScope, $scope) {
        $scope.booliUrl = "https://www.booli.se/karlaplan/149545/"
        $scope.getListings = function() {
            $rootScope.$emit('newBooliUrl', $scope.booliUrl);
        }
    });

myApp.controller('listingsController', function($rootScope, $scope, $http) {
    $rootScope.$on('newBooliUrl', function(event, data) {
        loadListings(data);
    });

    var loadListings = function(url) {
        $http.get('http://localhost:5000/api/listings?https://www.booli.se/karlaplan/149545/').
        then(function(response) {
            $scope.listings = response.data["listings"];
        });
    }
});

myApp.controller('durationController', function($scope, $http) {
    var origin = $scope.listing.location.position.latitude + "," + $scope.listing.location.position.longitude;
    var destination = "Sveavägen 25, Sweden";
    var url = '/api/duration?origin='+origin+'&destination='+destination
    $http.get(url).
        then(function(response) {
            $scope.duration = response.data["duration"];
    });
});

myApp.filter('secondsToDateTime', function() {
    return function(seconds) {
        return new Date(0, 0, 0).setSeconds(seconds);
    };
});