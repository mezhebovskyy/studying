'use strict';
var findUtilities = function (){
    function findMouse(args){
        return {
            x: args.pageX,
            y: args.pageY
        };
    }

    function findElementByAttr(attribute, tag1){
        var inputbox = null;
        var textElements = document.getElementsByTagName(tag1);
        
        for(var i = 0, n = textElements.length; i < n; i++){
            if (textElements[i].getAttribute(attribute) !== null){
                inputbox = textElements[i];
            }
        }
        return inputbox;
    }

    return {
        findMouse: findMouse,
        findElementByAttr: findElementByAttr
    };
}();

function positionInput(mouse, inputBox){
    var x = mouse.x;
    var y = mouse.y;
    inputBox.value = "x position = " + x + ", " + "y position = " + y;
};

function main(args){
    var attribute = 'myvalue';
    var tag1 = 'input';
    var mouse = findUtilities.findMouse(args);
    var inputBox = findUtilities.findElementByAttr(attribute, tag1);
    positionInput(mouse, inputBox);
};

