heroSelector = new function () {

    var mainTb = document.querySelector("#heroList");

    var nameArray = ["abathur", "anubarak", "artanis", "arthas", "azmodan", "brightwing", "chen",
    "chogall", "chromie", "dehaka", "diablo", "etc", "falstad", "gazlowe", "greymane", "illidan",
    "jaina", "johanna", "kaelthas", "kerrigan", "kharazim", "leoric", "li-ming",
    "lili", "lt-morales", "lunara", "malfurion", "muradin", "murky", "nazeebo",
    "nova", "raynor", "rehgar", "rexxar", "sgt-hammer", "sonya", "stitches", "sylvanas",
    "tassadar", "the-butcher", "the-lost-vikings", "thrall", "tracer", "tychus",
    "tyrael", "tyrande", "uther", "valla", "xul", "zagara", "zeratul"];

    for (name in nameArray) {
        var newTr = document.createElement("tr");
        var names = nameArray[name];

        var img = document.createElement("img");

        img.src = "http://us.battle.net/heroes/static/images/heroes/busts/" + names + ".jpg";
        img.height = "50";
        img.width = "50";
        img.className = "img-circle";

        var imageTd = document.createElement("td");
        imageTd.appendChild(img);

        var nameTd = document.createElement("td");
        nameTd.innerHTML = names;

        var newInputTd = document.createElement("td");
        var newInput = document.createElement("input");
        newInput.type = "checkbox";
        newInput.setAttribute('value', names);
        newInput.setAttribute('onClick', "heroProfileDisplay({{ username }});");


        newTr.appendChild(imageTd);
        newTr.appendChild(nameTd);
        newInputTd.appendChild(newInput);
        newTr.appendChild(newInputTd);
        mainTb.appendChild(newTr);
    }
};