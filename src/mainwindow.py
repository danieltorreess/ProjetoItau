# type: ignore
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
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
        self.setFixedSize(QSize(390, 220))  # Ajuste os valores conforme necessário

        # Define o título da janela
        self.setWindowTitle("Automação Itaú")

        # Define um ícone para a janela
        self.setWindowIcon(QIcon("J:\\Meu Drive\\ProjetoItau\\Fotos\\LogoItau.png"))  # Substitua pelo caminho do seu ícone

        # Conecta os sinais de clique dos botões aos métodos correspondentes
        self.ui.buscarPDF.clicked.connect(self.open_file_dialog)
        self.ui.buscarCaminhoPDF.clicked.connect(self.open_directory_dialog)
        self.ui.separarPDF.clicked.connect(self.separar_pdf)

        # Setando valor nome do tema que será usado.
        themeFile = STR_THEME_PATH.replace('[THEME_NAME]', STR_THEME_NAME)

        # Setando estilo do tema.
        self.theme(themeFile)

    def open_file_dialog(self):
        # Cria uma instância do QFileDialog para seleção de arquivos
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)  # Seleciona arquivos existentes
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec():
            # Obtém o caminho do arquivo selecionado
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Insere o caminho do arquivo na QLineEdit
                self.ui.inputArquivoPDF.setText(selected_files[0])

    def open_directory_dialog(self):
        # Cria uma instância do QFileDialog para seleção de diretórios
        directory_dialog = QFileDialog(self)
        directory_dialog.setFileMode(QFileDialog.Directory)  # Seleciona diretórios
        directory_dialog.setViewMode(QFileDialog.List)

        if directory_dialog.exec():
            # Obtém o caminho do diretório selecionado
            selected_directories = directory_dialog.selectedFiles()
            if selected_directories:
                # Insere o caminho do diretório na QLineEdit
                self.ui.inputSalvarComoPDF.setText(selected_directories[0])

    def separar_pdf(self):
        # Obtém os caminhos dos arquivos e diretórios
        pdf_path = self.ui.inputArquivoPDF.text()
        output_dir = self.ui.inputSalvarComoPDF.text()

        if not pdf_path or not output_dir:
            self.show_message("Erro", "Por favor, selecione um arquivo PDF e um diretório para salvar.")
            return

        from PyPDF2 import PdfReader, PdfWriter
        import os

        try:
            reader = PdfReader(pdf_path)
            num_pages = len(reader.pages)

            for page_num in range(num_pages):
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])
                output_file = os.path.join(output_dir, f"Comprovante_{page_num + 1}.pdf")

                with open(output_file, 'wb') as out_file:
                    writer.write(out_file)

            # Limpa os campos das LineEdits após o sucesso
            self.ui.inputArquivoPDF.clear()
            self.ui.inputSalvarComoPDF.clear()

            # Mostra mensagem de sucesso
            self.show_message("Sucesso", "O PDF foi separado com sucesso.")

        except Exception as e:
            # Mostra mensagem de erro
            self.show_message("Erro", f"Erro ao separar o PDF: {e}")

    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Information if title == "Sucesso" else QMessageBox.Critical)
        msg_box.exec()

    def theme(self, file):
        with open(file, 'r') as f:
            str_ = f.read()
        self.setStyleSheet(str_)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
