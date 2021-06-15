"use strict";

let map;

async function initMap() {
  // Map options
  let options = {
    zoom:8,
    center: { lat: 37.733795, lng: -122.446747 }
  }
  // New map 
  let map = new google.maps.Map(document.getElementById("map"), options);
  
  let response = await fetch('/mapevents')

  let data = await response.json()
  console.log(data)
  

  const markers = data.forEach(m => {

    
    const marker = new google.maps.Marker({
      position: { lat: parseFloat(m.lat), lng: parseFloat(m.lng) },
      map:map, icon: '/static/img/concert.png'
    });

    var contentString = '<div id="content">'+
		'<div id="siteNotice">'+
		'</div>'+
		`<h3 id="firstHeading" class="firstHeading">${m.name}</h3>`+
		'<p><div id="bodyContent">'+ `<div style="float:left; width:20%;"><img src="${m.pic_url}" width="120" height="80"/></div></p>` + 
		`<p> <div id = "picture"> <div style="float:left; width:100%; margin-top: -100px;">${m.venue_name}</p>` +
		'</div>'+
		'</div>';

      // Add infoWindow 
      const infoWindow = new google.maps.InfoWindow({
      content: contentString,
    });

    infoWindow.open(map, marker)

    marker.addListener('click', function(){
      if (isInfoWindowOpen(infoWindow)) {
        infoWindow.close()
      } else {
        infoWindow.open(map, marker)
      }
    })
  })

  // // Add Marker 
  // let marker = new google.maps.Marker({
  //   position: { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lng) },
  //   map:map, icon: '/static/img/concert.png'
  // });

  // // Add infoWindow 
  // let infoWindow = new google.maps.InfoWindow({
  //   content:'<h1>Show Name</h1>'
  // });

  // marker.addListener('click', function(){
  //   infoWindow.open(map, marker)
  // })

}

function isInfoWindowOpen(infoWindow){
  var map = infoWindow.getMap();
  return (map !== null && typeof map !== "undefined");
}
