#O programa recebe três valores do usuário para imprimir o MAIOR valor entre ele
num1=int(input("Digite o 1° N: "))
num2=int(input("Digite o 2° N: "))
num3=int(input("Digite o 3° N: "))
#Compara o valor UM com os demais
if (num1>=num2 and num1>=num3):
#Se ele for o maior, imprima
    print("O 1° é o maior!")
#Compara o valor DOIS com os demais
elif (num2>num1 and num2>num3):
#Se ele for maior, imprima
    print("O 2° é o maior!")
#Caso contrário o TERCEIRO será o MAIOR
else:
#Se o TERCEIRO for MAIOR 
    print("O 3° é o maior!")