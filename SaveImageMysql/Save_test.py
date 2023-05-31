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
    SQlStatement = "INSERT INTO imagens (imagem) values (%s)"
    MyCursor.execute(SQlStatement, (BinaryData, ))
    myDB.commit()

def RetrieveBlob(ID):
    SQLStatement2 = "SELECT * FROM imagens WHERE id = '{0}'"
    MyCursor.execute(SQLStatement2.format(str(ID)))
    # StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/"
    MyResult = MyCursor.fetchone()[1]
    image_format = imghdr.what("capture49acde6468.jpg", h =MyResult.encode())
    
    if image_format:
        image = Image.open(io.BytesIO(MyResult))
        StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{0}.png".format(str(ID))
        image.save(StoreFilePath, "png")
    else:
        print("The retrieved data is not a valid image.")


# # This portion is part of my test code
# byteImgIO = io.BytesIO()
# byteImg = Image.open("some/location/to/a/file/in/my/directories.png")
# byteImg.save(byteImgIO, "PNG")
# byteImgIO.seek(0)
# byteImg = byteImgIO.read()





    # with open(StoreFilePath, "wb") as File:
    #     File.write(MyResult.encode('utf-8'))
    #     File.close()
    # image = Image.open(io.BytesIO(MyResult.encode('utf-8')))
    # StoreFilePath = "C:/Users/User/Desktop/Codigos/Python/Abrec_Camera/test/capture{0}.png".format(str(ID))
    # image.save(StoreFilePath)
    





print("1. Insert Image \n2.Read Image")
MenuInput = input()
if int (MenuInput) == 1:
    UserFilePath = input ("Enter File Path:")
    InsertBlob (UserFilePath)
elif int (MenuInput) == 2:
    UserIdChoice = input("Enter ID:")
    RetrieveBlob(UserIdChoice)