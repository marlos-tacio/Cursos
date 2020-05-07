
var linhas = document.querySelectorAll(".paciente");

for(var i = 0; i < linhas.length; i++) {


	var paciente = recuperarPacienteLinha(linhas[i])
	
	if (!validarPeso(paciente.peso)) {
		    
	   tratarDadosInvalidos(linhas[i], "paciente-invalido", "Peso inválido");
	}
	else if (!validarAltura(paciente.altura)) {

		tratarDadosInvalidos(linhas[i], "paciente-invalido", "Peso inválido");
	}
	else {

		adicionarIMC(paciente.altura, paciente.peso, linhas[i]);
	}
}

// Função para recuperar uma paciente da tabela
function recuperarPacienteLinha(linha) {

	return {
		nome 	: linha.querySelector(".info-nome").textContent,
		peso 	: linha.querySelector(".info-peso").textContent,
		altura 	: linha.querySelector(".info-altura").textContent,
		gordura : linha.querySelector(".info-gordura").textContent,
		imc 	: linha.querySelector(".info-imc").textContent
	};
}

// Função que calcula o Índice de Massa Corporal
function calcularIMC(altura, peso) {

	return peso / (altura * altura);
}

// Função que adiciona o IMC na tabela
function adicionarIMC(altura, peso, linha) {

	linha.querySelector(".info-imc").textContent = calcularIMC(altura, peso).toFixed(2);
}

// Função para validar o valor do peso
function validarAltura(altura) {

	return altura >= 0 && altura <= 3 && altura.length != 0;
}

// Função para validar o valor do peso
function validarPeso(peso) {

	return peso >= 0 && peso <= 1000 && peso.length != 0;
}

// Função para validar a porcentagem de gordura
function validarGordura(gordura) {

	return gordura >= 0 && gordura <= 100 && gordura.length != 0;
}

// Função para validar o nome
function validarNome(nome) {

	return nome.trim().length != 0;
}


// Função de tratamento 
function tratarDadosInvalidos(linha, classe, mensagem) {

    linha.querySelector(".info-imc").textContent = mensagem;
    linha.classList.add(classe);
}