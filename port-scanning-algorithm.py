import socket

# Endereço IP do alvo
ip_alvo = "192.168.0.1"

# Fica em loop por todas as portas
for porta in range(1, 65535):
    # Cria o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Tenta se conectar à porta
    conexao = s.connect_ex((ip_alvo, porta))

    # Verifica se a conexão foi bem-sucedida
    if conexao == 0:
        print("Porta {} aberta!".format(porta))
    s.close()
