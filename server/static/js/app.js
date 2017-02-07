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

myApp.controller('listingsController', function($scope, $http) {
    $http.get('http://localhost:5000/api/listings?https://www.booli.se/karlaplan/149545/').
        then(function(response) {
            $scope.listings = response.data["listings"];
        });
});

myApp.controller('durationController', function($scope, $http) {
    $http.get('http://localhost:5000/api/duration?origin=Karlaplan%20T-bana,%20Sweden&destination=G%C3%A4rdet%20T-bana,%20Sweden').
        then(function(response) {
            $scope.duration = response.data["duration"];
        });
});