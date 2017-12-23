angular
    .module('app')
    .controller('loginController', loginController);

function loginController() { 
    var vm = this;
    vm.name = "HELLO";

    
    vm.login = function() {
        window.location.href = "https://api.imgur.com/oauth2/authorize?client_id=" + "CLIENT_ID_HERE" + "&response_type=token"
    }
}