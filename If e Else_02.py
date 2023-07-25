senha=input("Digite sua senha: ")

if senha=="admin":
    print("Olá Administrador!")
elif senha=="user":
    print("Olá Usuário!")
else:
    print("Acesso negado. Verifique sua senha.")