function findElement(attribute, tag1, tag2){
    var maintext = "";
    var allElements = document.getElementsByTagName(tag1);
    for (var i = 0, n = allElements.length; i < n; i++){
        if (allElements[i].getAttribute(attribute) !== null){
            maintext = allElements[i].value;
            return bindElements(attribute, maintext, tag2);
        };
    };
};

function bindElements(attribute, maintext, tag2){
    var htmlElement = document.getElementsByTagName(tag2);
    for (var i = 0, n = htmlElement.length; i < n; i++){
        if (htmlElement[i].getAttribute(attribute) !== null){
            htmlElement[i].innerHTML = maintext;
        };
    };
};

setInterval(function(){
    findElement('mybindvalue', 'input', 'h1');
}, 100);

