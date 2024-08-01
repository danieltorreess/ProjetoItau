# type: ignore
from PySide6.QtWidgets import QFileDialog

def open_file_dialog(self, file_filter, line_edit):
    file_dialog = QFileDialog(self)
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    file_dialog.setNameFilter(file_filter)
    file_dialog.setViewMode(QFileDialog.List)

    if file_dialog.exec():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            line_edit.setText(selected_files[0])

def open_directory_dialog(self, line_edit):
    directory = QFileDialog.getExistingDirectory(self, "Selecione o diretório")

    if directory:
        line_edit.setText(directory)
