import { Funcionario } from "./Funcionario.js";

export class Diretor extends Funcionario {

     // Métodos abstratos ------------------------------------------------------------

    // Sobrescrita do método de definição da bonificação
    _definirBonificacao() {

        return 2.0;
    }
}