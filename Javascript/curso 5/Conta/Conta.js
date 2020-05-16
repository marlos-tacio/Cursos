import {Cliente} from "../Cliente.js"

export class Conta {

    // Atributos estáticos ----------------------------------------------------------
    
    static numContas = 0;
    
    // Atributos privados -----------------------------------------------------------

    _saldo;
    _cliente;
    _agencia;

    // Construtores ----------------------------------------------------------------

    constructor(agencia, cliente) {

        // Verificação do tipo a ser instanciado
        if(this.constructor == Conta) {

            throw new Error("Classe abstrata não pode ser instanciada");
        }
        
        Conta.numContas++;

        this._saldo = 0;
        
        this._cliente = cliente;
        this._agencia = agencia;
    }

    // Métodos abstratos ------------------------------------------------------------

    // Método abstrato para o saque
    sacar(valor) {

        throw new Error("Método abstrato não implementado");
    }

    // Métodos públicos ------------------------------------------------------------
    
    // Método para depósito na conta
    depositar(valor) {
        
        if(valor >= 0) {
         
            this._saldo += valor;
        }
    }

    // Método para transferência para outra conta
    transferir(valor, destino) {
        
        this.sacar(valor);
        destino.transferir(valor);
    }

    // Métodos privados ------------------------------------------------------------

    // Método privado para saque na conta
    _sacar(valor, taxa) {

        if(this._saldo >= valor) {

            this._saldo -= valor * taxa;
        }
    }

    // Gets and Sets ---------------------------------------------------------------

    // Método para acessar cliente
    get cliente() {

        return this._cliente;
    }

    // Método para acessar saldo
    get saldo() {

        return this._saldo;
    }

    // Método para acessar agencia
    get agencia() {

        return this._agencia;
    }

    // Método para alterar o cliente
    set  cliente(cliente) {

        if(cliente instanceof Cliente) {

            this._cliente = cliente;
        }
    }

    // Método para alterar a agência
    set agencia(agencia) {

        this._agencia = agencia;
    }
}