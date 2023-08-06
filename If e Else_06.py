#O programa solicita três números ao usuário e imprimir o MAIOR e o MENOR
num1=int(input("Digite o 1° N: "))
num2=int(input("Digite o 2° N: "))
num3=int(input("Digite o 3° N: "))
#A variável maior armazena o valor de num1 para auxiliar na comparação
maior=num1
#Se o valor de num2 for maior que da variável maior
if (num2>maior):
#Então a variável maior recebe o valor digitado em num2
    maior=num2
#Se o valor de num3 for maior que da variável maior
if (num3>maior):
#Então a variável maior recebe o valor digitado em num3
    maior=num3
#Após a comparação imprima o valor MAIOR, agora armazenado na variável maior
print("O maior é ",maior)
#A variável menor armazena o valor de num1 para auxiliar na comparação
menor=num1
#Se o valor de num2 for menor que da variável menor
if (num2<menor):
#Então a variável menor recebe o valor digitado em num2
    menor=num2
#Se o valor de num3 for menor que da variável menor
if (num3<menor):
#Então a variável menor recebe o valor digitado em num3
    menor=num3
#Após a comparação imprima o valor MENOR, agora armazenado na variável menor
print("O menor é ",menor)