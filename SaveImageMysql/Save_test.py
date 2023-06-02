import mysql.connector
from PIL import Image
import io
import imghdr


myDB = mysql.connector.connect(
    host = "localHost",
    user = "root",
    password = "Bnas123!@#",
    database = "test"
)

MyCursor = myDB.cursor()


def InsertBlob(FilePath):
    with open (FilePath,"rb") as File:
        BinaryData = File.read()
    SQlStatement = "INSERT INTO imagens (nome) values (%s)"
    MyCursor.execute(SQlStatement, (BinaryData))
    myDB.commit()

def UpdateBlob(id, FilePath):
    with open (FilePath, "wb") as File:
        BinaryData = File.read()
    SQLStatement3 = 'UPDATE imagens SET imagem = %s WHERE id= %s'
    MyCursor.execute(SQLStatement3,(BinaryData, id))
    myDB.commit()



def RetrieveImageBytes(ID):
    SQLStatement2 = "SELECT * FROM imagens WHERE id = '{0}'"
    MyCursor.execute(SQLStatement2.format(str(ID)))
    MyResult = MyCursor.fetchone()[1]
    image_format = imghdr.what("capture49acde6468.jpg", h = MyResult.encode())
    if image_format:
        image = Image.open(io.BytesIO(MyResult))
        StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{0}.png".format(str(ID))
        image.save(StoreFilePath, "png")
    else:
        print("The retrieved data is not a valid image.")

def RetrieveBlob(ID):
    SQLStatement2 = "SELECT * FROM imagens WHERE id = '{0}'"
    MyCursor.execute(SQLStatement2.format(str(ID)))
    MyResult2 = MyCursor.fetchone()[1]
    StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/Imagens_Banco_Teste/capture{}.png".format(str(ID))
    print (MyResult2)
    with open (StoreFilePath, "wb") as File:
        File.write(MyResult2)
        File.close()
        
        
    # with open(StoreFilePath, "wb") as File:
    #     File.write(MyResult.encode('utf-8'))
    #     File.close()
    # image = Image.open(io.BytesIO(MyResult.encode('utf-8')))
    # StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{0}.png".format(str(ID))
    # image.save(StoreFilePath)
    
    
print("1.Insert Image \n2.Read Image\n3.Read Image Bytes\n4.Update Image")
MenuInput = input("Number:")    


if int (MenuInput) == 0 or 0 > 1:
    raise TypeError("Porfavor Selecione uma opção!")

elif int (MenuInput) == 1:
    UserFilePath = input ("Enter File Path:")
    InsertBlob (UserFilePath)
elif int (MenuInput) == 2:
    UserIdChoice = input("Enter ID:")
    RetrieveBlob(UserIdChoice)
elif int (MenuInput) == 3:
    UserFileBytes = input ("Enter Id Image:")
    RetrieveImageBytes(UserFileBytes)
elif int (MenuInput) == 4:
    UpdateImage = input("Enter Id Image:")
    UserFilePath = input("Enter FilePath:")
    UpdateBlob(UpdateImage,UserFilePath)



