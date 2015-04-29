'use strict';

angular.module('travelIQServices', ['ngResource'])
	.factory('SearchAPI', function($resource) {
		return $resource('/search', {}, {
			query: {
				method: 'POST',
				isArray: true
			}
		});
	})
;