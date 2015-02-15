function concatMonth(data){
    if (data) {
        month = parseInt(data.monthonly)+1;
        data.month=data.year+"-" + month + "-01";
        if (!data.year){delete(data.month);}
        if (data) {
            return angular.toJson(data);
        }
    }
}

angular.module('YataServices', ['ngResource', 'ngSanitize']).
factory('api', function ($http, $cookies, Me, $rootScope) {
    return {
        init: function (token) {
            token = token || $cookies.token;
            if (token) {$http.defaults.headers.common['Authorization'] = "Token " + token;}
            else if ($http.defaults.headers.common['Authorization']){delete($http.defaults.headers.common['Authorization'])}
            $rootScope.user = Me.get();
        }
    }
}).
factory('httpInterceptor', function ($q, $window, $location, $cookieStore) {
    return {
     'responseError': function(response) {
            if (response.status === 401) {
                $cookieStore.remove('token');
                $location.url('/login');
            }
            return $q.reject(response);
      }
    };
}).
factory('Me', function($resource){
    return $resource(BetaApiUrl + 'me/', {}, {
        get: {method:'GET'}
    });
}).
factory('Login', function($resource){
    return $resource(BetaApiUrl + 'token/', {}, {
        login: {method:'POST'}
    });
}).
factory('Project', function($resource){
    return $resource(BetaApiUrl + 'projects/:projectId', {}, {
        query: {method:'GET', params:{projectId:''}, isArray:true},
        get: {method:'GET', params:{projectId:''}, isArray:true}
    });
}).
factory('Company', function($resource){
    return $resource(BetaApiUrl + 'companies/:companyId', {}, {
        query: {method:'GET', params:{companyId:''}, isArray:true},
        get: {method:'GET', params:{companyId:''}, isArray:true}
    });
}).
factory('Customer', function($resource){
    return $resource(BetaApiUrl + 'customers/:customerId', {}, {
        query: {method:'GET', params:{customerId:''}, isArray:true},
        get: {method:'GET', params:{customerId:''}, isArray:true}
    });
}).
factory('Timesheet', function($resource){
    return $resource(BetaApiUrl + 'timesheets/:timesheetId/', {}, {
        query: {method:'GET', url:BetaApiUrl + 'timesheets/', isArray:true},
        get: {method:'GET', params:{timesheetId:''}},
        create: {method:'POST', isArray:false, transformRequest:concatMonth}
    });
});

