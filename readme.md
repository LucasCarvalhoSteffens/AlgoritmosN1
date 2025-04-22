# Implementação da Subsequência Comum Máxima (LCS)

## Problema Escolhido

O problema da Subsequência Comum Máxima (LCS - Longest Common Subsequence) foi escolhido por sua relevância em diversas áreas da computação, como:
- Comparação de sequências biológicas (DNA, RNA, proteínas)
- Detecção de plágio
- Sistemas de controle de versão
- Alinhamento de textos

O problema consiste em encontrar a maior sequência de caracteres que aparece na mesma ordem em duas strings, mas não necessariamente de forma contígua. Por exemplo, para as strings "ABCBDAB" e "BDCABA", a LCS é "BCBA".

## Estratégia de Resolução

### Recursividade

A solução implementada utiliza uma abordagem recursiva que divide o problema em subproblemas menores:

1. **Caso Base**: Se uma das strings estiver vazia, a LCS tem tamanho 0
2. **Caso Recursivo**:
   - Se os últimos caracteres das strings forem iguais, a LCS inclui esse caractere mais a LCS das substrings restantes
   - Se forem diferentes, a LCS é o máximo entre:
     - LCS da primeira string sem o último caractere e a segunda string
     - LCS da primeira string e a segunda string sem o último caractere

### Memoization

Para otimizar a solução recursiva, implementamos memoization (cache) que:

1. Armazena resultados de subproblemas já calculados
2. Evita recálculos desnecessários
3. Reduz a complexidade de tempo de exponencial (O(2^n)) para quadrática (O(n*m))

## Implementação do Cache

O cache foi implementado através de um dicionário Python que:

1. **Chave**: Tupla (m, n) representando os tamanhos atuais das substrings
2. **Valor**: Resultado da LCS para esses tamanhos

### Funcionamento do Cache:

```python
# Exemplo de uso do cache
memo = {}
chave = (m, n)

# Verifica se o resultado já foi calculado
if chave in memo:
    return memo[chave]

# Calcula e armazena o resultado
resultado = calculo_da_LCS()
memo[chave] = resultado
```

### Benefícios da Implementação:

1. **Eficiência**: Cada subproblema é calculado apenas uma vez
2. **Simplicidade**: Implementação direta usando estruturas de dados nativas do Python
3. **Flexibilidade**: O cache pode ser reutilizado entre diferentes chamadas da função

## Complexidade

- **Tempo**: O(n*m), onde n e m são os tamanhos das strings
- **Espaço**: O(n*m) para armazenar a matriz de memoization

## Exemplo de Uso

```python
s1 = "ABCBDAB"
s2 = "BDCABA"
tamanho, subsequencia = maior_subsequencia_comum(s1, s2)
print(f"Tamanho da LCS: {tamanho}")  # Saída: 4
print(f"Subsequência: {subsequencia}")  # Saída: "BCBA"
```

## Conclusão

A implementação demonstra como técnicas de programação dinâmica, como memoization, podem transformar uma solução recursiva ineficiente em um algoritmo otimizado e prático. O cache implementado é fundamental para tornar o algoritmo viável para strings de tamanho considerável.
