import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QToolButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from window import Ui_Dialog  # Importa a classe Ui_Dialog gerada do arquivo window.py

# CAMINHO DO TEMA
STR_THEME_PATH = "J:\\Meu Drive\\ProjetoItau\\design\\theme.qss"

# Combinear, Darkeum, Fibers, Fibrary, Genetive, Wstartpage
STR_THEME_NAME = 'Combinear'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Instancia a classe Ui_Dialog
        self.ui.setupUi(self)  # Configura a UI

        # Define o tamanho fixo da janela
        self.setFixedSize(QSize(360, 120))  # Ajuste os valores conforme necessário
        
        # Define o título da janela
        self.setWindowTitle("Automação Itaú")
        
        # Define um ícone para a janela
        self.setWindowIcon(QIcon("J:\\Meu Drive\\ProjetoItau\\Fotos\\LogoItau.png"))  # Substitua pelo caminho do seu ícone

        # Configura o widget central
        self.setCentralWidget(self.ui.gridLayoutWidget)

        # Setando valor nome do tema que será usado.
        themeFile = STR_THEME_PATH.replace('[THEME_NAME]', STR_THEME_NAME)

        # Setando estilo do tema.
        self.theme(themeFile)

    def theme(self, file):
        with open(file, 'r') as f:
            str_ = f.read()
        self.setStyleSheet(str_)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
