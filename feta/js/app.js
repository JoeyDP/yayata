var KanBanModule = angular.module('Yata', ['YataServices', ,'ngRoute','ngCookies','ngSanitize'])
.config(['$routeProvider', '$resourceProvider', '$httpProvider', function($routeProvider, $resourceProvider,$httpProvider) {
     $resourceProvider.defaults.stripTrailingSlashes = false;
     $httpProvider.interceptors.push('httpInterceptor');

     $routeProvider.
         when('/timesheet/new', {templateUrl: yataUrls['timesheet_new'], controller: TimesheetNewCtrl}).
         when('/timesheet/:timesheetId', {templateUrl: yataUrls['timesheet_view'], controller: TimesheetViewCtrl}).
         when('/login', {templateUrl: yataUrls['login_view'], controller: LoginCtrl}).
         when('/logout', {templateUrl: yataUrls['logout_view'], controller: LogoutCtrl}).
         when('/timesheets', {templateUrl: yataUrls['timesheet_list'], controller: TimesheetListCtrl}).
         when('/companies', {templateUrl: yataUrls['company_list'], controller: CompanyListCtrl}).
         otherwise({ redirectTo: '/timesheets' });
 }])
.run(function (api) {
      api.init();
}).run(function ($rootScope){
    $rootScope.errors = [];
})
//.config(['$locationProvider', function($locationProvider) {
//      $locationProvider.html5Mode(true).hashPrefix('!');
//}])
;
