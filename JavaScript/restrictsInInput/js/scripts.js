var find = function (){

    function findNotif(attribute, tag2){
        var notif = null;
        var htmlElement = document.getElementsByTagName(tag2);
        for (var i = 0, n = htmlElement.length; i < n; i++){
            if (htmlElement[i].getAttribute(attribute) !== null){
                notif = htmlElement[i];
            };
        };
        return {
            notification: notif
        };
    };


    function findTextElements(attribute, tag1){
        var maintext = "";
        var inputbox = null;
        var textElements = document.getElementsByTagName(tag1);
        for (var i = 0, n = textElements.length; i < n; i++){
            if (textElements[i].getAttribute(attribute) !== null){
                maintext = textElements[i].value;
                inputbox = textElements[i];
            }; 
        };
        return {
            text: maintext,
            input: inputbox
        };
    };
    return {
        findNotif: findNotif,
        findTextElements: findTextElements
    };
}();


function main(value){
    var attribute = 'myvalue';
    var tag1 = 'input';
    var tag2 = 'p';
    var notif = find.findNotif(attribute, tag2).notification;
    var text = find.findTextElements(attribute, tag1).text;
    var inputBox = find.findTextElements(attribute, tag1).input;
    checkLetters(notif, text, inputBox);
};


function checkLetters(notif, text, inputBox){
    var regex=/^[0-9]+$/;
    if (text === ""){
        inputBox.style.borderColor = "green";
        inputBox.style.borderWidth = "1px";
    } else if (!text.match(regex)) {
        notif.innerHTML = "Type a number!";
        inputBox.style.borderColor = "red";
        inputBox.style.borderWidth = "2px";
        text = text.slice(0, -1);
        inputBox.value = text;
    } else {
        notif.innerHTML = "Type a number.";
        inputBox.style.borderColor = "green";
        inputBox.style.borderWidth = "1px";
    };
};



