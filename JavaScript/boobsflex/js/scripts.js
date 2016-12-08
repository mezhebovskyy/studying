function refresh() {
    var elem = document.getElementById("flexCont");
    elem.innerHTML = '';

    $.getJSON("http://api.oboobs.ru/noise/20/", function(data) {
    data.forEach(function (obj) {
        var img = new Image();
        img.src = "http://media.oboobs.ru/" + obj.preview;
        img.setAttribute("class", "demo");
        return newItem(img);
        });
    });

    function newItem(img) {
        var ul = document.getElementById("flexCont");
        var li = document.createElement("li");
        li.setAttribute("class", "flex-item");
        li.appendChild(img);
        ul.appendChild(li);
    };
};






