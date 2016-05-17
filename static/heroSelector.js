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
        img.height = "90";
        img.width = "75";
        img.className = "img-circle";

        var alliedImageTd = document.createElement("td");
        alliedImageTd.appendChild(img);
        var enemyImageTd = document.createElement("td");
        enemyImageTd.appendChild(img);


        var alliedNameTd = document.createElement("td");
        alliedNameTd.innerHTML = names;
        var enemyNameTd = document.createElement("td");
        enemyNameTd.innerHTML = names;


        var newAlliedInputTd = document.createElement("td");
        var newEnemyInputTd = document.createElement("td");
        var newAlliedInput = document.createElement("input");
        var newEnemyInput = document.createElement("input");
        newAlliedInput.type = 'checkbox';
        newEnemyInput.type = 'checkbox';
        newAlliedInput.setAttribute('value', names);
        newEnemyInput.setAttribute('value', names);
        newAlliedInput.setAttribute('onClick', "heroProfileDisplay({{username}});");
        newEnemyInput.setAttribute('onClick', "heroProfileDisplay({{username}});");

        var spacerTd = document.createElement("td");
        newTr.appendChild(spacerTd);

        newAlliedInputTd.appendChild(newAlliedInput);
        newTr.appendChild(newAlliedInputTd);

        //newTr.appendChild(alliedImageTd);
        //newTr.appendChild(alliedNameTd);

        newTr.appendChild(enemyImageTd);
        newTr.appendChild(enemyNameTd);

        newEnemyInputTd.appendChild(newEnemyInput);
        newTr.appendChild(newEnemyInputTd);

        mainTb.appendChild(newTr);
    }
};