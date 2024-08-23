# define a função com a soma, e retorna o resultado à função
def somar(a, b):
    return a+b

# printar olá!
print("Olá, Usuário!")

# perguntar e printar o nome do usuário
name = input("Qual é o seu nome? ")
name = name.strip().title()
print("Prazer em te conhecer", name)


# perguntar qual o valor para a soma, e formatá-lo
b = int(input("Qual o primeiro valor para a soma? "))
c = int(input("Qual o segundo valor para a soma? "))

# a soma dos dois valores dentro da função definida = resultado
resultado = somar(b, c)

# printar o resultado da soma
print("O resultado da soma é: ", resultado)
print("Obrigado por usar este software! :)")
