heroSelector = new function () {

    var mainTb = document.querySelector("#heroList");
    var mainTr = document.createElement("tr");
    
    var nameArray = ["abathur", "anubarak", "artanis", "arthas", "azmodan", "brightwing", "chen",
    "chogall", "chromie", "dehaka", "diablo", "etc", "falstad", "gazlowe", "greymane", "illidan",
    "jaina", "johanna", "kaelthas", "kerrigan", "kharazim", "leoric", "li-ming",
    "lili", "lt-morales", "lunara", "malfurion", "muradin", "murky", "nazeebo",
    "nova", "raynor", "rehgar", "rexxar", "sgt-hammer", "sonya", "stitches", "sylvanas",
    "tassadar", "the-butcher", "the-lost-vikings", "thrall", "tracer", "tychus",
    "tyrael", "tyrande", "uther", "valla", "xul", "zagara", "zeratul"];

    
    
    
    for (name in nameArray) {

        var names = nameArray[name];

        x += 1;
        img.src = "http://us.battle.net/heroes/static/images/heroes/busts/" + names + ".jpg";
        img.height = "40";
        img.width = "40";
        img.className = "img-circle";

        var imageTd = document.createElement("td");
        imageTd.appendChild(img);
        
        var nameTd = document.createElement("td");
        nameTd.innerHTML(names)
    }

};