# type: ignore
import os
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from window import Ui_Dialog  # Importa a classe Ui_Dialog gerada do arquivo window.py
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from utils import show_message, theme

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Instancia a classe Ui_Dialog
        self.ui.setupUi(self)  # Configura a UI

        # Define o tamanho fixo da janela
        self.setFixedSize(QSize(390, 550))  # Ajuste os valores conforme necessário

        # Define o título da janela
        self.setWindowTitle("Automação Itaú")

        # Define um ícone para a janela
        self.setWindowIcon(QIcon("J:\\Meu Drive\\ProjetoItau\\Fotos\\LogoItau.png"))  # Substitua pelo caminho do seu ícone

        # Conecta os sinais de clique dos botões aos métodos correspondentes
        self.ui.buscarPDF.clicked.connect(self.open_file_dialog)
        self.ui.buscarCaminhoPDF.clicked.connect(self.open_directory_dialog)
        self.ui.separarPDF.clicked.connect(self.separar_pdf)
        
        # Conecta os botões para configurar Excel
        self.ui.buscarExcel.clicked.connect(self.open_excel_file_dialog)
        self.ui.buscarCaminhoExcel.clicked.connect(self.save_excel_file_dialog)
        self.ui.ConfigurarExcel.clicked.connect(self.configurar_excel)

        # Conecta os botões para renomeação de PDFs
        self.ui.buscarPastaPDF.clicked.connect(self.open_folder_dialog)
        self.ui.buscarArquivoExcel.clicked.connect(self.open_renaming_excel_file_dialog)
        self.ui.RenomearPDF.clicked.connect(self.renomear_pdfs)

        # Setando valor nome do tema que será usado.
        STR_THEME_PATH = "J:\\Meu Drive\\ProjetoItau\\design\\theme.qss"
        STR_THEME_NAME = 'Combinear'
        theme_file = STR_THEME_PATH.replace('[THEME_NAME]', STR_THEME_NAME)

        # Setando estilo do tema.
        theme(self, theme_file)

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
        # Abre o diálogo de seleção de diretórios
        directory = QFileDialog.getExistingDirectory(self, "Selecione o diretório para salvar")

        if directory:
            # Insere o caminho do diretório na QLineEdit
            self.ui.inputSalvarComoPDF.setText(directory)

    def separar_pdf(self):
        # Obtém os caminhos dos arquivos e diretórios
        pdf_path = self.ui.inputArquivoPDF.text()
        output_dir = self.ui.inputSalvarComoPDF.text()

        if not pdf_path or not output_dir:
            show_message(self, "Erro", "Por favor, selecione um arquivo PDF e um diretório para salvar.")
            return

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
            show_message(self, "Sucesso", "O PDF foi separado com sucesso.")

        except Exception as e:
            # Mostra mensagem de erro
            show_message(self, "Erro", f"Erro ao separar o PDF: {e}")

    def open_excel_file_dialog(self):
        # Cria uma instância do QFileDialog para seleção de arquivos
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)  # Seleciona arquivos existentes
        file_dialog.setNameFilter("Excel Files (*.xlsx *.xls)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec():
            # Obtém o caminho do arquivo selecionado
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Insere o caminho do arquivo na QLineEdit
                self.ui.inputArquivoExcel.setText(selected_files[0])

    def save_excel_file_dialog(self):
        # Cria uma instância do QFileDialog para salvar arquivos
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)  # Seleciona qualquer arquivo
        file_dialog.setNameFilter("Excel Files (*.xlsx *.xls)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setDefaultSuffix('xlsx')

        if file_dialog.exec():
            # Obtém o caminho do arquivo selecionado
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Insere o caminho do arquivo na QLineEdit
                self.ui.inputSalvarComoExcel.setText(selected_files[0])

    def configurar_excel(self):
        excel_path = self.ui.inputArquivoExcel.text()
        save_path = self.ui.inputSalvarComoExcel.text()

        if not excel_path or not save_path:
            show_message(self, "Erro", "Por favor, selecione um arquivo Excel e um caminho para salvar.")
            return

        try:
            # Abrir o arquivo Excel
            excel_data = pd.read_excel(excel_path, sheet_name='Relatório', header=10)

            # Manter apenas as colunas necessárias e renomeá-las
            cols_to_keep = ['Credor', 'Lançamento', 'Líquido']
            excel_data = excel_data[cols_to_keep]
            excel_data.columns = ['Credor', 'Lancamento', 'Liquido']

            # Remover valores vazios da coluna 'Lancamento'
            excel_data = excel_data.dropna(subset=['Lancamento'])

            # Manter apenas os primeiros 6 dígitos na coluna 'Lancamento'
            excel_data['Lancamento'] = excel_data['Lancamento'].astype(str).str[:6]

            # Ordenar a tabela pela coluna 'Liquido' do maior para o menor
            excel_data = excel_data.sort_values(by='Liquido', ascending=False)

            # Salvar o arquivo Excel modificado com um novo nome no caminho especificado
            save_dir = os.path.dirname(save_path)
            save_filename = os.path.basename(save_path)
            save_filename = save_filename if save_filename.endswith('.xlsx') else save_filename + '.xlsx'
            new_save_path = os.path.join(save_dir, save_filename)
            excel_data.to_excel(new_save_path, index=False)

            # Limpar os campos das LineEdits após o sucesso
            self.ui.inputArquivoExcel.clear()
            self.ui.inputSalvarComoExcel.clear()

            # Mostrar mensagem de sucesso
            show_message(self, "Sucesso", f"O arquivo Excel foi configurado com sucesso e salvo em: {new_save_path}")

        except Exception as e:
            show_message(self, "Erro", f"Erro ao configurar o Excel: {e}")

    def open_folder_dialog(self):
        # Abre o diálogo de seleção de diretórios
        directory = QFileDialog.getExistingDirectory(self, "Selecione a pasta de PDFs")

        if directory:
            # Insere o caminho da pasta na QLineEdit
            self.ui.inputPastaPDF.setText(directory)

    def open_renaming_excel_file_dialog(self):
        # Cria uma instância do QFileDialog para seleção de arquivos
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Excel Files (*.xlsx *.xls)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Insere o caminho do arquivo Excel na QLineEdit
                self.ui.inputExcelRenomear.setText(selected_files[0])

    def renomear_pdfs(self):
        # Obter os caminhos dos arquivos e diretórios
        pasta_pdfs = self.ui.inputPastaPDF.text()
        excel_path = self.ui.inputExcelRenomear.text()

        if not pasta_pdfs or not excel_path:
            show_message(self, "Erro", "Por favor, selecione a pasta com os PDFs e o arquivo Excel.")
            return

        try:
            # Ler o arquivo Excel
            df = pd.read_excel(excel_path, usecols=['Credor'])

            # Obter a lista de arquivos PDF na pasta
            pdf_files = [f for f in os.listdir(pasta_pdfs) if f.lower().endswith('.pdf')]

            # Obter os valores da coluna "Credor"
            credores = df['Credor'].dropna().tolist()

            if not pdf_files:
                show_message(self, "Erro", "Nenhum arquivo PDF encontrado na pasta especificada.")
                return

            if not credores:
                show_message(self, "Erro", "Nenhum valor encontrado na coluna 'Credor'.")
                return

            # Renomear os arquivos PDF
            for i, pdf_file in enumerate(pdf_files):
                if i < len(credores):
                    # Separar o nome e a extensão do arquivo
                    base, ext = os.path.splitext(pdf_file)
                    
                    # Manter o sufixo numérico
                    sufixo = base.split('_')[-1] if '_' in base else ''
                    
                    novo_nome = f"{credores[i]}{sufixo}{ext}"
                    caminho_antigo = os.path.join(pasta_pdfs, pdf_file)
                    caminho_novo = os.path.join(pasta_pdfs, novo_nome)
                    os.rename(caminho_antigo, caminho_novo)
                else:
                    break

            # Mostrar mensagem de sucesso
            show_message(self, "Sucesso", "Os arquivos PDF foram renomeados com sucesso.")

        except Exception as e:
            # Mostrar mensagem de erro
            show_message(self, "Erro", f"Erro ao renomear os PDFs: {e}")
