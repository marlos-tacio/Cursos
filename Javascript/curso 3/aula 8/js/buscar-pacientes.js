

var botaoAdicionar = document.querySelector("#buscar-pacientes");
var carregado = false;

botaoAdicionar.onclick = function() {

	var xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api-pacientes.herokuapp.com/pacientes");

    xhr.onload = function() {

        var erroAjax = document.querySelector("#erro-ajax");

        if (xhr.status == 200) {	

	        var pacientes = JSON.parse(xhr.responseText);
	        pacientes.forEach(function(paciente) {
	            
	            adicionarPaciente(paciente);
	        });

	        erroAjax.classList.add("invisivel");

	    }
	    else {
        
            erroAjax.classList.remove("invisivel");
        }
    };

    xhr.send();
};