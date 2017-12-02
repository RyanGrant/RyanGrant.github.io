var app = angular.module('App', ['ngAnimate', 'ui.bootstrap', 'ngCookies'])
    .controller('mainController', ['$cookies',
        function ($cookies) {
            var vm = this;
            //console.log(vm.weaponList);
            vm.init = function () {
                //console.log($cookies.getAll());
                var cookies = $cookies.get('weaponList');
                if (cookies == undefined) {
                    //console.log("Initial Setup");
                    vm.initialSetup();
                }
                else {
                    //console.log("Loaded cookies");
                    //console.log(cookies);
                    vm.initialSetup();
                    var cookieWeapons = $cookies.get('weaponList');
                    var cookieHunter = $cookies.get('hunterList');
                    var cookieWarlock = $cookies.get('warlockList');
                    var cookieTitan = $cookies.get('titanList');
                    var cookieShip = $cookies.get('shipList');
                    var cookieVehicle = $cookies.get('vehicleList');
                    var cookieEmote = $cookies.get('emoteList');

                    for (i = 0; i < vm.weaponList.length; i++) {
                        if (cookieWeapons[i] == '1') {
                            vm.weaponList[i].active = true;
                        }
                        else {
                            vm.weaponList[i].active = false;

                        }
                    } for (i = 0; i < vm.hunterList.length; i++) {
                        if (cookieHunter[i] == '1') {
                            vm.hunterList[i].active = true;
                        }
                        else {
                            vm.hunterList[i].active = false;

                        }
                    } for (i = 0; i < vm.warlockList.length; i++) {
                        if (cookieWarlock[i] == '1') {
                            vm.warlockList[i].active = true;
                        }
                        else {
                            vm.warlockList[i].active = false;

                        }
                    } for (i = 0; i < vm.titanList.length; i++) {
                        if (cookieTitan[i] == '1') {
                            vm.titanList[i].active = true;
                        }
                        else {
                            vm.titanList[i].active = false;

                        }
                    } for (i = 0; i < vm.shipList.length; i++) {
                        if (cookieShip[i] == '1') {
                            vm.shipList[i].active = true;
                        }
                        else {
                            vm.shipList[i].active = false;

                        }
                    } for (i = 0; i < vm.vehicleList.length; i++) {
                        if (cookieVehicle[i] == '1') {
                            vm.vehicleList[i].active = true;
                        }
                        else {
                            vm.vehicleList[i].active = false;

                        }
                    } for (i = 0; i < vm.emoteList.length; i++) {
                        if (cookieEmote[i] == '1') {
                            vm.emoteList[i].active = true;
                        }
                        else {
                            vm.emoteList[i].active = false;

                        }
                    }
                }
            };

            vm.toggle = function (item) {
                item.active = !item.active;
                var cookieWeapons = "";
                var cookieHunter = "";
                var cookieWarlock = "";
                var cookieTitan = "";

                for (i = 0; i < vm.weaponList.length; i++) {
                    if (vm.weaponList[i].active) {
                        cookieWeapons += '1';
                    }
                    else {
                        cookieWeapons += '0';

                    }
                } for (i = 0; i < vm.hunterList.length; i++) {
                    if (vm.hunterList[i].active) {
                        cookieHunter += '1';
                    }
                    else {
                        cookieHunter += '0';

                    }
                } for (i = 0; i < vm.warlockList.length; i++) {
                    if (vm.warlockList[i].active) {
                        cookieWarlock += '1';
                    }
                    else {
                        cookieWarlock += '0';

                    }
                } for (i = 0; i < vm.titanList.length; i++) {
                    if (vm.titanList[i].active) {
                        cookieTitan += '1';
                    }
                    else {
                        cookieTitan += '0';

                    }
                } for (i = 0; i < vm.shipList.length; i++) {
                    if (vm.shipList[i].active) {
                        cookieShip += '1';
                    }
                    else {
                        cookieShip += '0';

                    }
                } for (i = 0; i < vm.vehicleList.length; i++) {
                    if (vm.vehicleList[i].active) {
                        cookieVehicle += '1';
                    }
                    else {
                        cookieVehicle += '0';

                    }
                } for (i = 0; i < vm.emoteList.length; i++) {
                    if (vm.emoteList[i].active) {
                        cookieEmote += '1';
                    }
                    else {
                        cookieEmote += '0';

                    }
                }
                $cookies.put('weaponList', cookieWeapons);
                $cookies.put('hunterList', cookieHunter);
                $cookies.put('warlockList', cookieWarlock);
                $cookies.put('titanList', cookieTitan);
            	$cookies.put('shipList', cookieShip);
            	$cookies.put('emoteList', cookieEmote);
            	$cookies.put('vehicleList', cookieVehicle);
            }

            vm.initialSetup = function () {
                vm.weaponList = exoticWeaponList;
                vm.hunterList = exoticHunterArmorList;
                vm.warlockList = exoticWarlockArmorList;
                vm.titanList = exoticTitanArmorList;
		vm.shipList = exoticShipList;
		vm.emoteList = exoticEmoteList;
		vm.vehicleList = exoticVehicleList;
            }
    }]
)