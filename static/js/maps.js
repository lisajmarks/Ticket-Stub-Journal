"use strict";

let map;

async function initMap() {
  // Map options
  let options = {
    zoom:8,
    center: { lat: -34.397, lng: 150.644 }
  }
  // New map 
  let map = new 
  google.maps.Map(document.getElementById("map"), options);
  
  let response = await fetch('/mapevents')

  let data = await response.json()
  console.log(data)
  
  // Add Marker 
  let marker = new google.maps.Marker({
    position: { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lng) },
    map:map, icon: '/static/img/concert.png'
  });

  // Add infoWindow 
  let infoWindow = new google.maps.InfoWindow({
    content:'<h1>Show Name</h1>'
  });

  marker.addListener('click', function(){
    infoWindow.open(map, marker)
  })

}