var num = '';
var oper = '';
var check = false;
var result = '';

var selectVal = function(number) {
    if(check){
        del();
        check = false;
    }
    document.getElementById("input").value = document.getElementById("input").value + number;
};

var delAll = function() {
    document.getElementById("input").value = "";
    num = '';
    oper = '';
};

var del = function() {
    document.getElementById("input").value = "";
};

var doSomething = function(op) {
    if (num != '' && oper != ''){
        execute();
        oper = op;
        num = document.getElementById("input").value;
        result = '';
    }
    else {
        oper = op;
        num = document.getElementById("input").value;
    }
    check = true;
};

var execute = function() {
    num = Number(num);
    nextNum = document.getElementById("input").value;
    nextNum = Number(nextNum)
    del();
    if (oper === "÷"){
        result = num / nextNum;
    }
    else if (oper === "x"){
        result = num * nextNum;
    }
    else if (oper === "-"){
        result = num - nextNum;
    }
    else if (oper === "+"){
        result = num + nextNum;
    }
    selectVal(result);
    oper = '';
}



