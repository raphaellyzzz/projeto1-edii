import re

def ler_e_preprocessar(caminho_arquivo):
    """
    Preparar o arquivo para ser "limpo" lendo ele. Vai converter para minúsculas e remover pontuações/números.
    
    Args:
        caminho_arquivo (str): O caminho para o txt.

    Returns:
        str: O texto pré-processado.
    
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
        IOError: Outros erros de leitura do arquivo.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as texto:
            texto = texto.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
    except IOError as erro:
        raise IOError(f"Erro ao ler o arquivo {caminho_arquivo}: {erro}")

    texto = texto.lower() # vai converter para minúsculas.
    
    texto = re.sub(r'[^a-z\s]', '', texto) # vai remover pontuação, números e caracteres não alfabéticos, mantendo os espaços.
    
    texto = re.sub(r'\s+', ' ', texto).strip() # remover múltiplos espaços em branco com o .strip
    
    return texto

'''
após o tratamento do documento, o texto é quebrado em pequenos pedaços chamados shingles - um shingle é uma sequência de k palavras consecutivas (por exemplo: se k for 3, ele pega grupos de 3 palavras). 

vamos seguir para o arquivo shingling.py para conseguir observar melhor.
'''