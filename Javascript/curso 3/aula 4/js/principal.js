

var pacientes = document.querySelectorAll(".paciente");
var botaoAdicionar = document.querySelector("#adicionar-paciente");

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

	    tdImc.textContent = calIMC(altura, peso).toFixed(2);
	}
}


botaoAdicionar.onclick = function(event) {
    
    event.preventDefault();

    var form = document.querySelector("#form-adiciona");

    var nome = form.nome.value;
    var peso = form.peso.value;
    var altura = form.altura.value;
    var gordura = form.gordura.value;

    buildRow(nome, peso, altura, gordura)

};

function buildRow(nome, peso, altura, gordura) {

    var pacienteTr = document.createElement("tr");

    var nomeTd = document.createElement("td");
    var pesoTd = document.createElement("td");
    var alturaTd = document.createElement("td");
    var gorduraTd = document.createElement("td");
    var imcTd = document.createElement("td");

    nomeTd.textContent = nome;
    pesoTd.textContent = peso;
    alturaTd.textContent = altura;
    gorduraTd.textContent = gordura;
    imcTd.textContent = calIMC(altura, peso).toFixed(2);

    pacienteTr.appendChild(nomeTd);
    pacienteTr.appendChild(pesoTd);
    pacienteTr.appendChild(alturaTd);
    pacienteTr.appendChild(gorduraTd);
    pacienteTr.appendChild(imcTd);

    var tabela = document.querySelector("#tabela-pacientes");
    tabela.appendChild(pacienteTr);
}

function calIMC(altura, peso) {

	return peso / (altura * altura);
}