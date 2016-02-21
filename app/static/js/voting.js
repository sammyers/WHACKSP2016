/* Will  iterate through the list of values and then prompt the user to choose one
will continue to iterate until the list is exhausted, after which it will load a rankings page
*/



var testing = [(1,2),(3,4),(4,5)];
var index = 0;
var combos = [];

$(document).ready(function(jsonlist){

	
	for(i = 0; i < Object.keys(jsonlist).length-1; i++){
		for(k = i+1; k < Object.keys(jsonlist).length; k++){
			var pair = [0,0];
			pair[0] = jsonlist[i];
			pair[1] = jsonlist[k];
			combos.push(pair);

		}
	}

	pairvoting(combos);

});

var pairvoting = function (combinations){


	if(index >= combinations.length){
		windows.location.href="/rankings";
	} 
	var lefthtml = combination[i][0];
	var righthtml = combination[i][1];

	document.getElementById("yeet").innerHTML = lefthtml;
	document.getElementById("peet").innerHTML = righthtml;

	index++;


	
}

var update = function(winner){


	pairvoting(combos);


}

$("#yeet").click(update(document.getElementById("yeet").innerHTML));
$("#peet").click(update(document.getElementById("peet").innerHTML));