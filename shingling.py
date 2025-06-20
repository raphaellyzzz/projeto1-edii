def gerar_shingles(texto, k):
    """
    Vai gerar um conjunto de shingles a partir de um texto, utilizando um set para armazenar os shingles únicos. 

    Args:
        texto (str): O texto pré-processado.
        k (int): O tamanho do shingle (número de palavras por shingle). 

    Returns:
        set: Um conjunto de strings, onde cada string é um shingle único.
    """
    if not isinstance(k, int) or k <= 0:
        raise ValueError("O tamanho do shingle (k) deve ser um inteiro positivo.")
    
    palavras = texto.split()
    
    if len(palavras) < k: # se o texto for menor que k, não é possível formar shingles desse tamanho
        return set() # retornaremos um conjunto vazio

    shingles = set() # evitar repetição de shingle
    
    for i in range(len(palavras) - k + 1):
        shingle = ' '.join(palavras[i:i + k])
        shingles.add(shingle)
        
    return shingles