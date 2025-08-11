(30/07/2025)

# 1.1 Evolução das Linguagens de Programação

- 5 gerações: baixo nível -> alto nível

# 1.2 Razões para estudar Linguagens de Programação

  1. Capacidade de resolver soluções computacionais
  2. Habilidade para escolher as Linguagens de Programação
  3. Habilidade para aprender novas Linguagens de Programação
  4. Capacidade para projetar novas Linguagens de Programação

# 1.3 Propriedades desejáveis das LP's

  1. Legibilidade
  2. Redigibilidade
  3. Confiabilidade
  4. Eficiência
  5. Ortogonalidade
  6. Reusabilidade
  7. Modificabilidade
  8. Portabilidade

  1.3.1 Legibilidade
Facilidade para ler e entender um programa
Malhorar a manutenção dos programas
  Favorecem:
  - Simplicidade
  - Recursos para estruturação de dados e controle
  Prejudicam:
  - "goto's"
  - Estruturas não adequadas
  - Sobrecarga de operadores
  1.3.2 Redigibilidade
Facilidade para escrever o programa (concentrar nos algoritmos centrais)
  Favorecem:
  - Simplicidade
  - Suporte para abstração
  Prejudicam:
  - Contruções complexas
  - Falta de recurso para a abstração
  - COnstruções primitivas
  1.3.3 Confiabilidade
COmportamento confiável de acordo com as suas especificações sob todas as condições
  Favorecem:
  - Verificação de tipos
  - Tratamento de exceções
  Prejudicam:
  - Permitir ações perigosas
  - Recursos pobres para escritas dos programas
  1.3.4 Eficiência
Relacionado ao tempo de execução
  Prejudicam:
  - Fatores que melhoram a confiabilidade, abstração e legibilidade dos programas diminuem a eficiência
(eficiência != legibilidade)
  1.3.5 Ortogonalidade
Combinar comceitos básicos sem que se produzam efeitos anômalos nessa combinação
menos execuções, maior ortogonalidade
prever comportamento da combinação de conceitos
  Favorecem:
  - Número pequeno de construções primitivas
  Prejudicam:
  - Número alto de execuções
  1.3.6 Reusabilidade
Utilizar o mesmo código para várias aplicações
Ligada a recursos de abstração da linguagem
mais reusável, maior produtividade de programação
  1.3.7 Modificabilidade 
Facilidade de alterar o programa sem implicações em outras partes do mesmo
  Favorecem:
  - Uso de constantes simbólicas
  - Separação entre interface gráfica e lógica de negócio
  - Tipos abstratos de dados
  1.3.8 Portabilidade
Programa se comportar da mesma maneira independente do compilador, sistema operacional ou hardware utilizado
  Favorecem:
  - Implementação híbrida
  - Padronização da especificação da linguagem desde o seu projeto (pode prejudicar o desempenho)

# 1.4 Paradigmas das LP's
Conjunto de características que servem para categorizar um grupo de linguagens

*copiar foto slide

  1.4.1 Imperativo
Mudanças de estado
Especifica como um processamento deve ser feito
Variáveis podem possuir diferentes valores a cada momento
(Estruturado, Orientado a Objetos e Concorrente)

  A) Estruturado
  B) Orientado a Objetos
  C) Concorrente

  1.4.2 Declarativo
Descrição do problema (o que deve ser feito)
(Funcional e Lógico)

  A) Funcional
  B) Lógico

  1.4.3 Linguagens de Programação Multiparadigma
Suporta mais de um paradigma
Geralmente usam frameworks

# 1.5 Linguagens de Domínio Específico

(04/08/2025)
1.6 Compiladores e Interpretadores

Existem dois métodos na tradução de códigos escritos em alto nível para a linguagem da máquina: 
1) Compiladores
2) Interpretadores

  1.6.1 Compiladores: 
    Recebe como entrada um programa em uma linguagem de programação e o traduz em um programa equivalente em outra linguagem.
    linguagem fonte -> compilador -> linguagem alvo

  Criação de um programa objeto executável:
      A) Pré-Processador: operações simples
      B) Compilador: gerar uma linguagem assembly
      C) Montador: produz um código de máquina relocável 
      D) Linker/Loader: reúne os arquivos executáveis na memória para execução
  Bibliiotecas: 
      1) Estáticas: Inseridas antes de utilizar um compilador (.h, import de jars)
      2) Dinâmicas: São inseridas em uma das fases do compilador (.lib, .dll)
  
  1.6.1.1 Fases de um compilador
        Analise Lexica, Leitura e Scanning: o programa é lido e agrupado em sequências
                                            Lexemas - sequencia de caracteres que obedece um padrão
                                            Token - um lexema já tratado
        Analise Sintática: utiliza tokens para criar uma representação intermediária do tipo de árvore (mostra interação válida entre uma sequencia de tokens)
        Analise Semantica: verificação de tipo, realiza a coerção
        Geração de Código Intermediário: ser facilmente produzida e ser dacilmente traduzida para a máquina alvo
        Otimização: produzir um código melhor e mais rápido
                    Inibição de variáveis declaradas e não utilizadas;
                    Otimização de Laços;
                    Inibição de segmentos de código não relevantes.
        Geração de Código Alvo: linguagem Assembly
    *colocar foto da fase de um compilador
PROVA V OU F:
  Análise léxica é:
    relação entre blocos do código F
    primeira fase de compilação V
    1.6.1.2 Compilação Cruzada
        Tecnica usada para compilar programas de uma plataforma Y a partir de uma plataforma X, onde X é diferente de Y
  1.6.2 Interpretadores
    Um interpretador é um programa capaz de interpretar as instruções da linguagem fonte (alto nível), executando-as diretamente.
- Traduz linha a linha
- Não é totalmente traduzido antes de ser executado
- Utilizam kapenas recursos de anáçise lexica, sintatica e semantica

  1.6.3 Diferenças entre Compiladores e Interpretadores

**escrever resumo do slide aqui

  1.6.4 Compiladores Híbridos
  O compilador tem o papel de converter o código fonte em um código bytecode, que é de baixo nível
  Interpretados por uma máquina virtual




