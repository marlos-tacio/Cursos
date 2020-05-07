
var campoFiltro = document.querySelector("#filtrar-tabela");

campoFiltro.oninput = function() {
 
    var pacientes = document.querySelectorAll(".paciente");

    if (this.value.length > 0) {

        var expressao = new RegExp(this.value, "i");
        pacientes.forEach(function(paciente) {
            
            var nome = paciente.querySelector(".info-nome").textContent;
            
            // Adição aqui
            if (expressao.test(nome)) {

                paciente.classList.remove("invisivel");
            }
            else {
            
                paciente.classList.add("invisivel");
            }
        });
    }
    else {
    
        pacientes.forEach(function(paciente) {
    
            paciente.classList.remove("invisivel");
        });
    }
};