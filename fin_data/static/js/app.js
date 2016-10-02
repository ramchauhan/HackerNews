var fin_module = angular.module("finApp", ['ngRoute'])

//var fin_module = angular.module("finApp", ['ng-fusioncharts'])

fin_module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/findata', {
                templateUrl: static_url + 'html/fin_list.html',
                controller: 'finDataController'
            });
}]);

fin_module.config(['$httpProvider',
    function($httpProvider){
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    }
]);

//fin_module.config(['ChartJsProvider', function (ChartJsProvider) {
//    // Configure all charts
//    ChartJsProvider.setOptions({
//        colours: ['#FF5252', '#FF8A80'],
//        responsive: false
//    });
//    // Configure all line charts
//    ChartJsProvider.setOptions('Line', {
//        datasetFill: false
//    });
// }]);

fin_module.controller('finDataController', ['$scope', '$http',
    function($scope, $http){
        $http.get(api_end_point + '/?format=json').success(function(data){
            $scope.finance = data
        });
    }
]);

//fin_module.controller("LineCtrl", ['$scope', '$timeout',
//    function ($scope, $timeout) {
//        $scope.labels = ["January", "February", "March", "April", "May", "June", "July"];
//        $scope.series = ['Series A', 'Series B'];
//        $scope.data = [
//            [65, 59, 80, 81, 56, 55, 40],
//            [28, 48, 40, 19, 86, 27, 90]
//        ];
//        $scope.onClick = function (points, evt) {
//            console.log(points, evt);
//        };
//        // Simulate async data update
//        $timeout(function () {
//            $scope.data = [
//                [28, 48, 40, 19, 86, 27, 90],
//                [65, 59, 80, 81, 56, 55, 40]
//            ];
//        }, 3000);
//}]);
