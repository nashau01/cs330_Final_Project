heroSelector = new function (user) {

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
        newAlliedInput.onclick = doAllyCheck;
        newEnemyInput.onclick = doEnemyCheck;
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


function doAllyCheck() {
    //alert(this.id + " : " + this.checked);
    // PUT - /todo/<int:id>
    // Create JSON- {'done' : true}
    // xmlhttp.send(data)

    var cb = this;

    if (this.checked == true) {
        var req = new XMLHttpRequest();
        window.alert(this.value);
        req.open("GET", "/addAlly/" + this.value, true);
        req.setRequestHeader("Content-type", "application/json");
        req.onreadystatechange = function() {
            if(req.readyState == 4 && req.status == 200) {
                optArray = [];
                optDict = JSON.parse(req.responseText);
                for(hero in optDict) {
                    optArray.append(optDict[hero])
                }
                window.alert(optArray);
            }
        };

        req.send()
    }
}




/*<script type="text/javascript">
    function heroProfileDisplay(user) {
        window.alert(user);
        var req = new XMLHttpRequest();
        req.open("GET", "/getHeroes/" + user, true);
        req.onreadystatechange = function() {
            if (req.readyState == 4 && req.status == 200) {
                heroesDict = JSON.parse(req.responseText);
                window.alert("HeroDict:" + heroesDict);
                for(hero in heroesDict){
                    window.alert("heroList:" + heroesDict[hero]);
                }
            }
        };
        req.send()
    }
</script> */

// function doEnemyCheck() {
// }
