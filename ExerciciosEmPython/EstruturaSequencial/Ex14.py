tamanho_arquivo = int(input("Digite o tamanho do arquivo(MB): "))
vel_internet = int(input("Digite a velocidade da internet(Mbps): "))
tamanho_mbps = tamanho_arquivo * 8
tempo = tamanho_mbps / vel_internet
tempo_minutos = tempo / 60
print(f"O tempo aproximado para fazer o download vai ser de: {tempo_minutos:.2f} minutos.")


