'use strict'; //tells to compiler to not accept 'implicit' variables

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
        $scope.booliUrl = "https://www.booli.se/soderort/914052/?objectType=Parhus%2CRadhus%2CKedjehus&rooms=4";
        $scope.workAddress = "Sveavägen 25, Stockholm";
        $scope.getListings = function() {
            console.log($scope.booliUrl);
            $rootScope.$emit('newBooliUrl', $scope.booliUrl, $scope.workAddress);
        }
    });

myApp.controller('listingsController', function($rootScope, $scope, $http) {
    $rootScope.$on('newBooliUrl', function(event, url, address) {
        $scope.destinationAddress = address;
        loadListings(url);
    });

    var loadListings = function(url) {
        $http.get('/api/listings?'+url).
        then(function(response) {
            $scope.listings = response.data["listings"];
        });
    }
});

myApp.controller('durationController', function($scope, $http) {
    var origin = $scope.listing.location.position.latitude + "," + $scope.listing.location.position.longitude;
    var url = '/api/duration?origin='+origin+'&destination='+$scope.destinationAddress
    $http.get(url).
        then(function(response) {
            $scope.listing.duration = response.data["duration"];
    });
});

myApp.filter('secondsToDateTime', function() {
    return function(seconds) {
        return new Date(0, 0, 0).setSeconds(seconds);
    };
});