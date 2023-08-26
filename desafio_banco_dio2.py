import textwrap

def menu():
    menu = """\n
    [d]\tDeposita
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListagem de contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def deposita(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n**** Depósito realizado com sucesso! ****")
    else:
        print("\n**** Não foi possível realizar a operação! Valor inválido!!! ****")    

    return saldo, extrato    

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n**** Operação falhou! Você não possui saldo suficiente ****")

    elif excedeu_limite:
        print("\n**** Operação falhou! Saque excede o limite ****")

    elif excedeu_saques:
          print("\n**** Operação falhou! Número de saques passou do limite ****")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n**** Saque realizado com sucesso! ****")

    else:
        print("\n**** Falhou! Valor informado não é válido. ****")    

    return saldo, extrato    

def exibe_extrato(saldo, /,*, extrato):
     print("\n--------- EXTRATO ---------")
     print("Não foram realizadas movimentações. " if not extrato else extrato)
     print(f"\nSaldo:\t\tR$ {saldo:.2f}")
     print("-----------------------------")

def cria_usuario(usuarios):
     cpf = input("Informe o CPF (somente número): ")
     usuario = filtra_usuario(cpf, usuarios)

     if usuario:
          print("\n**** Já existe um usuário com esse CPF!!!! ****")
          return
     
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print("****Usuário foi criado com sucesso!****")
 

def filtra_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
     
def cria_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print("\n**** Conta criada com sucesso! ****")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n**** Usuário não encontrado, fluxo de criação de conta encerrado! ****")  

def listar_usuarios(contas) : 
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}

"""      
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0  
    usuarios = []
    contas = []

    while True:
          opcao = menu()

          if opcao == "d":
             valor = float(input("Informe o valor do depósito: "))
             
             saldo, extrato = deposita(saldo, valor, extrato)

          elif opcao == "s":
              valor = float(input("Informe o valor do saque: "))

              saldo, extrato = saque(
                   saldo = saldo,
                   valor= valor,
                   extrato = extrato,
                   limite = limite,
                   numero_saques = numero_saques,
                   limite_saques = LIMITE_SAQUES,
              )


          elif opcao == "e":
               exibe_extrato(saldo, extrato =extrato)

          elif opcao == "nu":
               cria_usuario(usuarios)

          elif opcao == "nc": 
                numero_conta = len(contas) + 1
                conta = cria_conta(AGENCIA, numero_conta, usuarios)
        
                if conta:
                  contas.append(conta)
          
          elif opcao == "lc":
               listar_usuarios(contas)        

          elif opcao == "q":
                break

          else:
              print("Operação inválida, por favor selecione novamente a operação desejada.")         

main()                