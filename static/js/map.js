var map = L.map('map').setView([41.3111, 69.2797], 12);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Подключение кластеров
var markers = L.markerClusterGroup();

var masters = [
    { name: "Шерзод", lat: 41.315, lon: 69.28, profession: "Электрик", district: "Мирзо-Улугбек" },
    { name: "Ирина", lat: 41.309, lon: 69.275, profession: "Сантехник", district: "Юнусабад" },
    { name: "Фаррух", lat: 41.313, lon: 69.29, profession: "Автомастер", district: "Мирзо-Улугбек" }
];

function addMarkers(filterProfession = "", filterDistrict = "") {
    markers.clearLayers();
    masters.forEach(function(master) {
        if ((filterProfession === "" || master.profession === filterProfession) &&
            (filterDistrict === "" || master.district === filterDistrict)) {
            var marker = L.marker([master.lat, master.lon]);
            marker.bindPopup("<b>" + master.name + "</b><br>" + master.profession + "<br>" + master.district);
            markers.addLayer(marker);
        }
    });
    map.addLayer(markers);
}

addMarkers(); // По умолчанию показать всех
