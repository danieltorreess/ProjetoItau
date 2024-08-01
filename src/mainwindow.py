import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from window import Ui_Dialog  # Importa a classe Ui_Dialog gerada do arquivo window.py
import fitz  # PyMuPDF

# Caminho do tema
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

        # Conecta os sinais de clique dos botões aos métodos correspondentes
        self.ui.buscarPDF.clicked.connect(self.open_file_dialog)
        self.ui.buscarCaminhoPDF.clicked.connect(self.open_directory_dialog)
        self.ui.separarPDF.clicked.connect(self.separate_pdf)  # Adiciona a conexão para o botão separarPDF

        # Setando valor nome do tema que será usado.
        themeFile = STR_THEME_PATH.replace('[THEME_NAME]', STR_THEME_NAME)

        # Setando estilo do tema.
        self.theme(themeFile)

    def open_file_dialog(self):
        # Cria uma instância do QFileDialog para seleção de arquivos
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles) # type: ignore
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        file_dialog.setViewMode(QFileDialog.List) # type: ignore

        if file_dialog.exec():
            # Obtém o caminho do arquivo selecionado
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Insere o caminho do arquivo na QLineEdit
                self.ui.inputArquivoPDF.setText(selected_files[0])

    def open_directory_dialog(self):
        # Cria uma instância do QFileDialog para seleção de diretórios
        directory_dialog = QFileDialog(self)
        directory_dialog.setFileMode(QFileDialog.Directory) # type: ignore
        # directory_dialog.setOption(QFileDialog.DontUseNativeDialog)  # Opcional, se preferir um diálogo Qt nativo
        directory_dialog.setViewMode(QFileDialog.List) # type: ignore 

        if directory_dialog.exec():
            # Obtém o caminho do diretório selecionado
            selected_directories = directory_dialog.selectedFiles()
            if selected_directories:
                # Insere o caminho do diretório na QLineEdit
                self.ui.inputSalvarComoPDF.setText(selected_directories[0])

    def separate_pdf(self):
        # Obtém o caminho do arquivo PDF e o diretório de destino
        pdf_path = self.ui.inputArquivoPDF.text()
        output_dir = self.ui.inputSalvarComoPDF.text()

        if not pdf_path or not output_dir:
            QMessageBox.warning(self, "Aviso", "Por favor, selecione o arquivo PDF e o diretório de destino.")
            return

        try:
            # Abre o arquivo PDF
            pdf_document = fitz.open(pdf_path)
            num_pages = pdf_document.page_count

            for page_num in range(num_pages):
                # Cria um novo documento PDF para cada página
                pdf_writer = fitz.open()
                page = pdf_document.load_page(page_num)
                pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

                # Define o nome do arquivo de saída com o formato desejado
                output_filename = f"{output_dir}/Comprovante_{page_num + 1}.pdf"
                pdf_writer.save(output_filename)
                pdf_writer.close()

            pdf_document.close()

            # Mensagem de sucesso
            QMessageBox.information(self, "Sucesso", "PDF separado com sucesso!")

            # Limpa os campos das QLineEdits
            self.ui.inputArquivoPDF.clear()
            self.ui.inputSalvarComoPDF.clear()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao separar o PDF: {e}")

    def theme(self, file):
        with open(file, 'r') as f:
            str_ = f.read()
        self.setStyleSheet(str_)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
