var temporaryPlace = [];

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 48.456849, lng: 35.061943},
        zoom: 13
    });
    
    var input = document.getElementById('inputField');

    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var infowindow = new google.maps.InfoWindow();
    var marker = new google.maps.Marker({
        map: map
    });

    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });

    autocomplete.addListener('place_changed', function() {
        infowindow.close();
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            return;
        }
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
            temporaryPlace = [];
            temporaryPlace.push(place.id, place.formatted_address, place.geometry.location.lat(), place.geometry.location.lng());
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
            temporaryPlace = [];
            temporaryPlace.push(place.id, place.formatted_address, place.geometry.location.lat(), place.geometry.location.lng());
        }

        marker.setPlace({
            placeId: place.place_id,
            location: place.geometry.location
        });
        marker.setVisible(true);

        infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + '<br>' + place.formatted_address);
        infowindow.open(map, marker);
    });
}

function PlaceData(placeID, adress, lat, lng, checked) {
    var self = this;

    self.placeID = placeID;
    self.adress = adress;
    self.lat = lat;
    self.lng = lng;
    self.checked = checked;
}

function PlacesViewModel(){
    var self = this;

  // Editable data
    self.places = ko.observableArray([]);

    // Operations
    self.addPlace = function() {
        self.places.push(new PlaceData(temporaryPlace[0], temporaryPlace[1], temporaryPlace[2], temporaryPlace[3], false));
    };
}







// function savePosition() {
// 	savedPlaces.push(temporaryPlace);
// 	var table = document.getElementById("addressTable");
// 	var rowCount = table.rows.length;
// 	var row = table.insertRow(rowCount);

// 	var cell1 = row.insertCell(0);
// 	var element1 = document.createElement("input");
// 	element1.type = "checkbox";
// 	element1.name="chkbox[]";
// 	cell1.appendChild(element1);

// 	var cell2 = row.insertCell(1);
// 	var newAddress = document.createTextNode(temporaryPlace[1]);
// 	cell2.appendChild(newAddress);

// 	var cell3 = row.insertCell(2);
// 	var element2 = document.createElement("input");
// 	element2.type = "checkbox";
// 	element2.name="chkbox[]";
// 	element2.onchange="chkboxCheck()";
// 	cell3.appendChild(element2);
// }



// function callback(results, status) {
//   if (status == google.maps.places.PlacesServiceStatus.OK) {
//     var marker = new google.maps.Marker({
//       map: map,
//       place: {
//         placeId: results[0].place_id,
//         location: results[0].geometry.location
//       }
//     });
//   }
// }


ko.applyBindings(new PlacesViewModel());