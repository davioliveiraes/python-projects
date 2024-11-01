import sys
import os
sys.path.append(os.path.abspath(os.curdir))

import __init__
from model.password import Password
from view.password_views import FernetHasher

if __name__ == '__main__':
   action = input("Digite 1 para salvar um nova senha ou 2 para ver determinda senha: ")
   match action:
      case '1':
         if len(Password.get()) == 0:
            key, path = FernetHasher.create_key(archive=True)
            print("Sua chave foi criada, salve-a com cuidado caso a parca não poderá recuperar suas senhas.")
            print(f"Chave: {key.decode('utf-8')}")
            if path:
               print("Chave salva no arquivo, lembre-se de remover o arquivo após transferir de local")
               print(f"Caminho: {path}")
         else:
            key = input("Digite sua chave usada para criptografia, use sempre a mesma chave: ")
            
         domain = input("Domínio: ")
         password = input("Digite a senha: ")
         fernet = FernetHasher(key)
         p1 = Password(domain=domain, password=fernet.encrypt(password).decode('utf-8'))
         p1.save()
      
      case '2':
         domain = input("Domínio: ")
         key = input("Key: ")
         fernet = FernetHasher(key)
         data = Password.get()
         password = ''
         for i in data:
            if domain in i['domain']:
               password = fernet.decrypt(i['password'])
         if password:
            print(f"Sua senha: {password}")
         else:
            print("Nenhuma senha encontrada para esse domínio.")
