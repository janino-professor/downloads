# intale o cryptography executando pip install cryptography
from cryptography.fernet import Fernet
import socket

# 1. Geração de uma chave simétrica segura (na prática, ela deve ser trocada de forma segura)
# Para fins didáticos, geramos e exibimos a chave:
chave = Fernet.generate_key()
cifrador = Fernet(chave)

print(f"[SISTEMA SEGURO] Chave simétrica gerada: {chave.decode()}")

mensagem_original = b"DADOS CONFIDENCIAIS DA ESCOLA"

# 2. Criptografia forte (AES)
mensagem_protegida = cifrador.encrypt(mensagem_original)
print(f"[REMETENTE] Mensagem Cifrada (AES): {mensagem_protegida}")

# 3. Simulando a descriptografia legítima pelo Destinatário que possui a chave
mensagem_revelada = cifrador.decrypt(mensagem_protegida)
print(f"[DESTINATARIO] Mensagem Descriptografada com Sucesso: {mensagem_revelada.decode()}")