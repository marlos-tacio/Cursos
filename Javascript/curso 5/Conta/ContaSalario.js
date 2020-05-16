import { Conta } from "./Conta.js";

export class ContaSalario extends Conta {

    // Métodos abstratos ------------------------------------------------------------

    // Sobrescrita do método sacar
    sacar(valor) {

        const taxa = 1.01;
        super._sacar(valor, taxa);
    }
}