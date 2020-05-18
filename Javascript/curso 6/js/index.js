var exp = /(\d\d)(\w)/g;

var resultado;
var alvo = '11a22b33c';

//console.log(exp.test(alvo));
while(resultado = exp.exec(alvo)) {    
    console.log(resultado);
}

exp = /-/g;
var anoMesDia = '2007-12-31';
console.log(anoMesDia.replace(exp, '/'));

exp = /[,;-]/;
var arquivo = '100,200-150,200;20';
console.log(arquivo.split(exp));

exp = /[A-Za-z]\d+/g;
var codigos = 'A121B12112C12212F12G01';
console.log(codigos.match(exp));