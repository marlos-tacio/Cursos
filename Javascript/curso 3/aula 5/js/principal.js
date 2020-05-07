
var pacientes = document.querySelectorAll(".paciente");

for(var i = 0; i < pacientes.length; i++) {

	var tdAltura = pacientes[i].querySelector(".info-altura");
	var tdPeso = pacientes[i].querySelector(".info-peso");
	var tdImc = pacientes[i].querySelector(".info-imc");


	var altura = tdAltura.textContent;
	var peso = tdPeso.textContent;

	if (peso <= 0 || peso > 1000) {
	    
	    console.log("Peso inválido!");
	    tdImc.textContent = "Peso inválido!";
	    pacientes[i].classList.add("paciente-invalido");
	}
	else if (altura <= 0 || altura >= 3) {

	    console.log("Altura inválida!");
	    tdImc.textContent = "Altura inválida!";
	    pacientes[i].classList.add("paciente-invalido");
	}
	else {

	    tdImc.textContent = calcularIMC(altura, peso).toFixed(2);
	}
}



// Função que calcula o Índice de Massa Corporal
function calcularIMC(altura, peso) {

	return peso / (altura * altura);
}


