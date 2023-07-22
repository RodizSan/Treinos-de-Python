nome=input('Digite seu nome completo: ').upper().strip()
if nome=='RODRIGO CONDE SANTOS':
    print('Usuário válido!' .upper())
else:
    print('Usuário inválido!')
idade=input('Digite sua idade: ') .strip()
if idade >='0' and idade <='9':
    idade=int(idade)
    if idade <18:
        print('Sinto muito, mas só aceitamos maiores de idade.')
    else:
        print('Usuário permitido!')