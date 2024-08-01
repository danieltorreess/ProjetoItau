# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(570, 416)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 59, 551, 171))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.inputArquivoPDF = QLineEdit(self.gridLayoutWidget)
        self.inputArquivoPDF.setObjectName(u"inputArquivoPDF")

        self.gridLayout.addWidget(self.inputArquivoPDF, 1, 1, 1, 1)

        self.arquivoPDF = QLabel(self.gridLayoutWidget)
        self.arquivoPDF.setObjectName(u"arquivoPDF")

        self.gridLayout.addWidget(self.arquivoPDF, 1, 0, 1, 1)

        self.salvarComoPDF = QLabel(self.gridLayoutWidget)
        self.salvarComoPDF.setObjectName(u"salvarComoPDF")

        self.gridLayout.addWidget(self.salvarComoPDF, 2, 0, 1, 1)

        self.inputSalvarComoPDF = QLineEdit(self.gridLayoutWidget)
        self.inputSalvarComoPDF.setObjectName(u"inputSalvarComoPDF")

        self.gridLayout.addWidget(self.inputSalvarComoPDF, 2, 1, 1, 1)

        self.buscarPDF = QToolButton(self.gridLayoutWidget)
        self.buscarPDF.setObjectName(u"buscarPDF")

        self.gridLayout.addWidget(self.buscarPDF, 1, 2, 1, 1)

        self.separarPDF = QPushButton(self.gridLayoutWidget)
        self.separarPDF.setObjectName(u"separarPDF")

        self.gridLayout.addWidget(self.separarPDF, 3, 1, 1, 1)

        self.buscarCaminhoPDF = QToolButton(self.gridLayoutWidget)
        self.buscarCaminhoPDF.setObjectName(u"buscarCaminhoPDF")

        self.gridLayout.addWidget(self.buscarCaminhoPDF, 2, 2, 1, 1)

        self.tituloPDF = QLabel(self.gridLayoutWidget)
        self.tituloPDF.setObjectName(u"tituloPDF")

        self.gridLayout.addWidget(self.tituloPDF, 0, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.arquivoPDF.setText(QCoreApplication.translate("Dialog", u"Arquivo PDF:", None))
        self.salvarComoPDF.setText(QCoreApplication.translate("Dialog", u"Salvar como:", None))
        self.buscarPDF.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.separarPDF.setText(QCoreApplication.translate("Dialog", u"Separar PDF", None))
        self.buscarCaminhoPDF.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.tituloPDF.setText(QCoreApplication.translate("Dialog", u"Separar PDF", None))
    # retranslateUi

