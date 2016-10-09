'use strict';

angular.module('myApp.sensor', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/sensor', {
    templateUrl: 'sensor/sensor.html',
    controller: 'SensorCtrl'
  });
}])

.controller('SensorCtrl', [function() {

}]);