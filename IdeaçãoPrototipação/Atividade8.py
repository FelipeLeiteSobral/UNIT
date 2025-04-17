# 1. Dados as variáveis e operações:

# v1 := 32
# v2 := 5 + v1
# v1 := v2 * 2

# Como fazer para segurar e mostrar o valor inicial da variável v1 no final das operações?

v1 = 32
v2 = v1 + 5
v3 = v1  # <-- Armazenar variável
v1 = v2 * 2

# 2. Como fazer para passar o valor de uma variável para outra e vice-versa?

v1,v2 = v2,v1 # <-- Troca de variáveis

# 3. Quais as operações necessárias para intercambiar os valores de 3 variáveis a, b e c de modo que “a” fique com o
# valor de “b”; “b” fique com o valor de “c” e “c” fique com o valor de “a”? Declarando uma quarta variável para
# guardar o valor de a, variável d.

v1,v2,v3 = v2,v3,v1 # <-- Troca de variáveis
