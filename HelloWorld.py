# i recebe 57.9
i = float(57.9)

# j recebe i
j = i

print(type(i))
# printo i
print("I eh igual a {}".format(i))

# printo j
print("J eh igual a {}".format(j))

# verifico se i tem o mesmo valor que j
# DICA: Descomente a linha abaixo para ver o resultado do else
# i = 5
if i == j:
    print("valores iguais")
else: 
    print("valores diferentes")

# verifico se i é o mesmo objeto que j
if i is j: 
    print("objetos iguais")
else:
    print("objetos diferentes")


# Hello World em Python - 1a forma
print("Hello World! Hello Ligia e Agatha!")

# Hello World em Python - 2a forma
message = "Hello World! Ligia e Agatha"
print(message)

# Hello World em Python - 3a forma
message2 = str("Hello World! Ligia e Agatha")
print(message2)

