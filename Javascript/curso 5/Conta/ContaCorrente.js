import { Conta } from "./Conta.js";

export class ContaCorrente extends Conta {
    
    // Métodos abstratos ------------------------------------------------------------

    // Sobrescrita do método sacar
    sacar(valor) {

        const taxa = 1.1;
        super._sacar(valor, taxa);
    }
}