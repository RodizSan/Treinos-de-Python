#Exibir a MÉDIA entre duas notas de um aluno e imprimir se ele foi APROVADO, REPRIVADO/
#ou APROVADO COM DISTINÇÃO caso ultrapasse a média 7 
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
#Calcule a MÉDIA
media=(nota1+nota2)/2
#Imprime a MÉDIA do aluno
print("A média é", media)
#Caso a MÉDIA seja MENOR que 7
if media<7.0:
#Imprima Reprovado
    print("Reprovado.")
#Se a MÉDIA for MENOR que 10 (ou seja 9, 8, 7)
elif media<10:
#Imprima Aprovado
    print("Aprovado.")
#Se não, ou seja se não for nenhuma das anteriores, poderá ser apenas 10
else:
#Imprima APROVADO COM DISTINÇÃO
    print("Aprovado com Distinção!")
