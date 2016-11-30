
function onlineclock() {
    var time = new Date();
    var hour = time.getHours();
    var min = time.getMinutes();
    var sec = time.getSeconds();
    hour = checkZero(hour);
    min = checkZero(min);
    sec = checkZero(sec);
    document.getElementById("time").value = hour + ":" + min + ":" + sec;
};

setInterval(onlineclock, 500);

function checkZero(i) {
    if (i < 10) {i = "0" + i};
    return i;
};



