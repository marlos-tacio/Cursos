export class Funcionario {

    // Construtores ----------------------------------------------------------------

    constructor(nome, cpf, salario) {
    
        // Verificação do tipo a ser instanciado
        if(this.constructor == Funcionario) {

            throw new Error("Classe abstrata não pode ser instanciada");
        }

        this._senha;

        this._cpf = cpf;
        this._nome = nome;
        this._salario = salario;

        // Definição da bonificação a partir de método abstrato
        this._bonificacao = this._definirBonificacao();
    }

    // Métodos abstratos ------------------------------------------------------------
    
    // Método abstrato para definição da bonificação
    _definirBonificacao() {
        
        throw new Error("Método abstrato não implementado");
    }

    // Métodos públicos -------------------------------------------------------------

    cadastrarSenha(senha) {

        this._senha = senha;
    }

    autenticar(senha) {

        return this._senha == senha;
    }

    // Gets and Sets ---------------------------------------------------------------

    get cpf() {

        return this._cpf;
    }

    get nome() {

        return this._nome;
    }

    get salario() {

        return this._salario;
    }

    get bonificacao() {

        return this._bonificacao;
    }

    set salario(valor) {

        if(valor >= 0) {

            this._salario = valor;
        }
    }   
}