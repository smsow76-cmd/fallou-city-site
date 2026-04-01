const ads = [
    "Découvrez nos appartements modernes à Pikine !",
    "Achetez votre villa à prix exceptionnel à Mermoz !",
    "Locations abordables dans tout Dakar !",
    "Profitez de notre promotion spéciale cette semaine !"
];

let i = 0;
setInterval(() => {
    i = (i + 1) % ads.length;
    document.getElementById('ad-span').innerText = ads[i];
}, 5000);