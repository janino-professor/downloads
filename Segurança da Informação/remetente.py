import socket

def cifrar_afim(texto, multiplicador=3, chave=5):
    """Aplica a Cifra Afim multiplicando e somando as posições."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            posicao_antiga = ord(char) - base
            posicao_nova = (posicao_antiga * multiplicador + chave) % 26
            resultado += chr(posicao_nova + base)
        else:
            resultado += char
    return resultado

# Configuração da rede do laboratório
IP_DESTINO = "10.0.10.255" 
PORTA = 5005

mensagem_original = "SEGURANCA DA INFORMACAO NA ESCOLA"

# =====================================================================
# PARA MUDAR DE ETAPA, BASTA INVERTER O '#' DE LUGAR:
# =====================================================================

# ETAPA 1: Enviar sem criptografia (deixe esta linha ATIVA e a de baixo comentada)
#mensagem_envio = mensagem_original  

# ETAPA 2: Enviar com criptografia (comente a de cima e DEIXE ESTA ATIVA)
mensagem_envio = cifrar_afim(mensagem_original, multiplicador=3, chave=5)


# Envio via Socket UDP (Sempre usa a variável 'mensagem_envio')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(mensagem_envio.encode('utf-8'), (IP_DESTINO, PORTA))

print(f"[REMETENTE] Mensagem Original: {mensagem_original}")
print(f"[REMETENTE] Mensagem Enviada pela rede: {mensagem_envio}")