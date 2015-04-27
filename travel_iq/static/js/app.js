'use strict';

window.TravelIQ = angular.module('TravelIQ', ['travelIQServices'],
  ['$locationProvider', function($locationProvider) {
    $locationProvider.html5Mode(true);
  }]
);