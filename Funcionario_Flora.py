funcionarios = []


def cpf_valido(cpf):
    """Verifica se o CPF tem 11 dígitos e é composto apenas por números."""
    return cpf.isdigit() and len(cpf) == 11


def cpf_existe(cpf):
    """Verifica se o CPF já está cadastrado no sistema."""
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            return True
    return False


def add_funcionario():
    print("Digite os dados do funcionário:")
    
    # Verificação do CPF
    while True:
        cpf = input("Digite o CPF do funcionário: ")
        if not cpf_valido(cpf):
            print("CPF inválido! Certifique-se de que contém 11 dígitos.")
            continue
        if cpf_existe(cpf):
            print("CPF já cadastrado no sistema!")
            return
        break

    nome = input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    cidade = input("Digite a cidade do funcionário: ")
    estado = input("Digite o estado do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    email = input("Digite o email do funcionário: ")
    escolaridade = input("Digite a escolaridade do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")

    funcionario = {
        "cpf": cpf,
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "estado": estado,
        "salario": salario,
        "email": email,
        "escolaridade": escolaridade,
        "cargo": cargo
    }
    
    
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} adicionado com sucesso!")


def atualizar_funcionario():
    cpf = input("Digite o CPF do funcionário a ser atualizado: ")
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            print("Digite os novos dados do funcionário:")
            funcionario["nome"] = input("Digite o nome do funcionário: ")
            funcionario["idade"] = int(input("Digite a idade do funcionário: "))
            funcionario["cidade"] = input("Digite a cidade do funcionário: ")
            funcionario["estado"] = input("Digite o estado do funcionário: ")
            funcionario["salario"] = float(input("Digite o salário do funcionário: "))
            funcionario["email"] = input("Digite o email do funcionário: ")
            funcionario["escolaridade"] = input("Digite a escolaridade do funcionário: ")
            funcionario["cargo"] = input("Digite o cargo do funcionário: ")
            print(f"Funcionário {funcionario['nome']} atualizado com sucesso!")
            return
    print(f"Funcionário com CPF {cpf} não encontrado.")


def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("Lista de funcionários:")
        for funcionario in funcionarios:
            print(f"Nome: {funcionario['nome']}, CPF: {funcionario['cpf']}, Cargo: {funcionario['cargo']}")


def excluir_funcionario():
    cpf = input("Digite o CPF do funcionário a ser excluído: ")
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            funcionarios.remove(funcionario)
            print(f"Funcionário {funcionario['nome']} excluído com sucesso!")
            return
    print(f"Funcionário com CPF {cpf} não encontrado.")


def start_sistema():
    while True:
        print("\nMenu:")
        print("1. Adicionar funcionário")
        print("2. Atualizar funcionário")
        print("3. Listar funcionários")
        print("4. Excluir funcionário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            add_funcionario()
        elif opcao == "2":
            atualizar_funcionario()
        elif opcao == "3":
            listar_funcionarios()
        elif opcao == "4":
            excluir_funcionario()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


executar = start_sistema()