import csv
import os

matriculacsv = 'alunos.csv'
objetivoEmail = 'objetivo_email.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print(f'''================ ALUNOS ================
[1] Cadastrar aluno
[2] Editar aluno
[3] Deletar cadastro de aluno
[4] Procurar aluno
[5] Registrar objetivo e e-mail
[6] Editar objetivo e e-mail
[0] Sair
=======================================''')
    selected_menu = input("Escolha uma alternativa => ")

    if selected_menu == "1":
        criar_aluno()
    elif selected_menu == "2":
        editar_contato()
    elif selected_menu == "3":
        deletar_aluno()
    elif selected_menu == "4":
        consultar_aluno()
    elif selected_menu == "5":
        registrar_info()
    elif selected_menu == "6":
        editar_info()
    elif selected_menu == "0":
        exit()
    else:
        print("ALTERNATIVA INVÁLIDA!!!")
        back_to_menu()

def back_to_menu():
    input("\nPressione ENTER para voltar")
    show_menu()

def criar_aluno():
    clear_screen()
    with open(matriculacsv, mode='a', newline="") as csvFile:
        fieldNames = ['CPF', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        cpfinput = input("CPF: ")
        nome = input("Nome Completo: ")
        celular = input("Número de telefone: ")
        writer.writerow({'CPF': cpfinput, 'NOME': nome, 'CELULAR': celular})
        print("Aluno cadastrado com sucesso!")
    back_to_menu()

def registrar_info():
    clear_screen()
    with open(objetivoEmail, mode='a', newline="") as csvFile:
        fieldNames = ['CPF', 'OBJETIVO', 'EMAIL']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        cpf = input("CPF: ")
        objetivo = input("Objetivo: ")
        email = input("E-mail: ")
        writer.writerow({'CPF': cpf, 'OBJETIVO': objetivo, 'EMAIL': email})
        print("Informações cadastradas com sucesso!")
    back_to_menu()

def editar_contato():
    clear_screen()
    contacts = []
    with open(matriculacsv, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'CPF \t\t NOME \t\t CELULAR')
    for data in contacts:
        print(f'{data["CPF"]} \t\t {data["NOME"]} \t\t {data["CELULAR"]}')
    matricula = input("CPF: ")
    nome = input("Novo nome: ")
    celular = input("Novo número: ")
    for data in contacts:
        if data['CPF'] == matricula:
            data['NOME'] = nome
            data['CELULAR'] = celular
            break
    with open(matriculacsv, mode="w", newline="") as csvFile:
        fieldNames = ['CPF', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        writer.writerows(contacts)
    print("Cadastro do aluno atualizado com sucesso!")
    back_to_menu()

def editar_info():
    clear_screen()
    contacts = []
    with open(objetivoEmail, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'CPF \tOBJETIVO\t EMAIL')
    for data in contacts:
        print(f'{data["CPF"]} \t {data["OBJETIVO"]} \t {data["EMAIL"]}')
    cpf = input("CPF: ")
    objetivo = input("Objetivo atual: ")
    email = input("Novo e-mail: ")
    for data in contacts:
        if data['CPF'] == cpf:
            data['OBJETIVO'] = objetivo
            data['EMAIL'] = email
            break
    with open(objetivoEmail, mode="w", newline="") as csvFile:
        fieldNames = ['CPF', 'OBJETIVO', 'EMAIL']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        writer.writerows(contacts)
    print("Informações do aluno atualizadas com sucesso!")
    back_to_menu()

def deletar_aluno():
    clear_screen()
    contacts = []
    with open(matriculacsv, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'CPF \t NOME COMPLETO \t CELULAR')
    for data in contacts:
        print(f'{data["CPF"]} \t {data["NOME"]} \t {data["CELULAR"]}')
    cpfdel = input("CPF a ser deletado: ")
    contacts = [data for data in contacts if data['CPF'] != cpfdel]
    with open(matriculacsv, mode="w", newline="") as csvFile:
        fieldNames = ['CPF', 'NOME', 'CELULAR']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        writer.writerows(contacts)
    print("Cadastro do aluno deletado com sucesso!")
    back_to_menu()

def consultar_aluno():
    clear_screen()
    contacts = []
    with open(matriculacsv, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    emails = []
    with open(objetivoEmail, mode="r", newline="") as csvemail:
        csvReader = csv.DictReader(csvemail, delimiter=',')
        for row2 in csvReader:
            emails.append(row2)
    cpflab = input("Procurar pelo CPF: ")
    data_found = None
    email_found = None
    for data in contacts:
        if data['CPF'] == cpflab:
            data_found = data
            break
    for email in emails:
        if email['CPF'] == cpflab:
            email_found = email
            break
    if data_found and email_found:
        print(f'''DADOS ENCONTRADOS: 
        Nome: {data_found['NOME']}
        Celular: {data_found['CELULAR']}
        Objetivo: {email_found['OBJETIVO']} 
        Email: {email_found['EMAIL']}''')
    else:
        print("Aluno não encontrado.")
    back_to_menu()

if __name__ == "__main__":
    show_menu()