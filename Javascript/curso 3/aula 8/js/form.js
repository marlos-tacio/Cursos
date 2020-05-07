
// Recupera o botão de adicionar clientes
var botaoAdicionar = document.querySelector("#adicionar-paciente");

// Evento para adição de paciente na tabela
botaoAdicionar.onclick = function(event) {
    
    event.preventDefault();

    var form = document.querySelector("#form-adiciona");
    var paciente = recuperarPacienteForm(form);

    var erros = validarPaciente(paciente);

	var lista = document.querySelector("#mensagem-erro");
	limparLista(lista);

    if(erros.length > 0){
    	imprimirErros(lista, erros);
    	return;
    }

    adicionarPaciente(paciente);

    form.reset();
};

// Função que recupera os dados de um paciente de um formulário
function recuperarPacienteForm(form) {

	return {
		nome 	: form.nome.value,
		peso 	: form.peso.value,
		altura 	: form.altura.value,
		gordura : form.gordura.value,
		imc 	: calcularIMC(form.altura.value, form.peso.value).toFixed(2)
	};
}

// Função que adiciona um paciente na tabela
function adicionarPaciente(paciente) {

    var nomeTd     = criarCelula("info-nome", paciente.nome);
    var pesoTd 	   = criarCelula("info-peso", paciente.peso);
    var alturaTd   = criarCelula("info-altura", paciente.altura);
    var gorduraTd  = criarCelula("info-gordura", paciente.gordura);
    var imcTd 	   = criarCelula("info-imc", paciente.imc);

	var pacienteTr = criarLinha("paciente", nomeTd, pesoTd, alturaTd, gorduraTd, imcTd);
    
    document.querySelector("#tabela-pacientes").appendChild(pacienteTr);
}

// Função que cria uma linha da tabela
function criarLinha(classe, ...celulas) {

	var linha = document.createElement("tr");
	for(var i = 0; i < celulas.length; i++) {

		linha.appendChild(celulas[i]);
	}
	linha.classList.add(classe);

	return linha;
}

// Função que cria uma célula da tabela
function criarCelula(classe, dado) {

	var celula = document.createElement("td");
	celula.classList.add(classe);
	celula.textContent = dado;

	return celula;
}

// Função que verifica os dados do paciente
function validarPaciente(paciente) {
	
	var erros = [];


	if(!validarNome(paciente.nome)) {
		erros.push("Nome inválido!")
	}
	
	if(!validarPeso(paciente.peso)) {
		erros.push("Peso inválido!");
	}

	if(!validarAltura(paciente.altura)) {
		erros.push("Altura inválida!");
	}

	if(!validarGordura(paciente.gordura)) {
		erros.push("Porcentagem de gordura inválida!");
	}

	return erros;
}

// Função que imprime as mensagens de erro
function imprimirErros(lista, erros) {

	for(var i = 0; i < erros.length; i++) {

		lista.appendChild(criarItenLista(erros[i]));
	}	
}

// Função que cria um item de uma lista
function criarItenLista(dado) {

	var item = document.createElement("li");
	item.textContent = dado;

	return item;
}

// Função que limpa uma lista
function limparLista(lista) {

	var itens = lista.getElementsByTagName("li");
	
	for(var i = 0; i < itens.length;) {
		lista.removeChild(itens[0]);
	}
}