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
        Dialog.resize(392, 591)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 70, 371, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.inputArquivoPDF = QLineEdit(self.gridLayoutWidget)
        self.inputArquivoPDF.setObjectName(u"inputArquivoPDF")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.inputArquivoPDF.setFont(font)

        self.gridLayout.addWidget(self.inputArquivoPDF, 1, 1, 1, 1)

        self.arquivoPDF = QLabel(self.gridLayoutWidget)
        self.arquivoPDF.setObjectName(u"arquivoPDF")
        self.arquivoPDF.setFont(font)

        self.gridLayout.addWidget(self.arquivoPDF, 1, 0, 1, 1)

        self.salvarComoPDF = QLabel(self.gridLayoutWidget)
        self.salvarComoPDF.setObjectName(u"salvarComoPDF")
        self.salvarComoPDF.setFont(font)

        self.gridLayout.addWidget(self.salvarComoPDF, 2, 0, 1, 1)

        self.inputSalvarComoPDF = QLineEdit(self.gridLayoutWidget)
        self.inputSalvarComoPDF.setObjectName(u"inputSalvarComoPDF")
        self.inputSalvarComoPDF.setFont(font)

        self.gridLayout.addWidget(self.inputSalvarComoPDF, 2, 1, 1, 1)

        self.buscarPDF = QToolButton(self.gridLayoutWidget)
        self.buscarPDF.setObjectName(u"buscarPDF")
        self.buscarPDF.setFont(font)

        self.gridLayout.addWidget(self.buscarPDF, 1, 2, 1, 1)

        self.separarPDF = QPushButton(self.gridLayoutWidget)
        self.separarPDF.setObjectName(u"separarPDF")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.separarPDF.setFont(font1)

        self.gridLayout.addWidget(self.separarPDF, 3, 1, 1, 1)

        self.buscarCaminhoPDF = QToolButton(self.gridLayoutWidget)
        self.buscarCaminhoPDF.setObjectName(u"buscarCaminhoPDF")
        self.buscarCaminhoPDF.setFont(font)

        self.gridLayout.addWidget(self.buscarCaminhoPDF, 2, 2, 1, 1)

        self.tituloPDF = QLabel(self.gridLayoutWidget)
        self.tituloPDF.setObjectName(u"tituloPDF")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.tituloPDF.setFont(font2)
        self.tituloPDF.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.tituloPDF, 0, 0, 1, 3)

        self.TituloPrincipal = QLabel(Dialog)
        self.TituloPrincipal.setObjectName(u"TituloPrincipal")
        self.TituloPrincipal.setGeometry(QRect(50, 10, 281, 51))
        self.TituloPrincipal.setFont(font2)
        self.TituloPrincipal.setAlignment(Qt.AlignCenter)
        self.LogoItau = QLabel(Dialog)
        self.LogoItau.setObjectName(u"LogoItau")
        self.LogoItau.setGeometry(QRect(10, 18, 41, 41))
        self.LogoItau.setPixmap(QPixmap(u"../Fotos/LogoItau.png"))
        self.LogoItau.setScaledContents(True)
        self.LogoMV = QLabel(Dialog)
        self.LogoMV.setObjectName(u"LogoMV")
        self.LogoMV.setGeometry(QRect(330, 20, 51, 41))
        self.LogoMV.setPixmap(QPixmap(u"../Fotos/LogoMV.png"))
        self.LogoMV.setScaledContents(True)
        self.gridLayoutWidget_2 = QWidget(Dialog)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 230, 371, 141))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.inputArquivoExcel = QLineEdit(self.gridLayoutWidget_2)
        self.inputArquivoExcel.setObjectName(u"inputArquivoExcel")
        self.inputArquivoExcel.setFont(font)

        self.gridLayout_2.addWidget(self.inputArquivoExcel, 1, 1, 1, 1)

        self.arquivoExcel = QLabel(self.gridLayoutWidget_2)
        self.arquivoExcel.setObjectName(u"arquivoExcel")
        self.arquivoExcel.setFont(font)

        self.gridLayout_2.addWidget(self.arquivoExcel, 1, 0, 1, 1)

        self.salvarComoExcel = QLabel(self.gridLayoutWidget_2)
        self.salvarComoExcel.setObjectName(u"salvarComoExcel")
        self.salvarComoExcel.setFont(font)

        self.gridLayout_2.addWidget(self.salvarComoExcel, 2, 0, 1, 1)

        self.inputSalvarComoExcel = QLineEdit(self.gridLayoutWidget_2)
        self.inputSalvarComoExcel.setObjectName(u"inputSalvarComoExcel")
        self.inputSalvarComoExcel.setFont(font)

        self.gridLayout_2.addWidget(self.inputSalvarComoExcel, 2, 1, 1, 1)

        self.buscarExcel = QToolButton(self.gridLayoutWidget_2)
        self.buscarExcel.setObjectName(u"buscarExcel")
        self.buscarExcel.setFont(font)

        self.gridLayout_2.addWidget(self.buscarExcel, 1, 2, 1, 1)

        self.ConfigurarExcel = QPushButton(self.gridLayoutWidget_2)
        self.ConfigurarExcel.setObjectName(u"ConfigurarExcel")
        self.ConfigurarExcel.setFont(font1)

        self.gridLayout_2.addWidget(self.ConfigurarExcel, 3, 1, 1, 1)

        self.buscarCaminhoExcel = QToolButton(self.gridLayoutWidget_2)
        self.buscarCaminhoExcel.setObjectName(u"buscarCaminhoExcel")
        self.buscarCaminhoExcel.setFont(font)

        self.gridLayout_2.addWidget(self.buscarCaminhoExcel, 2, 2, 1, 1)

        self.tituloExcel = QLabel(self.gridLayoutWidget_2)
        self.tituloExcel.setObjectName(u"tituloExcel")
        self.tituloExcel.setFont(font2)
        self.tituloExcel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.tituloExcel, 0, 0, 1, 3)


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
        self.TituloPrincipal.setText(QCoreApplication.translate("Dialog", u"Automa\u00e7\u00e3o comprovantes Ita\u00fa", None))
        self.LogoItau.setText("")
        self.LogoMV.setText("")
        self.arquivoExcel.setText(QCoreApplication.translate("Dialog", u"Arquivo Excel:", None))
        self.salvarComoExcel.setText(QCoreApplication.translate("Dialog", u"Salvar como:", None))
        self.buscarExcel.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.ConfigurarExcel.setText(QCoreApplication.translate("Dialog", u"Configurar Excel", None))
        self.buscarCaminhoExcel.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.tituloExcel.setText(QCoreApplication.translate("Dialog", u"Configurar arquivo Excel", None))
    # retranslateUi

