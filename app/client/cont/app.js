/* global angular */
var app = angular.module('myApp', []);
app.controller('teamCtrl', function ($scope, $http) {
    
    "use strict";
    
    $scope.teamid = "some";
    $scope.Name = "some";
    $scope.country = "some";
    
    $scope.sortType     = 'teamid'; // default sort type
    $scope.sortReverse  = false;  // default sort order
    $scope.searchName = ''; // for filtering the table
    
   // $http.get("http://10.147.187.106:8080")
   //     .success(function (result) {
   //          console.log(result.Team_1);
   //          $scope.things = result.Team_1;

   //      })
   //      .error(function (data, status) {

   //          /*jslint devel: true */
        
   //          console.log(data);

    
   })

   // function sendData($scope) {
   //  $http({
   //      method: "POST",
   //      url: 'http://10.147.187.106:8080',
   //      data: { 'teamid' : , 'Name' : , 'country' : }
   //  })
   //  .then(function(response) {
   //          // success
   //  }, 
   //  function(response) { // optional
   //          // failed
   //  });
   //        }



  $scope.things =[{teamid:1, country:"Spain", Name:"Barcelona"}, {teamid:2, country:"Spain", Name:"Real Madrid"}, {teamid:3, country:"England", Name:"Chelsea"},
    {teamid:4, country:"England", Name:"Liverpool"}, {teamid:5, country:"France", Name:"PSG"}, {teamid:6, country:"France", Name:"Olympique Lyonnais"}, {teamid:7, country:"Italy", Name:"Juventus"},
    {teamid:8, country:"Spain", Name:"Atletico de Madrid"}, {teamid:9, country:"England", Name:"Arsenal"}, {teamid:10, country:"Italy", Name:"Napoli"},
    {teamid:11, country:"England", Name:"Everton"}];
    console.log($scope.things);
 });