import mysql.connector
import cv2
import uuid

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
        StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/{}.png".format(gerar_nome_aleatorio(tamanho_nome))
        # Insere a imagem no banco de dados
        consulta = "INSERT INTO imagens (nome, caminho) VALUES (%s, %s)"
        valores = ("{}.png".format(gerar_nome_aleatorio(tamanho_nome)), StoreFilePath)
        cursor.execute(consulta, valores)
        # Salva as alterações
        conexao.commit()
        break

vid.release()
cv2.destroyAllWindows()
# Fecha a conexão
cursor.close()
conexao.close()
