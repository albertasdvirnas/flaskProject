function tryMe(arg) {
    document.write(arg);
}

function getData2(){     
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
today = mm + '/' + dd + '/' + yyyy;
document.write(today);
}

function toggleClass(el, className) {
    if (el.className.indexOf(className) >= 0) {
        el.className = el.className.replace(className,"");
		window.alert("barcode removed from list");
    }
    else {
        el.className  += className;
        //document.myform.myinput.value = el.tr.cells[0]
    }
}

function getclass(data_table) {
	var array = document.getElementsByClassName("selected");
	document.myform.myinput.value = array[0].cells.item(0).innerHTML;
	document.myform.myinput2.value = array[0].cells.item(1).innerHTML;
	document.myform.myinput3.value = array[0].cells.item(2).innerHTML;
}

