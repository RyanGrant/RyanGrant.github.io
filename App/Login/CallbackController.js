angular
    .module('app')
    .controller('callbackController', callbackController);

function callbackController($http) { 
    var vm = this;
    vm.name = "HELLO";

	var callbackCode = (document.URL).split("=")[1];

	//https://www.bungie.net/en/OAuth/Authorize?client_id=22434&response_type=code
	//https://www.bungie.net/Platform/App/OAuth/Token/client_id=22434&grant_type=authorization_code&code=2fa0f60eb62ebf5f3a2e5111cb26e4c3
  
	var req = {
		method: 'POST',
		url: 'https://www.bungie.net/Platform/App/OAuth/Token/',
		headers: { 
			'Content-Type': 'application/x-www-form-urlencoded' 
		},
		data: { 
			client_id: '22434',
			grant_type: 'authorization_code',
			code: callbackCode
		}
	}
	console.log(req);
	$http(req).then(function successCallback(response) {
		console.log("success");
	console.log(response);
  }, function errorCallback(response) {
	  console.log("fail");
	console.log(response);
  });	
/*
            var responseParameters = (callbackResponse).split("&");
            var parameterMap = [];
            for(var i = 0; i < responseParameters.length; i++) {
                parameterMap[responseParameters[i].split("=")[0]] = responseParameters[i].split("=")[1];
            }
            if(parameterMap.access_token !== undefined && parameterMap.access_token !== null) {
                var imgur = {
                    oauth: {
                        access_token: parameterMap.access_token,
                        expires_in: parameterMap.expires_in,
                        account_username: parameterMap.account_username
                    }
                };
                window.localStorage.setItem("imgur", JSON.stringify(imgur));
                window.location.href = "http://localhost/App/Login/Secure.html";
            } else {
                alert("Problem authenticating");
            }
*/

}