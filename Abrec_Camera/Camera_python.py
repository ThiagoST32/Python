import cv2
import mysql.connector
import uuid
import os
import random
import string
from PIL import Image

# Estabelecer conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localHost',
    user='root',
    password='Bnas123!@#',
    database='test'
)
cursor = conexao.cursor()

vid = cv2.VideoCapture(0)
tamanho_nome = 10

def gerar_nome_aleatorio(tamanho):
    nome_aleatorio = uuid.uuid4().hex[:tamanho]
    return nome_aleatorio

while True:
    ret, frame = vid.read()
    cv2.imshow("Janela", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{}.png".format(gerar_nome_aleatorio(tamanho_nome))
        if not os.path.exists(StoreFilePath):
                os.makedirs(StoreFilePath)
        # Insere a imagem no banco de dados
        consulta = "INSERT INTO imagens (nome, caminho) VALUES (%s, %s)"
        valores = ("capture{}.png".format(gerar_nome_aleatorio(tamanho_nome)), StoreFilePath)
        cursor.execute(consulta, valores)
        # Salva as alterações
        conexao.commit()
        image_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image_pil.save(StoreFilePath)
        print("Imagem salva em:", StoreFilePath)
        break
        

vid.release()
cv2.destroyAllWindows()
# Fecha a conexão
cursor.close()
conexao.close()
