//PROMISSE

function loadSomeData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = {
        id: 123,
        name: "Gustavo",
      };
      resolve(data);
    }, 1000);
  });
}
loadSomeData()
  .then((data) => {
    console.log("Dados carregados com sucesso:", data);
    return data;
  })
  .then((newData) => {
    console.log(`O nome é: ${newData.name}`);
  })
  .catch((err) => {
    console.log(`Erro ao carregar dados: ${err}`);
  });

//ARROW FUNCTION

const somaB = (a, b) => a + b;

console.log(somaB(2, 3));

const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const numerosPares = numeros.filter((numero) => numero % 2 === 0);
console.log(numerosPares);

//DESTRUCTURING

const usuario = {
  nome: "Gustavo",
  idade: 25,
  email: "gustavo-markes@hotmail.com",
};

const { nome, email } = usuario;

console.log(nome);
console.log(email);

const numerosB = [1, 2, 3];
const [a, b, c] = numerosB;

console.log(a);
console.log(b);
console.log(c);

function exibeNomeUsuario({ nome, email, idade }) {
  console.log(nome);
  console.log(email);
  console.log(idade);
}

exibeNomeUsuario(usuario);

let saldo = 1000;

const mensagem = `O seu saldo atual é: ${
  saldo > 0 ? `R$ ${saldo}` : "negativo"
}`;

console.log(mensagem);

// REST

const muitosNumeros = (...numeros) => {
  return console.log(numeros.reduce((somador, numero) => somador + numero));
};

muitosNumeros(1, 2, 3, 4, 5);

//SPREAD
const usuarioC = {
  nome: "Ana",
  idade: 23,
};

const usuarioComEndereco = { ...usuarioC, endereco: "Rua 1, numero 1" };
console.log(usuarioComEndereco);

// ORIENTAÇÃO A OBJETO

class Pessoa {
  constructor(nome, idade) {
    this.nome = nome;
    this.idade = idade;
  }

  apresenta() {
    console.log(`Meu nome é: ${this.nome} e eu tenho ${this.idade} ano`);
  }
}

const gustavo = new Pessoa("Gustavo", 25);
const guilherme = new Pessoa("Guilherme", 17);

gustavo.apresenta();

guilherme.apresenta();

class Funcionario extends Pessoa {
  constructor(nome, idade, salario) {
    //DECLARO MAIS NÃO USO O THIS
    super(nome, idade); //TENHO QUE DECLARAS PARA SABER AS PROPRIEDADES QUE ESTOU PUXANDO DA CLASSE PAI
    this.salario = salario;
  }

  apresentaFuncionario() {
    console.log(
      `Meu nome é: ${this.nome}, e eu tenho ${this.idade} anos, e meu salario é ${this.salario}`
    );
  }
}

const funcionario = new Funcionario("Pedro", 28, 2500);

funcionario.apresenta();
funcionario.apresentaFuncionario();

//METODOS DE ARRAY
const numeroC = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const numerosDobrados = numeroC.map((numero) => numero * 2);

console.log(numerosDobrados);

const numerosD = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const numerosImpares = numerosD.filter((numero) => numero % 2 > 0);

console.log(numerosImpares);

const numerosE = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const numerosSomados = numerosE.reduce((total, somador) => total + somador, 5); // 5  É A VARIAVEL TEMPORARIA DO TOTAL DA SOMA, SE QUISER COMEÇAR COM 0 É SO NÃO COLOCAR NADA

console.log(numerosSomados);

const numeroF = [1, 2, 4, 5, 6, 7, 8, 9];

const numero3 = numeroF.find((numero) => numero === 3);

console.log(numero3);

const nomes = ["Pedro", "Paulo", "Alex"];

nomes.forEach((nomeAtual, index) => console.log(nomeAtual, index));
