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
        });
    }

    return {
        getInitials: getInitials,
        getFact: getFact
    }
}();

var insert = function(){
    var facts = [];
    var callCount = 0;
    while (callCount < 100) {
        var data = fact.getInitials();
        fact.getFact(data.adress, function (z) {
            facts.push(z);
            if (facts.length == 100){
                console.log(facts);
            };
        });
        callCount += 1;
    }
};

