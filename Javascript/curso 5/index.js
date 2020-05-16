import {Cliente} from "./Cliente.js"
import { ContaPoupanca } from "./Conta/ContaPoupanca.js";
import { Diretor } from "./Funcionarios/Diretor.js";
import { Gerente } from "./Funcionarios/Gerente.js";
import { Autenticacao } from "./Autenticacao.js";

const cliente1 = new Cliente("Marlos", 12222);
cliente1.cadastrarSenha("123");
console.log(cliente1);

const conta1 = new ContaPoupanca(544433, cliente1);
conta1.depositar(100);
conta1.sacar(10);

const gerente = new Gerente("João", 1234, 2500.00);
gerente.cadastrarSenha("123456");
console.log(gerente);

const diretor = new Diretor("José", 1203, 1200.00);
diretor.cadastrarSenha("1234");
console.log(diretor);

console.log(Autenticacao.login(gerente, "123456"));
console.log(Autenticacao.login(diretor, "1234"));
console.log(Autenticacao.login(cliente1, "123"));