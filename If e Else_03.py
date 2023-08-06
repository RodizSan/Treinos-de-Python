#Verifucar se a letra digitada é VOGAL ou CONSOANTE
letra=str(input("Digite uma letra: "))
#O programa compra se a letra digitada é uma vogal, lembrando de comprar as maiusculas também
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or\
    letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
#Se na comparação for localizado alguma VOGAL, imprima a mensagem
    print("É uma VOGAL!")
#Se nenhuma letra digitada for uma VOGAL
else:
#Ela será CONSOANTE, imprima a mensagem
    print("É uma CONSOANTE!")