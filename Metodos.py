# Método que realiza a soma entre dois numeros
def soma(x, y):
    return x + y

# Método que realiza a subtracao entre dois numeros
def subtracao(x, y):
    return x - y

# Método que realiza a multiplicacao entre dois numeros
def multiplicacao(x, y):
    return x * y

# Método que realiza a multiplicacao entre dois numeros
def divisao(x, y):
    return x / y

# Método que realiza a verficacao entre dois numeros
def isSmall(x, y):
    return x < y

# Desafio: criar um loop que acesse cada posicao da minha lista 
# e faça um print dizendo -> Olá <nome>

# Etapas do loop
# - acessar cada item da lista
# - printar o valor na frase

nomes = ["Pedro", "Ligia", "Agatha"]
print(nomes)

# Para obtermos o tamanho da lista usamos a função len() passando a lista como parametro (olhe a linha abaixo)
print(len(nomes))

# Loop usando While
# Para fazermos um loop usando a estrutura de repetição while é necessário criar 
# uma variável de controle para que o loop realize um número definido de iterações
# evitando que ele seja um loop infinito

print("inicio do loop")
# criando a variavel de controle
i = 0
# verificando se a variavel obedece a verificação
# DICA: Experimente trocar o valor da verificação para um valor maior ou menor que o tamanho da lista
while i < 3:
    # caso a variavel obedeça a verificação é realizado um print usando i como indice
    # de acesso a lista de nomes
    print(nomes[i])

    # por último a variável de controle deve ser iterada para que o loop possa prosseguir
    i+=1
    # após a linha de código acima o fluxo do programa volta para a linha 39 onde i é verificado
    # caso obedeça a verificação o loop continua, caso contrário o programa passa para
    # o próximo comando (nesse caso para a linha 50)
print("fim do loop")

# Loop usando for
# Diferente do while, para usarmos a estrutura de repetição for não é necessário 
# que criemos uma variável de controle. Apenas devemos criar uma variável que receberá
# um valor da lista a cada iteração

print("inicio do loop")

for resposta in nomes:
    # DICA: Experimente fazer um print(resposta) para ver os valores que a variável recebe a cada iteração
    print("Ola {}".format(resposta))

# No caso acima a cada iteração do loop, a variável resposta recebeu um valor da lista, ou seja,
# na primeira iteração resposta = nomes[0]
# na segunda iteração respota = nomes[1]
# na terceira iteração resposta = nomes[2]
# E o loop acaba, sendo o código da linha 67 o próximo comando a ser executado 
print("fim do loop")
