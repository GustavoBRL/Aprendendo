def main():
    x = int(input("Qual o X, novamente? "))

    if Épar(x):
        print("É Par.")
    else:
        print("É Ímpar")


def Épar(n):
    if n % 2 == 0:
        return True
    else:
        return False


#Atribuir valor à variável para comparação
x = int(input("Qual o X? "))

if x % 2 == 0:
    print("X é Par")

else:
    print("X é Ímpar")

#Realizando a mesma ação, pporém com funções definidas
print("Agora, vamos à segunda parte do exercício.")

main()
