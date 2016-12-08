

var calcModule = function () {
    function Add(a, b){
        return a + b;
    }

    function Div(a, b){
        return AdditionalDiv(a,b);
    }

    function AdditionalDiv(a, b){
        return a / b + 0.00001;
    }

    return {
        add: Add,
        div: Div,
        pi: 3.14,
        someFunc: function(){
            return "Yo!"
        }
    }
}();

var result = calcModule.add(1,2); //3

console.log(calcModule.someFunc())