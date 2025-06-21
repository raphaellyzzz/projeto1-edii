# projeto1-edii
Desenvolver uma classe em Python que implemente a Tabela Hash (Mapa Hash).

<a href="https://github.com/tiagopessoalima/ED2/blob/main/Semana_10_(ED2).pdf">requisito</a>

# HashSimPy

Este projeto implementa o algoritmo **HashSimPy**, uma implementação eficiente para virificar a similaridade entre dois documento <i>.txt</i>. Utilizando o princípio de MinHash juntamente com a semelhança de Jaccard.

---

## O que é MinHash?

O **MinHash** (ou "Minimum Hashing") é uma técnica para estimar rapidamente a semelhança de dois conjuntos. A probabilidade de que um determinado valor MinHash venha de um dos itens compartilhados é igual à semelhança de Jaccard.

### História

O esquema foi publicado por Andrei Broder em uma conferência de 1997, e inicialmente usado no mecanismo de busca AltaVista para detectar páginas da web duplicadas e eliminá-las dos resultados de pesquisa. Também tem sido aplicado em problemas de agrupamento em larga escala, como agrupamento de documentos pela semelhança de seus conjuntos de palavras.
Por exemplo, Chris McCormick mostrou que, em 10.000 artigos, computar todas as Jaccard pairwise levava cerca de 20 minutos, enquanto comparar MinHash levava apenas 3 minutos. Podemos ver o estudo <a href="https://github.com/chrisjmccormick/MinHash">nesse link</a>

---

## Índice de Jaccard
Quantifica a similaridade entre dois conjuntos A e B como a razão entre o tamanho da interseção e da união: <i>J(A,B) = |A ∩ B| / |A ∪ B|.</i> É 0 se A e B são disjuntos, e 1 se são iguais.

## Shingling
Associa um conjunto de subsequencias de tokens a um documento, A partir disso reduz a listas de tokens a uma lista de hashes, que essas podem ser comparadas diretamente utilizando diferença, união e interseção de conjuntos para determinar a dissimilaridade ou distancia. <a href="https://www.cos.ufrj.br/uploadfile/publicacao/2929.pdf#:~:text=Jaccard%20,%282.2">Podemos ver melhor nesse link</a>

## Estrutura projeto

```plaintext
├── __init__.py # Indicar que é um pacote Python
├── cli.py # Interface de linha de comando
├── comparar.py # Lógica para comparar arquivos de texto
├── minhashing.py # Algoritmo de MinHash
├── preprocessamento.py # Limpeza e normalização de texto
├── shingling.py # Geração de shingles (k-gramas)
├── testes/ # Arquivos de teste
│ ├── sem_texto.txt
│ ├── texto_base.txt
│ ├── ..
└── README.md # Documentação do projeto
```

## 🚀 Funcionalidades

- ✅ Geração de shingles (k-gramas)
- ✅ Cálculo de MinHash signatures
- ✅ Estimativa de similaridade de Jaccard com base nas assinaturas
- ✅ Exemplo de uso com documentos de texto
- ✅ Visualização de resultados (opcional)

---

## 🛠️ Como usar

### 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/raphaellyzzz/projeto1-edii
cd projeto1-edii
```
