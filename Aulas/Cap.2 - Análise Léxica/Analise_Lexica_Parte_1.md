# CAPÍTULO 2 (Parte 1)

## 2.1. Introdução

A principal tarefa do **Analisador Léxico** é ler os caracteres de entrada do programa fonte, agrupá-los em **Lexemas** e produzir como saída uma sequência de **Tokens** para cada Lexema no programa fonte.  

📌 **Observação:**  
- Lexemas → termos não caracterizados.  
- Tokens → lexemas categorizados.  

**Etapas:**
1. **Varredura:** como se fosse um pré-processamento (remover campos desnecessários).  
2. **Análise Léxica:** produz a sequência de Tokens como saída.  

---

## 2.2. Análise Léxica vs Análise Sintática

- A **Análise Léxica** é um processo **anterior** à Análise Sintática.  
- **Análise Léxica:** encontra padrões em um texto (**lexemas**) e os agrupa em **tokens**.  
- **Análise Sintática:** verifica a interação entre os conjuntos (**tokens**).  

---

## 2.3. Tokens, Padrões e Lexemas

1. **Lexema:** sequência de caracteres que obedece a algum padrão dentro de uma linguagem.  
2. **Token:** representa uma classe de Lexemas no formato `(<Nome_Token, Lexema>)`.  
3. **Padrão:** conjunto de regras que definem como os lexemas são reconhecidos.  

📌 **Exemplos de Classes de Tokens:**
- `ID` → Identificadores  
- `KW` → Palavras-chave  
- `LT` → Literais  
- `SP` → Separadores  
- `OP` → Operadores  

---

### Exemplo 1
<img width="1080" height="688" alt="image" src="https://github.com/user-attachments/assets/0b6945af-0cee-4ce2-baf7-be6e0947d9b2" />

---

## 2.4. Expressões Regulares (REGEX)

Ferramenta para descrever padrões em cadeias de caracteres.

### Conceitos Fundamentais

- **Alfabeto:** finito e não vazio  
  - Ex.: binário, letras minúsculas, tabela ASCII  

- **String:** finita e formada a partir de algum alfabeto  
  - String vazia: `ε`  
  - Comprimento de uma string `|w|` → número de posições de `w`.  
    - Ex.: `|010111| = 6`  
  - Conjunto de todas as Strings: Σ\*  

- **Linguagem:** conjunto de Strings escolhidas a partir de Σ\*.  

---

### Operadores

- **União (`L ∪ M`):** união de duas linguagens.  
- **Concatenação (`LM`):** junta strings de dois conjuntos.  
- **Fecho de Kleene (`L*`):** conjunto de strings formadas por zero ou mais repetições de elementos de L.  

📌 **Observações:**
- REGEX é **associativo à esquerda**.  
- Prioridade: `*` > concatenação > `|`.  

---

### Outros Operadores

- **Qualquer caractere (`.`):** reconhece um único caractere do alfabeto.  
- **Uma ou mais instâncias (`+`):** fechamento positivo.  
  - Ex.: `a+ = {a, aa, aaa, ...}`  
- **Zero ou uma instância (`?`):** indica zero ou uma ocorrência.  
  - Ex.: `abc? = {ab, abc}`  

📌 Diferença importante:  
- `a* = {ε, a, aa, aaa, ...}` (inclui vazio)  
- `a+ = {a, aa, aaa, ...}` (não inclui vazio)  

---

### Exemplos de Expressões Regulares

A) `a|b = {a, b}` → **União**  
B) `(a|b)(a|b) = {aa, ab, ba, bb}` → **Concatenação**  
C) `a* = {ε, a, aa, aaa, ...}` → **Fecho de Kleene**  
D) `(a|b)* = {ε, a, b, aa, bb, abab, ...}` → **Infinitas ocorrências de a ou b**  
E) `a|a*b = {a, b, ab, aab, aaab, ...}` → **a ou combinações de a seguidas de b**  
F) `(a|b)+c = {ac, bc, abc, aac, bbc, ...}` → **uma ou mais repetições de a ou b seguidas de c**  
G) `(a|b)ab = {aab, bab}` → **a ou b seguidos de ab**  
H) `abc? = {ab, abc}` → **c pode existir ou não**  
I) `a?bc. = {bca, bcb, abca, ...}` → **a opcional, seguido de bc e mais um caractere qualquer**  
J) `(a|bc)* = {ε, a, bc, abc, bca, aabc, bcbc, ...}` → **a ou bc infinitamente**  

---
