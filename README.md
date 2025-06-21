# Verificador de Similaridade Textual em Python com MinHashing
Desenvolver uma ferramenta Python, via linha de comando (CLI), que compara documentos e calcula um índice de similaridade usando MinHashing.

<a href="https://github.com/tiagopessoalima/ED2/blob/main/Semana_10_(ED2).pdf">Requisitos do projeto</a>

# HashSimPy

Este projeto implementa o algoritmo **HashSimPy**, uma implementação eficiente para virificar a similaridade entre dois documento <i>.txt</i>. Utiliza o princípio de MinHash juntamente com a semelhança de Jaccard para retornar a semelhança em %.

---

## -> O que é MinHash?

O **MinHash** (ou "Minimum Hashing") é uma técnica para estimar rapidamente a semelhança de dois conjuntos. A probabilidade de que um determinado valor MinHash venha de um dos itens compartilhados é igual à semelhança de Jaccard.

### História

O esquema foi publicado por Andrei Broder em uma conferência de 1997, e inicialmente usado no mecanismo de busca AltaVista para detectar páginas da web duplicadas e eliminá-las dos resultados de pesquisa. Também tem sido aplicado em problemas de agrupamento em larga escala, como agrupamento de documentos pela semelhança de seus conjuntos de palavras.
Por exemplo, Chris McCormick mostrou que, em 10.000 artigos, computar todas as Jaccard pairwise levava cerca de 20 minutos, enquanto comparar MinHash levava apenas 3 minutos. Podemos ver o estudo <a href="https://github.com/chrisjmccormick/MinHash">nesse link</a>

---

## -> Índice de Jaccard
Quantifica a similaridade entre dois conjuntos A e B como a razão entre o tamanho da interseção e da união: <i>J(A,B) = |A ∩ B| / |A ∪ B|.</i> É 0 se A e B são disjuntos, e 1 se são iguais.

## -> Shingling
Associa um conjunto de subsequencias de tokens a um documento, A partir disso reduz a listas de tokens a uma lista de hashes, que essas podem ser comparadas diretamente utilizando diferença, união e interseção de conjuntos para determinar a dissimilaridade ou distancia. <a href="https://www.cos.ufrj.br/uploadfile/publicacao/2929.pdf#:~:text=Jaccard%20,%282.2">Podemos ver melhor nesse link</a>

## Estrutura projeto

```plaintext
├── __init__.py # Indicar que é um pacote Python
├── cli.py # script principal de interface de linha de comando. realiza o parse de argumentos, orquestra as chamadas aos demais módulos e apresenta os resultados ao usuário via linha de comando.
├── comparar.py # funções para comparar duas assinaturas de MinHash (por exemplo, calculando a fração de posições coincidentes) e estimar a similaridade.
├── minhashing.py # implementação do algoritmo MinHash, que recebe um conjunto de shingles e retorna a assinatura de hash de tamanho fixo.
├── preprocessamento.py # funções para ler arquivos de texto e realizar pré-processamento
├── shingling.py # funções para gerar o conjunto de k-shingles de um texto pré-processado.
├── testes/ # Arquivos de teste
│ ├── sem_texto.txt
│ ├── texto_base.txt
│ ├── ..
└── README.md # Documentação do projeto
```

## -> Funcionalidades

- ✅ Geração de shingles (k-gramas)
- ✅ Cálculo de MinHash signatures
- ✅ Estimativa de similaridade de Jaccard com base nas assinaturas
- ✅ Exemplo de uso com documentos de texto
- ✅ Visualização de resultados via linha de comando

---

## Como usar?

### Instalação

Clone o repositório:

```bash
git clone https://github.com/raphaellyzzz/projeto1-edii
cd projeto1-edii
```

Execute via CLI

```bash
python cli.py <arquivo1> <arquivo2> [--k K] [--num_hashes N]
```
<ul>arquivo1 e arquivo2 são os caminhos para os arquivos de texto a serem comparados.</ul>
<ul>--k (opcional) define o tamanho do shingle (default = 3).</ul>
<ul>--num_hashes (opcional) define o número de funções de hash usadas no MinHash (default = 100).</ul>

## Bibliografia utilizada
- https://en.wikipedia.org/wiki/MinHash
- https://milvus.io/pt/blog/minhash-lsh-in-milvus-the-secret-weapon-for-fighting-duplicates-in-llm-training-data.md
- https://mccormickml.com/2015/06/12/minhash-tutorial-with-python-code/
- https://www-di.inf.puc-rio.br/~casanova/Disciplinas/INF1331/Slides/03.2-03.3-Shingling-MinHash.pdf
