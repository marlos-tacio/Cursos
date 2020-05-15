import {Cliente} from "./Cliente.js"
import {Conta} from "./Conta.js"


const cliente1 = new Cliente("Marlos", 12222);
const conta1 = new Conta(544433, cliente1);

console.log(conta1);
console.log(Conta.numContas);