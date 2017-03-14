/* JS File For MelshoX project
 * By : Mahmoud Elshobaky (Mahmoud.elshobaky@gmail.com)
 */

 function init() {
 	console.log("initilizing ....");
 	bindEvents ();
 }

function bindEvents() {
	console.log("binding form submit event ....");
	$('#photo').change(function(e){
		uploadPhoto(e);
	});
	console.log("bind form submit event (done)");
}

function uploadPhoto(e) {
	var loading_txt = $("#photo_label").attr("data-loading-text");
	$("#photo_label").prepend(loading_txt);
	$("#photo_upload").trigger("submit");
}