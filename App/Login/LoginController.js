angular
    .module('app')
    .controller('loginController', loginController);

function loginController() { 
    var vm = this;
    vm.name = "HELLO";

    
    vm.login = function() {
        window.location.href = "https://www.bungie.net/en/OAuth/Authorize?client_id=" + "22434" + "&response_type=code"
    }
}