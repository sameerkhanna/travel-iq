'use strict';

/* Controllers */

TravelIQ.controller('searchCtrl', ['$scope', '$location', function($scope, $location) {
	$scope.searchTerm = $location.search().q;
	$scope.results = [];
	$scope.filters = [
		{
			"Atmosphere": [
				{
					"label": "Loud",
					"id": "loud"
				},
				{
					"label": "Relaxed",
					"id": "relaxed"
				},
				{
					"label": "Friendly",
					"id": "friendly"
				}
			]
		},
		{
			"Envrionment": [
				{
					"label": "Outdoor",
					"id": "outdoor"
				},
				{
					"label": "Indoor",
					"id": "Indoor"
				}
			]
		},
		{
			"Social": [
				{
					"label": "Solo",
					"id": "solo"
				},
				{
					"label": "Couple",
					"id": "couple"
				},
				{
					"label": "Group",
					"id": "group"
				}
			]
		}
	]

	$scope.search = function() {
		console.log('true');
		$scope.results = [1];
    	$location.search({'q': $scope.searchTerm});
  	};
}]);
