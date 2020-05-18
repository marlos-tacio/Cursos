import { Conta } from "./Conta.js";

export class ContaPoupanca extends Conta {

    // Métodos abstratos ------------------------------------------------------------

    // Sobrescrita do método sacar
    sacar(valor) {

        const taxa = 1.02;
        super._sacar(valor, taxa);
    }
}