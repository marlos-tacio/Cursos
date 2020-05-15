import {Cliente} from "./Cliente.js"

export class Conta {
   
    static numContas = 0;

    agencia;

    _saldo;
    _cliente;
    
    constructor(agencia, cliente) {
        
        Conta.numContas++;

        this._saldo = 0;
        this.cliente = cliente;
        this.agencia = agencia;
    }

    // Altera o cliente da conta
    set  cliente(cliente) {

        if(cliente instanceof Cliente) {

            this._cliente = cliente;
        }
    }

    get cliente() {

        return this._cliente;
    }

    get saldo() {
        return this._saldo;
    }
    
    // Método para saque na conta
    sacar(valor) {

        if(this._saldo >= valor) {

            this._saldo -= valor;
        }
    }

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
}