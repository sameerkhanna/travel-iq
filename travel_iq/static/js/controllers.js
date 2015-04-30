'use strict';

/* Controllers */

TravelIQ.controller('searchCtrl', ['$scope', '$location', 'SearchAPI', function($scope, $location, SearchAPI) {
	$scope.searchTerm = '';
	$scope.results = [];
	$scope.filters = {
		"atmosphere": ["loud", "relaxed", "friendly"],
		"environment": ["outdoor", "indoor"],
		"social": ["solo", "couple", "group"]
	};
	$scope.filterOptions = null;
	$scope.loaded = true;

	$scope.search = function(searchTerm) {
		$scope.searchTerm = searchTerm;
		$scope.results = [1];

		_search($scope.searchTerm, '');
  	};

  	$scope.filterResults = function(filterOptions) {
  		$scope.filterOptions = filterOptions;
  		_search($scope.searchTerm, $scope.filterOptions);
  	};

  	$scope.reset = function() {
  		var radioButtons = angular.element(document.querySelectorAll('input[type="radio"]'));
  		for (var i = 0; i < radioButtons.length; i++) {
  			radioButtons[i].checked = false;
  		}

  		$scope.filterOptions = null;
  		_search($scope.searchTerm, $scope.filterOptions);
  	};

  	function _search(q, filters) {
  		$scope.loaded = false;
  		SearchAPI.save({q: q, filters: filters}, function(res) {
  			if (res.result) {
  				$scope.results = res.result;
  			}
  			$scope.loaded = true;
		});
	}
}]);
