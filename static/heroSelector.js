heroSelector = new function () {

    var mainUl = document.querySelector("#heroList");
    
    var nameArray = ["abathur", "anubarak", "artanis", "arthas", "azmodan", "brightwing", "chen",
    "chogall", "chromie", "dehaka", "diablo", "etc", "falstad", "gazlowe", "greymane", "illidan",
    "jaina", "johanna", "kaelthas", "kerrigan", "kharazim", "leoric", "li-ming",
    "lili", "lt-morales", "lunara", "malfurion", "muradin", "murky", "nazeebo",
    "nova", "raynor", "rehgar", "rexxar", "sgt-hammer", "sonya", "stitches", "sylvanas",
    "tassadar", "the-butcher", "the-lost-vikings", "thrall", "tracer", "tychus",
    "tyrael", "tyrande", "uther", "valla", "xul", "zagara", "zeratul"];
            
    x = 0;
    for (name in nameArray) {
        if (x == 0) {
            var rowLi = document.createElement("li");
            var rowUl = document.createElement("ul");

            rowLi.className = "HeroRow"
        }

        var heroLi = document.createElement("li");
        var pictureWName = document.createElement("ul");
        var imgLi = document.createElement("li");
        var charNameLi = document.createElement("li");
        var img = document.createElement("img");
        var charName = document.createElement("Label");
        var names = nameArray[name];

        charName.innerHTML = names;

        x += 1;
        img.src = "http://us.battle.net/heroes/static/images/heroes/busts/" + names + ".jpg";
        img.height = "100";
        img.width = "100";
        img.className = "img-circle";


        imgLi.appendChild(img);
        imgLi.appendChild(document.createElement("br"));
        imgLi.appendChild(charName);

        pictureWName.appendChild(imgLi);
        pictureWName.className = "pictureWName";

        heroLi.appendChild(pictureWName);
        rowUl.appendChild(heroLi);
        rowLi.appendChild(rowUl);

        
        if (x == 8) {
            mainUl.appendChild(rowLi);
            x = 0;
        }
    }
    mainUl.appendChild(rowLi);
};