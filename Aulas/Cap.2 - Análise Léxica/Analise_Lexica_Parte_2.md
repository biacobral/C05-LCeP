CAPITULO 2 (Parte 2)



2.6. Autômatos Finitos



&nbsp;	Modelo computacional e mecanismo de reconhecimento - de caráter gráfico.



<img width="425" height="298" alt="image" src="https://github.com/user-attachments/assets/fd309db0-8add-4a16-a6a4-4b4817d11a9a" />



&nbsp;	Círculos representam estados e Arcos representam transição de estados.



&nbsp;	Um autômato verifica se uma palavra W (word) pertence a uma linguagem L (language).





Onde podemos aplicar a Teoria de Autômatos?

* Projetar e verificar o comportamento de **circuitos digitais**;
* Examinar grandes **corpos de texto**;
* Verificar sistemas que têm um **número fixo de estados distintos**;
* Construção de **analisadores léxicos**.



Os autômatos operam em 3 partes: 

&nbsp;	1) Fita de Entrada

&nbsp;		Dispositivo de entrada que contém a informação a ser processada

&nbsp;	2) Unidade de Controle

&nbsp;		Indica o estado atual da máquina

&nbsp;	3) Função de Transição de Autòmato

&nbsp;		Comanda a leitura de símbolos de fita e define o estado da máquina



Os Autômatos Finitos podem ser de três tipos:

&nbsp;	1) Autômatos Finitos Deterministas (DFA)

&nbsp;		Dependendo do estado atual e do símbolo lido, o sistema pode assumir um ÚNICO estado bem determinado;

&nbsp;	2) Autômatos Finitos Não Deterministas (NFA)

&nbsp;		Dependendo do estado atual e do símbolo lido, o sistema pode assumir um CONJUNTO de estados alternativos.

&nbsp;	3) Autômatos Finitos com movimentos vazios (NFA-ε)

&nbsp;		Dependendo do estado atual e sem ler qualquer símbolo, o sistema ainda assim pode assumir um conjunto de estados.



Os três tipos de Autômatos são capazes de reconhecer as linguagens regulares



2.7. Autômatos Finitos Deterministas



&nbsp;	É composto pela seguinte Quíntupla:



A = (Q, Σ, δ, q₀, F)



* A é o nome do DFA (Autômato Finito Determinístico);
* Q é o conjunto de estados;
* Σ (sigma) é o conjunto de símbolos de entrada;
* δ (delta) é a função de transição;
* q₀ é o estado inicial;
* F é o conjunto de estados de aceitação (ou estados finais).



Existem duas notações para descrever Autômatos:

&nbsp;	1) Diagrama de Transição

&nbsp;		Representa um Autômato por meio de um grafo;

&nbsp;	2) Tabela de Transição 

&nbsp;		É uma listagem da função δ que informa o conjunto de estados e o alfabeto de entrada



<img width="662" height="300" alt="image" src="https://github.com/user-attachments/assets/80337d1f-927f-4bb8-941e-d459bcfacca4" />



EXEMPLO 1:



<img width="432" height="217" alt="image" src="https://github.com/user-attachments/assets/e777ba56-2332-4e78-925f-0dcfa6edacfd" />



&nbsp;	A = (Q, Σ, δ, q₀, F)



&nbsp;	Q = {1, 2}

&nbsp;	Σ = {letra, dígito}

&nbsp;	δ: (1, letra) = 2

&nbsp;	   (2, letra) = 2

&nbsp;	   (2, dígito) = 2

&nbsp;	q₀ = {1}

&nbsp;	F = {2}



2.8. A Ferramenta JFLAP



É um software educacional interativo escrito em Java para a realização de experimentos com Linguagens Formais e Autômatos



http://www.jflap.org/

&nbsp;

