'use strict';

angular.module('myApp.ia', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/ia', {
    templateUrl: 'ia/ia.html',
    controller: 'IaCtrl'
  });
}])

.controller('IaCtrl', [function() {

}]);