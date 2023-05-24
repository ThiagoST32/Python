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


        # StoreFilePath2 = "SELECT * FROM imagens WHERE id = '{0}'"
        # cursor.execute(StoreFilePath2.format(str(id)))
# .format(StoreFilePath2)

# import cv2

# vid = cv2.VideoCapture(0)

# while True:
#     ret, frame = vid.read()
#     cv2.imshow("Janela", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# vid.release()
# cv2.destroyAllWindows()












































# import mysql.connector
# import cv2




# # Estabelecer conexão com o banco de dados
# conexao = mysql.connector.connect(
#     host='localHost',
#     user='root',
#     password='Bnas123!@#',
#     database='test'
# )
# cursor = conexao.cursor()

# vid = cv2.VideoCapture(0)

# if not vid.isOpened():
#     print("Erro ao abrir o vídeo.")
#     exit()

# def RetrieveBlob(ID):
#     while True:
#         ret, frame = vid.read()
#         cv2.imshow("Janela", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             # Insere a imagem no banco de dados
#             consulta = "INSERT INTO imagens (nome, caminho) VALUES (%s, %s)"
#             valores = ('capture{}.png'.format(ID), StoreFilePath)
#             cursor.execute(consulta, valores)
#             # Salva as alterações
#             conexao.commit()
#             # Fecha a conexão
#             cursor.close()
#             conexao.close()
#             StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{}.png".format(ID)
#             cv2.imwrite(StoreFilePath, frame)
#             break
#     vid.release()
#     cv2.destroyAllWindows()

# TABELA CRIADA!

# cursor = conexao.cursor()
# cursor.execute('''
#     CREATE TABLE imagens (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         nome VARCHAR(100),
#         caminho VARCHAR(200)
#     )
# ''')



# # Caminho completo do arquivo
# file_path = os.path.join(directory, filename)

# # Verifique se o arquivo existe antes de abri-lo
# if os.path.exists(file_path):
#     print("Imagem Encontrada!")
#     imagem = Image.open(file_path)
#     # Restante do seu código para trabalhar com a imagem aberta
# else:
#     print("O arquivo não foi encontrado.")
# # Converta a imagem em bytes
# imagem_bytes = directory.tobytes()







# # Insira a imagem no banco de dados
# consulta = '''
#     INSERT INTO imagens (nome, caminho) VALUES (%s, %s)
# '''
# valores = ('capture3.png', './test/')
# cursor.execute(consulta, valores)

# # Salve as alterações
# conexao.commit()

# # Feche a conexão
# cursor.close()
# conexao.close()

# # Nome do arquivo que você deseja abrir
# filename = "capture3.png"

# # Diretório onde o arquivo está localizado
# directory = Image.open("C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture3.png")









# import cv2
# local_img="my_img.png"# caminho da imagem
# img = cv2.imread(local_img)
# cv2.imshow("Janela", img) # cria janela
# k = cv2.waitKey(0) # mostra jamela criada e aguarda evento de uma tecla
# if k == ord("s"): # se s for pressionado salva a imagem
#     cv2.imwrite("starry_night.png", img)
# cv2.destroyAllWindows()