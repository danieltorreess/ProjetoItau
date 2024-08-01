from PySide6.QtWidgets import QMessageBox

def show_message(parent, title, message):
    msg_box = QMessageBox(parent)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()

def theme(window, theme_path):
    with open(theme_path, "r") as f:
        style = f.read()
        window.setStyleSheet(style)
