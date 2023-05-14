import sys
from PySide6.QtWidgets import *


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela")
        self.label_titulo =QLabel("app")




       
        self.label_comp=QLabel("Insira o Comprimento")
        self.input_comp=QLineEdit()
       
        self.label_altura=QLabel("Insira a Largura")
        self.input_altura=QLineEdit()

        self.input_largura=QLineEdit()
        self.label_largura=QLabel("Insira a Altura")

        self.btn_calcular=QPushButton("Calcular")
        self.result_calculo=QLabel()


        layout=QVBoxLayout()

        layout.addWidget(self.label_titulo)
        
        layout.addWidget(self.label_comp)
        layout.addWidget(self.input_comp)

        layout.addWidget(self.label_altura)
        layout.addWidget(self.input_altura)

        layout.addWidget(self.label_largura)
        layout.addWidget(self.input_largura)

        layout.addWidget(self.btn_calcular)
        layout.addWidget(self.result_calculo)
        



        container=QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.btn_calcular.clicked.connect(self.calc)




    def calc(self):
        Comprimento=float(self.input_comp.text())
        Largura=float(self.input_largura.text())
        Altura=float(self.input_altura.text())

        result=Comprimento*Largura*Altura
        self.result_calculo.setText(str(result))



app = QApplication(sys.argv)
app.setStyle('Fusion')
window = JanelaPrincipal()
window.show()
app.exec_()
