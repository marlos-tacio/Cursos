
var tabela = document.querySelector("table");

tabela.ondblclick = function(evento) {

	if(evento.target.tagName == "TD") {

		evento.target.parentNode.classList.add("fade-out");

		setTimeout(function() {
			
			evento.target.parentNode.remove();
		}, 500);
	}
};