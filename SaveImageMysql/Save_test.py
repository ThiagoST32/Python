import mysql.connector

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
    SQlStatement = "INSERT INTO imagem_save (imagem) values (%s)"
    MyCursor.execute(SQlStatement, (BinaryData, ))
    myDB.commit()


def RetrieveBlob(ID):
    SQLStatement2 = "SELECT * FROM imagem_save WHERE id = '{0}'"
    MyCursor.execute(SQLStatement2.format(str(ID)))
    MyResult = MyCursor.fetchone()[1]
    StoreFilePath = "capture{0}.png".format(str(ID))
    print(MyResult)
    with open(StoreFilePath, "wb") as File:
        File.write(MyResult)
        File.close()





print("1. Insert Image \n2.Read Image")
MenuInput = input()
if int (MenuInput) ==1:
    UserFilePath = input ("Enter File Path:")
    InsertBlob (UserFilePath)
elif int (MenuInput) ==2:
    UserIdChoice = input("Enter ID:")
    RetrieveBlob(UserIdChoice)