#Calculadora Romantica
#Digite o seu nome
nome1=input("Digite seu nome: ")
#Digite o nome da sua namorada(o)
nome2=input("Digite outro nome: ")
#Agora na variável nome1, digite o nome da sua namorada e na variável nome2 digite o seu nome,/
# para o programa sempre combinar o casal
if nome1=="nome_da_namorada" and nome2=="seu_nome":
#Agora o programa imprime a mensagem que o casal combina
        print("Vocês super-combinam!")
#Caso a ordem dos nomes seja invertida também dá certo
elif nome1=="seu_nome" and nome2=="nome_da_namorada":
#O programa imprime a mensagem que o casal combina
    print("Vocês super-combinam!")
#Caso contrário, ou seja, qualquer nome ou combinação será impresso uma mensagem negativa
else:
#Imprima uma resposta onde a combinação doferente da pré-programada seja negativa a combinação
    print("Desculpe, vocês não combinam.")
