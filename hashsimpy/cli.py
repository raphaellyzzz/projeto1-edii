import argparse
import os 
from hashsimpy import preprocessamento, shingling, minhashing, comparar

"""
    Esse módulo junta tudo. Ele é a interface de linha de comando. É necessário passar quais arquivos comparar (ex: arquivo1, arquivo2), o tamanho do shingle (--k) e quantas funções hash usar (--num_hashes). Ele chama todos os outros módulos na sequência - ou seja utiliza: preprocessamento, shingling, minhashing, compara) e, ao final, retorna ao usuário o veredito da similaridade em porcentagem.
"""

def main():
    parser = argparse.ArgumentParser(
        description='HashSimPy - Verificador de Similaridade Textual em Python com MinHashing.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('arquivo1', help='Caminho para o primeiro arquivo de texto (.txt).')
    parser.add_argument('arquivo2', help='Caminho para o segundo arquivo de texto (.txt).')
    parser.add_argument(
        '--k', 
        type=int, 
        default=3, 
        help='Tamanho do shingle (número de palavras por shingle). Padrão: 3.\n'
             'Valores maiores geram shingles mais específicos.'
    )
    parser.add_argument(
        '--num_hashes', 
        type=int, 
        default=100, 
        dest='n_hashes', 
        help='Número de funções hash a serem usadas para gerar a assinatura MinHash.\n'
             'Padrão: 100. Valores maiores aumentam a precisão, mas também o tempo de processamento.'
    )
    args = parser.parse_args()

    # verificacao de erros

    if not os.path.exists(args.arquivo1):
        print(f"Erro: O arquivo '{args.arquivo1}' não foi encontrado.")
        return
    if not os.path.exists(args.arquivo2):
        print(f"Erro: O arquivo '{args.arquivo2}' não foi encontrado.")
        return

    print(f"Processando '{args.arquivo1}' e '{args.arquivo2}'...")
    print(f"Parâmetros: k={args.k}, número de hashes={args.n_hashes}")

    try:
        # preprocessamento.py
        texto1 = preprocessamento.ler_e_preprocessar(args.arquivo1)
        texto2 = preprocessamento.ler_e_preprocessar(args.arquivo2)

        # shingles.py 
        shingles1 = shingling.gerar_shingles(texto1, args.k)
        shingles2 = shingling.gerar_shingles(texto2, args.k)
        
        if not shingles1 or not shingles2:
            print("Atenção: Um ou ambos os documentos resultaram em nenhum shingle. A similaridade será 0.0.")
            similaridade = 0.0
        else:
            # minhashing.py
            funcoes_hash = minhashing.gerar_funcoes_hash(args.n_hashes)
            
            # minhashing.py
            assinatura1 = minhashing.gerar_assinatura(shingles1, funcoes_hash)
            assinatura2 = minhashing.gerar_assinatura(shingles2, funcoes_hash)

            # comparar.py 
            similaridade = comparar.comparar_assinaturas(assinatura1, assinatura2)
        
        print("\n<---> Resultados da Similaridade <--->")
        print(f"Similaridade estimada entre '{os.path.basename(args.arquivo1)}' e '{os.path.basename(args.arquivo2)}': {similaridade:.2%}")

    except ValueError as ve:
        print(f"Erro de Validação: {ve}")
    except FileNotFoundError as fnfe:
        print(f"Erro de Arquivo: {fnfe}")
    except IOError as ioe:
        print(f"Erro de E/S: {ioe}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == '__main__':
    main()