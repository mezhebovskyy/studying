var phonePrice = 250;
var accPrice = 25;
var taxRate = 0.05;
var balance = 1200;
var totalPurchases = 0;

function buyPhone(){
    while (true){
        var fullPrice = (phonePrice + accPrice) + (phonePrice + accPrice) * taxRate;
        fullPrice = fullPrice.toFixed(2);
        if ((balance - fullPrice) > 0) {
            balance = balance - fullPrice;
            totalPurchases += 1;
        } else {
            console.log(totalPurchases);
            break;
        };
    };
}

buyPhone();