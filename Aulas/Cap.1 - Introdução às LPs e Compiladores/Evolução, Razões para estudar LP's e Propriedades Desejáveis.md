# 📘 Linguagens de Programação


## 1.1 Evolução das Linguagens de Programação
- 5 gerações: baixo nível → alto nível

---

## 1.2 Razões para estudar Linguagens de Programação
1. Capacidade de resolver soluções computacionais  
2. Habilidade para escolher as Linguagens de Programação  
3. Habilidade para aprender novas Linguagens de Programação  
4. Capacidade para projetar novas Linguagens de Programação  

---

## 1.3 Propriedades desejáveis das LP's

1. **Legibilidade**  
2. **Redigibilidade**  
3. **Confiabilidade**  
4. **Eficiência**  
5. **Ortogonalidade**  
6. **Reusabilidade**  
7. **Modificabilidade**  
8. **Portabilidade**

---

### 1.3.1 Legibilidade
Facilidade para ler e entender um programa.  
Melhora a manutenção dos programas.

**Favorecem:**  
- Simplicidade  
- Recursos para estruturação de dados e controle  

**Prejudicam:**  
- Uso de `goto`  
- Estruturas inadequadas  
- Sobrecarga de operadores  

---

### 1.3.2 Redigibilidade
Facilidade para escrever o programa (foco nos algoritmos centrais).  

**Favorecem:**  
- Simplicidade  
- Suporte para abstração  

**Prejudicam:**  
- Construções complexas  
- Falta de recurso para abstração  
- Construções primitivas  

---

### 1.3.3 Confiabilidade
Comportamento confiável de acordo com as especificações sob todas as condições.  

**Favorecem:**  
- Verificação de tipos  
- Tratamento de exceções  

**Prejudicam:**  
- Permitir ações perigosas  
- Recursos pobres para escrita de programas  

---

### 1.3.4 Eficiência
Relacionado ao tempo de execução.  

⚠️ Muitas vezes, fatores que **melhoram a confiabilidade, abstração e legibilidade** diminuem a eficiência.  
> Eficiência ≠ Legibilidade  

---

### 1.3.5 Ortogonalidade
Capacidade de **combinar conceitos básicos sem produzir efeitos anômalos**.  
- Menos exceções → maior ortogonalidade  
- Facilita prever o comportamento da combinação de conceitos  

**Favorecem:**  
- Número pequeno de construções primitivas  

**Prejudicam:**  
- Número alto de exceções  

---

### 1.3.6 Reusabilidade
Capacidade de utilizar o mesmo código em várias aplicações.  
- Ligada a recursos de abstração  
- Quanto mais reusável, maior a produtividade  

---

### 1.3.7 Modificabilidade
Facilidade de alterar o programa sem afetar outras partes.  

**Favorecem:**  
- Uso de constantes simbólicas  
- Separação entre interface gráfica e lógica de negócio  
- Tipos abstratos de dados  

---

### 1.3.8 Portabilidade
Capacidade do programa de se comportar da mesma forma **independente do compilador, SO ou hardware**.  

**Favorecem:**  
- Implementação híbrida  
- Padronização da especificação da linguagem desde o projeto (mas pode prejudicar desempenho)  

---

## 1.4 Paradigmas das Linguagens de Programação
Conjunto de características que categorizam um grupo de linguagens.  

> *(Inserir imagem do slide aqui)*

---

### 1.4.1 Imperativo
- Mudanças de estado  
- Especifica **como** o processamento deve ser feito  
- Variáveis podem mudar de valor  

**Subcategorias:**  
- A) Estruturado  
- B) Orientado a Objetos  
- C) Concorrente  

---

### 1.4.2 Declarativo
- Descrição do problema (**o que** deve ser feito)  

**Subcategorias:**  
- A) Funcional  
- B) Lógico  

---

### 1.4.3 Multiparadigma
- Suportam mais de um paradigma  
- Geralmente utilizam **frameworks**  

---

## 1.5 Linguagens de Domínio Específico
*(Conteúdo a ser complementado)*  

---

## 1.6 Compiladores e Interpretadores (04/08/2025)

Existem dois métodos de tradução de código em alto nível para linguagem de máquina:  
1. **Compiladores**  
2. **Interpretadores**  

---

### 1.6.1 Compiladores
Um compilador recebe como entrada um programa em uma linguagem de programação e o traduz em outro equivalente.  

```mermaid
flowchart LR
    A[Linguagem Fonte] --> B[Compilador] --> C[Linguagem Alvo]

  
# 1.6 Compiladores e Interpretadores

### 1.6.1.1 Fases de um compilador
- **Análise Léxica (Leitura e Scanning):**  
  O programa é lido e agrupado em sequências.  
  - **Lexemas:** sequência de caracteres que obedece a um padrão.  
  - **Token:** um lexema já tratado.  

- **Análise Sintática:**  
  Utiliza tokens para criar uma representação intermediária do tipo árvore (mostra interação válida entre uma sequência de tokens).  

- **Análise Semântica:**  
  Verificação de tipo, realiza coerção.  

- **Geração de Código Intermediário:**  
  Deve ser facilmente produzido e traduzido para a máquina alvo.  

- **Otimização:**  
  Produzir um código melhor e mais rápido. Exemplos:  
  - Inibição de variáveis declaradas e não utilizadas;  
  - Otimização de laços;  
  - Inibição de segmentos de código não relevantes.  

- **Geração de Código Alvo:**  
  Código final na linguagem Assembly.  

📌 *Colocar foto da fase de um compilador*  

---

### Prova V ou F
- Análise léxica é:  
  - relação entre blocos do código → **F**  
  - primeira fase de compilação → **V**

---

### 1.6.1.2 Compilação Cruzada
Técnica usada para compilar programas de uma plataforma **Y** a partir de uma plataforma **X**, onde **X ≠ Y**.  

---

## 1.6.2 Interpretadores
Um **interpretador** é um programa capaz de interpretar instruções da linguagem fonte (alto nível), executando-as diretamente.  

- Traduz **linha a linha**;  
- Não é totalmente traduzido antes de ser executado;  
- Utilizam apenas recursos de análise léxica, sintática e semântica.  

---

## 1.6.3 Diferenças entre Compiladores e Interpretadores

- **Compilador:**  
  - Traduz o código inteiro antes de executar.  
  - Gera código objeto/máquina.  
  - Mais rápido na execução, mas demora na compilação.  

- **Interpretador:**  
  - Executa linha por linha.  
  - Não gera código objeto completo.  
  - Mais lento na execução, mas rápido para testar pequenos trechos.  

📌 **Resumo:**  
Compiladores traduzem tudo antes de rodar, enquanto interpretadores executam diretamente cada instrução.  

---

## 1.6.4 Compiladores Híbridos
- O compilador converte o **código-fonte** em **bytecode** (baixo nível).  
- O bytecode é interpretado por uma **máquina virtual**.  
- Exemplo: **Java** (compilador → bytecode → JVM interpreta).  
