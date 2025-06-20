import random
import hashlib 
from collections import defaultdict

PRIMO = 4294967311 

def _string_to_int(s):
    """
    Converte uma string (shingle) em um número inteiro, usando SHA-1 para garantir que o valor seja sempre o mesmo, mesmo entre execuções diferentes.
    """
    return int(hashlib.sha1(s.encode('utf-8')).hexdigest(), 16) % PRIMO


def gerar_funcoes_hash(n_hashes):
    """
    Gera uma lista de funções de hash de permutação aleatórias (funções hash universais).
    
    Cada função é da forma (ax + b) % P, onde a e b são números aleatórios
    e P é um número primo grande. 

    Args:
        n_hashes (int): O número de funções hash a serem geradas (ou seja, o tamanho da assinatura). 

    Returns:
        list: Uma lista de funções lambda, onde cada função aceita um inteiro
              (representando um shingle) e retorna um valor de hash.
    """
    if not isinstance(n_hashes, int) or n_hashes <= 0:
        raise ValueError("O número de funções hash (n_hashes) deve ser um inteiro positivo.")

    funcoes = []

    for _ in range(n_hashes):
        a = random.randint(1, PRIMO - 1) 
        b = random.randint(0, PRIMO - 1)

        # essa função lambda irá aplicar a hash_universal a um valor inteiro do shingle
        func = lambda x, a_val=a, b_val=b: (a_val * x + b_val) % PRIMO
        funcoes.append(func)
    return funcoes


def gerar_assinatura(shingles, funcoes_hash):
    """
    Calcula a assinatura para um conjunto de shingles.
    
    Ou seja, para cada função hash, encontra o valor hash mínimo entre todos os shingles
    e o adiciona à assinatura. 

    Args:
        shingles (set): Um conjunto de shingles.
        funcoes_hash (list): Uma lista de funções hash geradas por 'gerar_funcoes_hash'.

    Returns:
        list: Uma lista de inteiros representando a assinatura MinHash do documento.
    """
    if not isinstance(shingles, set):
        raise TypeError("Shingles deve ser um conjunto (set).")
    if not shingles: # se não tiver shingles a assinatura é preenchida com um valor padrão
        return [float('inf')] * len(funcoes_hash)

    assinatura = []
    
    shingle_ids = [_string_to_int(shingle) for shingle in shingles] # converte cada shingle para número (usando ID) apenas uma vez

    for func in funcoes_hash:
        min_hash = float('inf') # inicializa com infinito para encontrar o mínimo
        for shingle_id in shingle_ids:
            h_val = func(shingle_id)
            if h_val < min_hash:
                min_hash = h_val
        assinatura.append(min_hash)
        
    return assinatura