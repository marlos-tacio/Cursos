export class Cliente {
  
    // Construtores ----------------------------------------------------------------

    constructor(nome, cpf) {

        this._senha;

        this._cpf = cpf;
        this.nome = nome;
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
}