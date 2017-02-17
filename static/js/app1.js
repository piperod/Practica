/* global angular */
var app = angular.module('myApp', []);
app.controller('customersCtrl', function ($scope, $http) {
    
    "use strict";
    
   $http.get("http://www.inorthwind.com/Service1.svc/getAllCustomers")
        .success(function (result) {

            $scope.things = result;

        })
        .error(function (data, status) {

            /*jslint devel: true */
        
            console.log(data);

    
});
