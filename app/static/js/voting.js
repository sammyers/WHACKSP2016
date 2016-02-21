/* Will  iterate through the list of values and then prompt the user to choose one
will continue to iterate until the list is exhausted, after which it will load a rankings page
*/



var testing = [(1,2),(3,4),(4,5)];
var index = 0;

var pairvoting = function (combinations){


	if(index >= combinations.length){
		windows.location.href="/rankings";
	} 
	
}

var update = function(winner){


}