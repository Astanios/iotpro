'use strict';

angular.module('myApp.control', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/control', {
    templateUrl: 'control/control.html',
    controller: 'ControlCtrl'
  });
}])

.controller('ControlCtrl', [function() {

}]);