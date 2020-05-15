export class Cliente {
  
    _cpf;
    nome;

    constructor(nome, cpf) {

        this._cpf = cpf;
        this.nome = nome;
    }

    get cpf() {

        return this._cpf;
    }
}