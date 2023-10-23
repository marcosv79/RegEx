[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/GYGT1GQo)
# TP01 

## grupo  D09

|  Número  |                 Nome                 |
|----------|:------------------------------------:|
|  18568   |  Marcos Alberto Lopes de Vasconcelos |
|  20468   |  Diogo Miguel Barbosa de Oliveira    |
|  20457   |  Tomás Fernandes Ferreira            |

## Exercício 1
Esta primeira parte do trabalho prático tem como objetivo aplicar o conhecimento de linguagens regulares e reconhecedores.
O exercício 1 está dividido em 4 alíneas:

#### Alínea a
Na alínea a foi definida uma expressão regular para usar no decorrer do trabalho.

#### Alínea b
Na alínea b antes de calcular o AFD foi feito o AFND.

#### Alínea c
Na alínea c foi definida a Tabela de Transição da expressão regular e também desenvolvido um algoritmo de exemplos para testes.

#### Alínea d
Na alinea d foi representado o grafo de saída da expressão regular correspondente utilizando a linguagem **graphviz**.


## Exercício 2
Na segunda parte deste trabalho prático o objetivo foi a implementação em Python + a utilização da biblioteca **PLY** para análise léxica.
O objetivo deste projeto é a simulação da interação de um utilizador com uma máquina de venda automática.
As decisões tomadas foram sempre de acordo com que a implementação fosse o mais idêntica possível com o exemplo fornecido no enunciado.
Apenas é possível inserir as moedas e2, e1, c50, c20, c10, c5, c2, c1. Tudo o resto é ignorado e não é aceite pela máquina.
Os produtos estão já definidos anteriormente, tendo nome, preço e quantidade. Para a compra de um produto é apenas necessário escrever “PRODUTO=” e o nome do produto desejado.
Se o utilizador não tiver dinheiro suficiente é exibida uma mensagem, o mesmo acontece caso o produto não tenha stock.
Se a compra do produto for bem-sucedida o preço do produto é descontado ao saldo do cliente e o stock é atualizado.
Se o utilizador escrever “CANCELAR” é devolvido o dinheiro especificando a quantidade e qual(quais) moeda(s) a máquina irá devolver.