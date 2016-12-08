function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(myPosition);
    } else {
        document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
    }
}

function myPosition(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    return urlBuilder(latitude, longitude);
}

function urlBuilder(lat, lon){
    var initurl = "http://api.openweathermap.org/data/2.5/weather?";
    var api = "&APPID=9c92e78ddecd10ddce5a86a369282183";
    mainUrl = initurl + "lat=" + lat + "&lon=" + lon + "&units=metric" + api;
    return getWeatherData(mainUrl);
}

function getWeatherData(mainUrl){
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET", mainUrl, true);
    Httpreq.send(null);
    return Httpreq.responseText;       
}
var json_obj = JSON.parse(getWeatherData());
// console.log("your latitude is: "+json_obj.latitude);
// console.log("your longitude is: "+json_obj.longitude);


// function httpGetAsync(geourl, callback)
// {
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.onreadystatechange = function() { 
//         if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
//             callback(xmlHttp.responseText);
//     }
//     xmlHttp.open("GET", geourl, true); // true for asynchronous 
//     xmlHttp.send(null);
// }