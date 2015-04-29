'use strict';

window.TravelIQ = angular.module('TravelIQ', ['travelIQServices', 'travelIQFilters', 'angular-loading-bar'],
  ['$locationProvider', function($locationProvider) {
    $locationProvider.html5Mode(true);
  }]
);