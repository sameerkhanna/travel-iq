'use strict';

angular.module('TravelIQ', ['travelIQServices', 'ngRoute'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/landing.html',
			controller: IndexController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		//$locationProvider.html5Mode(true);
	}])
;