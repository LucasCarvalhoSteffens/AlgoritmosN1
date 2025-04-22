"""
Implementação do algoritmo de Subsequência Comum Máxima (LCS - Longest Common Subsequence)
usando programação dinâmica com memoização.

Este módulo fornece funções para encontrar a maior subsequência comum entre duas strings,
tanto o tamanho quanto a própria subsequência.
"""

def lcs(s1: str, s2: str, m: int, n: int, memo: dict = None, contador: dict = None) -> int:
    """
    Encontra o tamanho da maior subsequência comum entre duas strings usando recursão com memoização.
    
    Args:
        s1 (str): Primeira string
        s2 (str): Segunda string
        m (int): Tamanho atual da primeira string
        n (int): Tamanho atual da segunda string
        memo (dict, optional): Dicionário para armazenar resultados já calculados
        contador (dict, optional): Dicionário para contar chamadas recursivas
        
    Returns:
        int: Tamanho da maior subsequência comum
    """
    if memo is None:
        memo = {}
    if contador is None:
        contador = {}
    
    chave = (m, n)
    
    # Conta quantas vezes este subproblema foi visitado
    contador[chave] = contador.get(chave, 0) + 1
    
    if chave in memo:
        return memo[chave]
    
    if m == 0 or n == 0:
        return 0
    
    if s1[m-1] == s2[n-1]:
        resultado = 1 + lcs(s1, s2, m-1, n-1, memo, contador)
    else:
        resultado = max(lcs(s1, s2, m-1, n, memo, contador), lcs(s1, s2, m, n-1, memo, contador))
    
    memo[chave] = resultado
    return resultado

def encontrar_subsequencia(s1: str, s2: str) -> str:
    """
    Encontra a maior subsequência comum entre duas strings.
    
    Args:
        s1 (str): Primeira string
        s2 (str): Segunda string
        
    Returns:
        str: A maior subsequência comum
    """
    m, n = len(s1), len(s2)
    # Cria uma matriz para armazenar os resultados intermediários
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Preenche a matriz dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstrói a subsequência
    i, j = m, n
    subsequencia = []
    
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            subsequencia.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(subsequencia))

def maior_subsequencia_comum(s1: str, s2: str) -> tuple[int, str, dict]:
    """
    Encontra o tamanho e a maior subsequência comum entre duas strings.
    
    Args:
        s1 (str): Primeira string
        s2 (str): Segunda string
        
    Returns:
        tuple[int, str, dict]: Tupla contendo o tamanho, a subsequência comum e o contador de chamadas
    """
    contador = {}
    tamanho = lcs(s1, s2, len(s1), len(s2), contador=contador)
    subsequencia = encontrar_subsequencia(s1, s2)
    return tamanho, subsequencia, contador

def main():
    """Função principal com exemplos de uso."""
    # Casos de teste
    testes = [
        ("ABC", "AC"),  # Exemplo simples para demonstração
        ("ABCDGH", "AEDFHR"),
        ("AGGTAB", "GXTXAYB"),
    ]
    
    print("=" * 50)
    print("Testes da Subsequência Comum Máxima (LCS)")
    print("=" * 50)
    
    for s1, s2 in testes:
        tamanho, subsequencia, contador = maior_subsequencia_comum(s1, s2)
        print(f"\nString 1: '{s1}'")
        print(f"String 2: '{s2}'")
        print(f"Tamanho da LCS: {tamanho}")
        print(f"Subsequência: '{subsequencia}'")
        
        # Mostra estatísticas do cache
        total_chamadas = sum(contador.values())
        subproblemas_unicos = len(contador)
        print(f"\nEstatísticas do Cache:")
        print(f"Total de chamadas recursivas: {total_chamadas}")
        print(f"Número de subproblemas únicos: {subproblemas_unicos}")
        print(f"Eficiência do cache: {subproblemas_unicos/total_chamadas:.2%}")
        print("-" * 50)

if __name__ == "__main__":
    main()
    