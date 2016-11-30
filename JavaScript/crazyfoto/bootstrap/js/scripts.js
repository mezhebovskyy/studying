function runaway() {
    var pic = document.getElementById("img01");
    var way = Math.floor((Math.random() * 4) + 1);
    var currentLeft = pic.style.left;
    var currentTop = pic.style.top;
    var numLeft = parseInt(currentLeft, 10);
    var numTop = parseInt(currentTop, 10);
    if (way == 1){
        pic.style.left = (numLeft - 151 <= 0) ? numLeft + 151 + "px" : numLeft - 151 + "px";
        pic.style.top = (numTop - 101 <= 0) ? numTop + 101 + "px" : numTop - 101 + "px";
    }
    else if (way == 2){
        pic.style.left = (numLeft + 151 >= 800) ? numLeft - 151 + "px" : numLeft + 151 + "px";
        pic.style.top = (numTop - 101 <= 0) ? numTop + 101 + "px" : numTop - 101 + "px";
    }
    else if (way == 3){
        pic.style.left = (numLeft - 151 <= 0) ? numLeft + 151 + "px" : numLeft - 151 + "px";
        pic.style.top = (numTop + 101 >= 750) ? numTop - 101 + "px" : numTop + 101 + "px";
    }
    else if (way == 4){
        pic.style.left = (numLeft + 151 >= 800) ? numLeft - 151 + "px" : numLeft + 151 + "px";
        pic.style.top = (numTop + 101 >= 750) ? numTop - 101 + "px" : numTop + 101 + "px";
    }
};