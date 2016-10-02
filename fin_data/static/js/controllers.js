var DataControllers = angular.module('finDataControllers', [])

DataControllers.controller('finDataController', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){
        $http.get('http://127.0.0.1:8000/api/v1/financedata' + '/?format=json').success(function(data){
            $scope.finance = data
        });
    }
]);