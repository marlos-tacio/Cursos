import { Funcionario } from "./Funcionario.js";

export class Gerente extends Funcionario {

     // Métodos abstratos ------------------------------------------------------------

    // Sobrescrita do método de definição da bonificação
    _definirBonificacao() {

        return 1.1;
    }
}