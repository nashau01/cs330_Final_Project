heroSelector = new function () {

    mainUl = document.querySelector("#heroList");
    window.alert("In the Function");
    
    nameArray = ["abathur", "anubarak", "artanis", "arthas", "azmodan", "brightwing", "chen",
    "chogall", "chromie", "dehaka", "diablo", "etc", "falstad", "gazlowe", "greymane", "illidan",
    "jaina", "johanna", "kaelthas", "kerrigan", "kharazim", "leoric", "li-ming",
    "lili", "lt-morales", "lunara", "malfurion", "muradin", "murky", "nazeebo",
    "nova", "raynor", "rehgar", "rexxar", "sgt-hammer", "sonya", "stitches", "sylvanas",
    "tassadar", "the-butcher", "the-lost-vikings", "thrall", "tracer", "tychus",
    "tyrael", "tyrande", "uther", "valla", "xul", "zagara", "zeratul"];
            
    x = 0;
    for (name in nameArray) {
        if (x == 0) {
            rowLi = document.createElement("li");
            rowUl = document.createElement("ul");

            rowLi.className = "HeroRow"
        }

        heroLi = document.createElement("li");
        img = document.createElement("img");

        x += 1;
        img.src = "http://us.battle.net/heroes/static/images/heroes/busts/" + nameArray[name] + ".jpg";
        img.height = "100";
        img.width = "100";
        img.className = "img-circle";


        heroLi.appendChild(img);
        rowUl.appendChild(heroLi);


        
        if (x%5 == 0) {
            rowLi.appendChild(rowUl);
            mainUl.appendChild(rowLi);
        }
    }
};