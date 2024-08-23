# define a função com a soma, e retorna o resultado à função
def somar(a, b):
    return a+b

# a soma dos dois valores dentro da função definida = resultado
resultado = somar(5, 5)

# printar olá!
print("Hello, User!")

# perguntar e printar o nome do usuário
name = input("What's your name? ")
print("Nice to meet you,", name)

# printar o resultado da soma
print("Agora, o resultado da soma que vc pensou é: ", resultado)
# não é obrigatório atribuir a função com seu valor à uma variável 
# (resultado), poderia se referir à função como ela está (somar(5, 5))
# mas é melhor assim