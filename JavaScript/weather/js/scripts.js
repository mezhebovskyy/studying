var locationModule = function getLocation() {
    function nav(callback){
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(callback);
        } else {
            document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    return {
        location: nav
    }
}();

var url = function(){
    function urlMainParts(lat, lon){
        var initurl = "http://api.openweathermap.org/data/2.5/weather?";
        var api = "&APPID=9c92e78ddecd10ddce5a86a369282183";
        return urlBuilder(initurl, api, lat, lon)
    }
    function urlBuilder(initurl, api, lat, lon){
        var mainUrl = initurl + "lat=" + lat + "&lon=" + lon + "&units=metric" + api;
        return mainUrl;
    }

    return {
        getUrl: urlMainParts
    }
}();

var mainModule = function(){
    function getPath(){
        locationModule.location(function(resp){
            // var apprlat = +resp.coords.latitude;
            // var apprlon = +resp.coords.longitude;
            // var lat = apprlat.toFixed(20);
            // var lon = apprlon.toFixed(20);
            var path = url.getUrl(lat, lon);
            console.log(path);    
        });
    }

    return {
        getPath: getPath
    }
}();


mainModule.getPath();



// function getJSONP(url, success) {
//     var ud = '_' + +new Date,
//         script = document.createElement('script'),
//         head = document.getElementsByTagName('head')[0] 
//                || document.documentElement;

//     window[ud] = function(data) {
//         head.removeChild(script);
//         success && success(data);
//     };
//     script.src = url.replace('callback=?', 'callback=' + ud);
//     head.appendChild(script);
// }

// getJSONP('http://soundcloud.com/oembed?url=http%3A//soundcloud.com/forss/flickermood&format=js&callback=?', function(data){
//     console.log(data);
// });  