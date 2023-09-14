

function searchSong(){
    // get data from input elements
    var songName = document.getElementById("song").value;
    var artistName = document.getElementById("artist").value;
    var inputString  = '\"'+songName+'\" \"'+artistName+'\"';
    console.log(inputString);


    // alert(response);


    // retrieve data from output file
    // fileData=readTextFile("mood.txt");
    fileData="sad \nd9c5f0"
    moodData=fileData.split(/\r?\n/);
    // console.log(moodData);
    moodValue = moodData[0];
    colorValue = '#'+moodData[1];

    var moodText = document.getElementById("mood");
    var square = document.getElementById("square");

    moodText.innerHTML = moodValue;
    moodText.style.color="#977b31";
    square.style.backgroundColor=colorValue;
    

    console.log(moodValue+" "+colorValue)
    
}

function readTextFile(file){
    var output ="";
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function (){
        if(rawFile.readyState === 4){
            if(rawFile.status === 200 || rawFile.status == 0){
                output = rawFile.responseText;
            }
        }
    }
    rawFile.send(null);
    console.log(output);
    return output;
}

