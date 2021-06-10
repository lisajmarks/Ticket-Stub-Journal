"use strict";

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
  new google.maps.Marker({
    position: { lat: -34.397, lng: 150.644 },
    map,
    title: "Hello World!",
  });
}
