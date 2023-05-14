import sys
from PySide6.QtWidgets import *

import pycep_correios

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela2")
        self.label_titulo =QLabel("Correios")

        fonte=self.label_titulo.font()
        fonte.setPointSize(18)
        self.label_titulo.setFont(fonte)

        self.input_nome=QLineEdit()
        self.input_nome.setPlaceholderText("Digite seu Nome")

        self.input_fone=QLineEdit()
        self.input_fone.setPlaceholderText("Digite seu Telefone")

        self.input_CEP=QLineEdit()
        self.input_CEP.setPlaceholderText("Digite seu CEP")

        self.input_Rua=QLineEdit()
        self.input_Rua.setPlaceholderText("Digite sua Rua")

        self.input_Bairro=QLineEdit()
        self.input_Bairro.setPlaceholderText("Digite seu Bairro")

        self.input_Cidade=QLineEdit()
        self.input_Cidade.setPlaceholderText("Digite seu Cidade")
        
        self.input_Estado=QLineEdit()
        self.input_Estado.setPlaceholderText("Digite seu Estado")

        self.btn_enviar=QPushButton("Enviar")

        layout=QVBoxLayout()

        layout.addWidget(self.label_titulo)

        

        
        layout.addWidget(self.input_nome)
        layout.addWidget(self.input_fone)
        layout.addWidget(self.input_CEP)
        layout.addWidget(self.input_Rua)
        layout.addWidget(self.input_Bairro)
        layout.addWidget(self.input_Cidade)
        layout.addWidget(self.input_Estado) 
        
        layout.addWidget(self.btn_enviar)

        container=QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.input_CEP.editingFinished.connect(self.printer)





    def printer(self):
        endereco= pycep_correios.get_address_from_cep(self.input_CEP.text())
        print(endereco)
        
        self.input_Estado.setText(endereco['uf'])
        self.input_Cidade.setText(endereco['cidade'])
        self.input_Bairro.setText(endereco['bairro'])
        self.input_CEP.setText(endereco['cep'])


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = JanelaPrincipal()
window.show()
app.exec_()
