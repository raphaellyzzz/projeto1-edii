def comparar_assinaturas(assinatura1, assinatura2):
    """
    Depois de ter as assinaturas compactas dos dois documentos, compara a similaridade. Ele compara as duas assinaturas, elemento por elemento. O número de elementos iguais dividido pelo total de elementos na assinatura - nos dando a similaridade estimada de Jaccard.
    
    Similaridade: Proporção de elementos idênticos nas assinaturas. 

    Args:
        assinatura1 (list): A primeira assinatura MinHash.
        assinatura2 (list): A segunda assinatura MinHash.

    Returns:
        float: Um valor entre 0.0 e 1.0 representando a similaridade estimada.
               Retorna 0.0 se as assinaturas estiverem vazias ou forem de tamanhos diferentes.
    """
    if not isinstance(assinatura1, list) or not isinstance(assinatura2, list):
        raise TypeError("As assinaturas devem ser listas.")
        
    if len(assinatura1) == 0 or len(assinatura1) != len(assinatura2):
        return 0.0 # assinatura vazia ou de tamanhos diferentes não podem ser comparadas.

    iguais = sum(1 for a, b in zip(assinatura1, assinatura2) if a == b)
    
    similaridade = iguais / len(assinatura1)
    
    '''
        A similaridade Jaccard estimada é o número de hashes idênticos dividido pelo
        número total de hashes (ou seja, o tamanho da assinatura).
    '''

    return similaridade