angular
    .module('app')
    .controller('secureController', secureController);

function secureController() { 
    var vm = this;
    vm.name = "HELLO";

    vm.accessToken = JSON.parse(window.localStorage.getItem("imgur")).oauth.access_token;

}