contacts = []

def display_menu():
    print("\n" + "=" * 40)
    print("AGENDA DE CONTATOS")
    print("=" * 40)
    print("[1] - Adicionar contato")
    print("[2] - Listar contatos")
    print("[3] - Editar contato")
    print("[4] - Favoritar/Desfavoritar contato")
    print("[5] - Listar favoritos")
    print("[6] - Apagar contato")
    print("[0] - Sair")

def main():
    while True:
        display_menu()
        option = input("Escolha uma opção: ").strip()

        match option:
            case "1":
                add_contact()
            case "2":
                list_contacts()
            case "3":
                edit_contact()
            case "4":
                toggle_favorite()
            case "5":
                list_favorites()
            case "6":
                delete_contact()
            case "0":
                print("\nAté logo")
                break
            case _:
                print("\n Opção inválida. Tente novamente.")

def add_contact():
    print(" === NOVO CONTATO === ")

    name = input("Nome: ").strip()
    if not name:
        print("Nome é obrigatório!")
        return

    phone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    favorite_input = input("Marcar como favorito? [s/n]").strip().lower()
    favorite = favorite_input == "s"

    contact = {"nome": name, "telefone": phone, "email": email, "favorito": favorite}

    contacts.append(contact)
    print(f"\nContato {name} foi adicionado com sucesso!")

def list_contacts():
    print(" === LISTA DE CONTATOS === ")

    if not contacts:
        print("Nenhum contato cadastrado")
        return {}

    contacts_with_index = list(enumerate(contacts))

    ordered_contacts = sorted(
        contacts_with_index,
        key=lambda x: (not x[1]["favorito"], x[1]["nome"].lower())
    )

    mapping = {}

    for position, (real_indice, contact) in enumerate(ordered_contacts, start=1):
        mapping[position] = real_indice
        star = "⭐" if contact["favorito"] else " "
        print(f"\n{star} [{position}] {contact["nome"]}")
        print(f"    {contact["telefone"] or "Não informado"}")
        print(f"    {contact["email"] or "Não informado"}")

    print(f"\nTotal: {len(contacts)} contato(s)")

    return mapping

# Auxilio para seleção de contato
def select_contact(message="Digite o número do contato: "):
    mapping = list_contacts()

    if not mapping:
        return None
    
    try:
        position = int(input(f"\n{message}"))

        if position not in mapping:
            print("Número inválido")
            return None

        return mapping[position]
    
    except ValueError:
        print("Digite um número válido")
        return None

def edit_contact():
    print(" === EDITAR CONTATO === ")

    index = select_contact("Digite o número do contato para editar: ")

    if index is None:
        return
    
    contact = contacts[index]
    print(f"\nEditando: {contact["nome"]}")
    print("(Pressione Enter para manter o valor atual)\n")

    new_name = input(f"Nome [{contact["nome"]}]: ").strip()
    new_phone = input(f"Telefone [{contact['telefone']}]: ").strip()
    new_email = input(f"Email [{contact['email']}]: ").strip()

    if new_name:
        contact["nome"] = new_name
    if new_phone:
        contact["telefone"] = new_phone
    if new_email:
        contact["email"] = new_email
    
    print("\nContato atualizado com sucesso!")

def toggle_favorite():
    print(" === FAVORITAR/DESFAVORITAR === ")

    index = select_contact("Digite o número do contato: ")

    if index is None:
        return
    
    contact = contacts[index]
    contact["favorito"] = not contact["favorito"]

    status = "adicionado aos" if contact["favorito"] else "removido dos"
    print(f"\n '{contact["nome"]}' foi {status} favoritos!")

def list_favorites():
    print(" === LISTA DE FAVORITOS === ")

    favorites = [(i, c) for i, c in enumerate(contacts) if c["favorito"]]

    if not favorites:
        print("Nenhum contato favorito.")
        return {}

    favorites_sorted = sorted(favorites, key=lambda x: x[1]["nome"].lower())

    mapping = {}

    for position, (real_index, contact) in enumerate(favorites_sorted, start=1):
        mapping[position] = real_index
        print(f"\n⭐ [{position}] {contact["nome"]}")
        print(f"         {contact["telefone"] or 'Não informado'}")
        print(f"         {contact["email"] or 'Não informado'}")
    
    print(f"\nTotal: {len(favorites)} favorito(s)")

def delete_contact():
    print(" === APAGAR CONTATO === ")

    index = select_contact("Digite o número do contato para apagar: ")

    if index is None:
        return
    
    contact = contacts[index]
    confirmation = input(f"Tem certeza que deseja apagar '{contact["nome"]}'?[s/n] ").strip().lower()

    if confirmation == "s":
        contacts.pop(index)
        print("\nContato apagado com sucesso!")
    else:
        print("\nOperação cancelada!")

if __name__ == "__main__":
    main()
