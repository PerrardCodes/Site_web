function allerA(id){
	document.getElementsByClassName("sshow")[0].className = "hide";
	document.getElementById(id).className="sshow";
	if(document.getElementsByClassName("show").length<4){
		liste()
	}
}
function cacher(id){
	d = document.getElementsByClassName("article");
	var n = d.length;
	for(var i=0; i<n; i++){
		if(d[i].className=="article hide " +id){
			d[i].className="article show " + id;
		}
	}
	s = document.getElementsByTagName("span")
	for(var i=0; i<s.length; i++){
		if(s[i].className!="show " +id){
			s[i].className = s[i].className.replace("show", "hide")
		}
	}
	r = document.getElementById("retour");
	r.className = "show";
}
function liste(){
		r = document.getElementById("retour");
		r.className = "hide";
		d = document.getElementsByClassName("article");
		for(var i=0; i<d.length; i++){
			d[i].className = d[i].className.replace("show", "hide")
		}
		s = document.getElementsByTagName("span");
		for(var i=0; i<s.length; i++){
			s[i].className = s[i].className.replace("hide", "show")
		}
}
