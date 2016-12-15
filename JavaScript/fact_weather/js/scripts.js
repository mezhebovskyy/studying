var fact = function (){
    function getInitials(){
        var number = Math.floor(Math.random() * 250) + 1;
        var adress = "http://numbersapi.com/" + number;
        return {
            number:number,
            adress:adress
        };
    }

    function getFact(adress, callback){
        var promise = $.get(adress);
        promise.then(function(data) {
            callback(data);
            promise = $.get("http://api.openweathermap.org/data/2.5/weather?q={London}&units=metric&APPID=9c92e78ddecd10ddce5a86a369282183");
            promise.then(function(data) {
                callback(data);
            });
        });
    }

    return {
        getInitials: getInitials,
        getFact: getFact
    }
}();

var insert = function(){
    var data = fact.getInitials();
    fact.getFact(data.adress, function (item) {
        console.log(item);
    });
};
