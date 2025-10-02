def adicionar_tarefa(tarefa, nome_tarefa):
   tarefa = {"tarefa": nome_tarefa, "completada": False}
   tarefas.append(tarefa)
   print(f"A tarefa {nome_tarefa} foi adicionada com sucesso.")
   return

def ver_lista_tarefas(tarefa):
   print("\nLista de tarefas: ")
   for indice, tarefa in enumerate(tarefas, start=1):
      status = "✔️" if tarefa["completada"] else " "
      nome_tarefa = tarefa["tarefa"]
      print(f"{indice}. [{status} ] {nome_tarefa}")

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
   indice_tarefa_ajustado = indice_tarefa - 1
   if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
      tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
      print(f"Tarefa {indice_tarefa} atualizado para {novo_nome_tarefa}")
   else:
      print("Índice da tarefa inválido")
   return
   

def completar_tarefa(tarefas, indice_tarefa):
   indice_tarefa_ajustada = indice_tarefa - 1
   tarefas[indice_tarefa_ajustada]["completada"] = True
   print(f"Tarefa {indice_tarefa} marcado como concluído.")
   return

def deletar_tarefa_completa(tarefas):
   for tarefa in tarefas:
      if tarefa["completada"]:
         tarefas.remove(tarefa)
   print("Tarefa completadas foram deletadas")
   return

tarefas = []

while True:
   print("\nMenu - Gerenciador de lista de tarefas")
   print("1. Adicionar Tarefa")
   print("2. Ver Lista de Tarefas")
   print("3. Atualizar Tarefa")
   print("4. Completar Tarefa")
   print("5. Deletar Tarefas Completas")
   print("6. Sair")

   escolha = input("Digite um número de sua escolha: ")
   if escolha == "1":
      nome_tarefa = str(input("Digite o nome da tarefa: "))
      adicionar_tarefa(tarefas, nome_tarefa)
   elif escolha == "2":
      ver_lista_tarefas(tarefas)
   elif escolha == "3":
      ver_lista_tarefas(tarefas)
      indice_tarefa = int(input("Digite o número da tarefa: "))
      novo_nome_tarefa = str(input("Digite o novo nome da tarefa: "))
      atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
   elif escolha == "4":
      ver_lista_tarefas(tarefas)
      indice_tarefa = int(input("Digite o número da tarefa que deseja ser concluída: "))
      completar_tarefa(tarefas, indice_tarefa)
   elif escolha == "5":
      deletar_tarefa_completa(tarefas)
      ver_lista_tarefas(tarefas)
   elif escolha == "6":
      break
   else:
      print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE")

print("PROGRAMA FINALIZADA!")
   