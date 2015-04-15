'use strict';

/* Filters */

angular.module('travelIQFilters', []).filter('uppercase', function() {
	return function(input) {
		return input.toUpperCase();
	}
});