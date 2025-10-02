def add_contact(contact, name, phone, email):
   contact = {"Nome": name, "Telefone": phone, "Email": email, "Favorito": False}
   contacts.append(contact)
   print(f"O contato {name} - {phone} - {email}, foi adicionado na agenda com sucesso.")
   return

def list_contacts(contact):
   print("\nLista de contatos: ")
   for i, contact in enumerate(contacts, start=1):
      favorite = "⭐" if contact["Favorito"] else " " 
      name = contact["Nome"]
      phone = contact["Telefone"]
      email = contact["Email"]
      print(f"{i}. [{favorite}] {name} - {phone} - {email}")
   return

def edit_contact(list_contact, i_list_contact, new_name, new_phone, new_email):
   i_update_contact = i_list_contact - 1
   if i_update_contact >= 0 and i_update_contact < len(list_contact):
      list_contact[i_update_contact]["Nome"] = new_name
      list_contact[i_update_contact]["Telefone"] = new_phone
      list_contact[i_update_contact]["Email"] = new_email
      print(f"\nContato {i_list_contact} foi atualizado com sucesso.")
      print(f"Nome: {new_name}; Telefone: {new_phone}; Email: {new_email}.")
   return

def mark_unmark_contact(contacts, i_list_contact, action):
   i_update_contact = i_list_contact - 1

   if i_update_contact < 0 or i_update_contact >= len(contacts):
      print(f"ÍNDICE INVÁLIDO.")
      return
   
   contact = contacts[i_update_contact]

   if action == "1":
      contact["Favorito"] = True
      print(f"Contato {contact["Nome"]} foi favoritado com sucesso.")
   elif action == "2":
      has_favorites = any(c.get("Favorito", False) for c in contacts)
      if not has_favorites:
         print("Não existe nenhum contato favoritado.")
      else:
         contact["Favorito"] = False
         print(f"Contato {contact["Nome"]} foi desfavoritado com sucesso.")
   else:
      print("ENTRADA INVÁLIDA")

def list_contact_favorite(contacts):
   print("\nLista de contatos favoritos: ")
   for i, contact in enumerate(contacts, start=1):
      if contact["Favorito"]:
         print(f"{i}. {contact["Nome"]} - {contact["Telefone"]} - {contact["Email"]}")
   return

def delete_contact(contacts, i_delete_contact):
   index = i_delete_contact - 1

   if index <= 0 or index >= len(contacts):
      print("ENTRADA INVÁLIDA.")

   removed_contact = contacts.pop(index)
   print(f"O contato {removed_contact["Nome"]} foi removido com sucesso.")

contacts = []
while True:
   print("\nMenu do Gerenciador de Agenda: ")
   print("1. Adicionar contato ")
   print("2. Listar contatos ")
   print("3. Editar contato ")
   print("4. Marcar ou Desmarcar contato ")
   print("5. Listar contatos favoritos ")
   print("6. Apagar contato ")
   print("7. Sair ")

   choose = input("Digite a sua escolha: ")
   if choose == "1":
      name = str(input("Digite o nome: "))
      phone = int(input("Digite o telefone(apenas números): "))
      email = str(input("Digite o email: "))
      add_contact(contacts, name, phone, email)
   elif choose == "2":
      list_contacts(contacts)
   elif choose == "3":
      list_contacts(contacts)
      i_list_contact = int(input("Digite o índice do contato que deseja atualizar: "))
      print("\nVai ser pedido todos os dados, o dado que não deseja atualizar, coloque o mesmo que está!")
      new_name = str(input("Digite o novo nome: "))
      new_phone = int(input("Digite o novo telefone(apenas números): "))
      new_email = str(input("Digite o novo email: "))
      edit_contact(contacts, i_list_contact, new_name, new_phone, new_email)
   elif choose == "4":
      action = input("Digite 1 - Favoritar ou 2 - Desfavoritar: ")
      list_contacts(contacts)
      i_list_contact = int(input("Digite o índice do contato que desejar marcar/desmarcar como favorito: "))
      mark_unmark_contact(contacts, i_list_contact, action)
   elif choose == "5":
      list_contact_favorite(contacts)
   elif choose == "6":
      list_contacts(contacts)
      i_delete_contact = int(input("Digite o índice do contato que deseja excluir: "))
      delete_contact(contacts, i_delete_contact)
   if choose == "7":
      break

print("PROGRAMA FINALIZADO.")