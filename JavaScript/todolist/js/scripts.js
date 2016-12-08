function addItem(){
    var newItem = document.getElementById("input").value;
    if (newItem == "") {
        alert("THERE IS NOTHING TO ADD BUDDY!");
        throw new Error();
    };
    var table = document.getElementById("toDoTable");
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    var cell1 = row.insertCell(0);
    var element1 = document.createElement("input");
    element1.type = "checkbox";
    element1.name="chkbox[]";
    cell1.appendChild(element1);

    var cell2 = row.insertCell(1);
    var newText = document.createTextNode(newItem);
    cell2.appendChild(newText);

    var cell3 = row.insertCell(2);

    var date = new Date();

    var dayName = dayFinder();
    function dayFinder() {
        var days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
        var dayInd = date.getDay();
        return days[dayInd - 1];
    };
    var monthName = monthFinder();
    function monthFinder() {
        var months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"];
        var monthNum = date.getMonth();
        return months[monthNum];
    };
    
    var day = date.getDate();
    var year = date.getFullYear();
    var hour = date.getHours();
    var min = date.getMinutes();
    hour = checkZero(hour);
    min = checkZero(min);

    var timetext = dayName + ", " + day + " " + monthName
    + " " + year + ", " + hour + ":" + min;
    var newDate = document.createTextNode(timetext);
    cell3.appendChild(newDate);
    
    document.getElementById("input").value = "";
};

function checkZero(i) {
    if (i < 10) {i = "0" + i};
    return i;
};

function removeItem() {
    try {
    var table = document.getElementById("toDoTable");
    var rowCount = table.rows.length;

    for(var i=0; i<rowCount; i++) {
        var row = table.rows[i];
        var chkbox = row.cells[0].childNodes[0];
        if(chkbox != null && chkbox.checked == true) {
            table.deleteRow(i);
            rowCount--;
            i--;
        };
    };
    } catch(e) {
        alert('Failure ' + e.name + ":" + e.message + "\n" + e.stack);
    };
};

function search() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("mySearch");
    filter = input.value.toUpperCase();
    table = document.getElementById("toDoTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            } else {
            tr[i].style.display = "none";
            };
        };
    };
};

