### CAPÍTULO 2

(11/08/2025)

#### 

#### **2.1. Introdução**



A principal tarefa do Analisador Léxico é ler os caracteres de entrada do programa fonte, agrupá-los em Lexemas e produzir como saída uma sequência de Tokens para cada Lexema no programa fonte



OBS.: Lexemas são termos não caracterizados, após ser categorizados viram Tokens



&nbsp;	1) Varredura: (como se fosse pré-processamento) remover campos desnecessários

&nbsp;	2) Análise Léxica: produz a sequência de Tokens como saída



#### **2.2. Análise Léxica vs Análise Sintática**



OBS.: Análise Léxica é um processo anterior à Análise Sintática

&nbsp;	Análise Léxica encontra padrões em um texto (lexemas) e agrupa-os (tokens); e a Análise Sintática verifica a interação entre os conjuntos (tokens).



#### **2.3. Tokens, Padrões e Lexemas**



&nbsp;	1) Lexema: sequência de caracteres que obedece a algum padrão dentro de uma linguagem

&nbsp;	2) Token: (<Nome\_Token,Lexema>) representa uma classe de Lexemas

&nbsp;	3) Padrão: 

&nbsp;		- Palavras Reservadas

&nbsp;		- Identificadores

OBS.: Ex. de Classes de Tokens:

* ID (identificadores)
* KW (palavras-chave)
* LT (literais)
* SP (separadores)
* OP (operador)



EXEMPLO 1







