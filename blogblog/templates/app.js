const hamburger = document.querySelector('.header .navi .nav-list .hamburger');
const mobile_menu = document.querySelector('.header .navi .nav-list ul');
const header = document.querySelector('.header.container');
const title = document.querySelector('.header .navi h1 li');

hamburger.addEventListener('click', ()=>{
	hamburger.classList.toggle('active');
	mobile_menu.classList.toggle('active');
});

document.addEventListener('scroll', ()=>{
	var scroll_position = window.scrollY;
	if (scroll_position > 150){ 
		header.style.backgroundColor = "#4F576B";
		title.style.color = "white";
	}else{
		header.style.backgroundColor = "transparent";
	}
});