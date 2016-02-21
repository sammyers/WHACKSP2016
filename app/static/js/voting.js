/* Will  iterate through the list of values and then prompt the user to choose one
will continue to iterate until the list is exhausted, after which it will load a rankings page
*/



var testing = [(1,2),(3,4),(4,5)];
var index = 0;
var combos = [];

$(document).ready(function(){

	var jsonlist = ideas
	for(i = 0; i < Object.keys(jsonlist).length-1; i++){
		for(k = i+1; k < Object.keys(jsonlist).length; k++){
			var pair = [0,0];

			pair[0] = jsonlist[Object.keys(jsonlist)[i]];
			pair[1] = jsonlist[Object.keys(jsonlist)[k]];

			combos.push(pair);

		}
	}

	pairvoting(combos);

	
	$("#yeet").click(function(){
		updatevote($("#yeet").text());
		pairvoting(combos);
	});

	$("#peet").click(function(){
		updatevote($("#peet").text());
		pairvoting(combos);
	});

});

function pairvoting(combinations){

	var lefthtml = combinations[index][0];
	var righthtml = combinations[index][1];

	$("#yeet").text(lefthtml);
	$("#peet").text(righthtml);

	index++;

	if(index >= combinations.length){
		combos = [];
		window.location.href="/rankings";
	} 	
}

function updatevote(winner){

	$.ajax({
		type: "POST",
		url: "/voteincrement",
		data: {idea: winner},
		contentType: "application/json",
		dataType: "json"
	}).done(function(response){
		console.log(response);
		pairvoting(combos);
	});//use ajax to change value of winner;
}

