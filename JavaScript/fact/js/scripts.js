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
            var strArray = data.split(" ");
            var excluded = strArray.shift();
            var finalStr = strArray.join(" ");
            callback(finalStr);
        });
    }

    return {
        getInitials: getInitials,
        getFact: getFact
    }
}();

var insert = function(){
    var sectionNumber = document.getElementById("pInt");
    var sectionFact = document.getElementById("pStr");
    var data = fact.getInitials();

    sectionNumber.innerHTML = "";

    sectionFact.innerHTML = "Loading......";

    sectionNumber.innerHTML = data.number;

    fact.getFact(data.adress, function (z) {
        sectionFact.innerHTML = z;
    });
};