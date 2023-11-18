# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YaLic_checkout.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Main_checkout(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(416, 391)
        Dialog.setStyleSheet(u"background-color:rgba(235,223,7,255); \n"
"font-family:source-sans-pro;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 371, 371))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 231, 43))
        font = QFont()
        font.setFamilies([u"source-sans-pro"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 0);\n"
"")
        self.label.setScaledContents(False)
        self.label.setIndent(12)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 120, 271, 61))
        self.lineEdit.setStyleSheet(u"color: black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 210, 91, 51))
        self.lineEdit_2.setStyleSheet(u"color: black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 10px;")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(200, 210, 71, 51))
        self.lineEdit_3.setStyleSheet(u"color: black;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 10px;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 233, 43))
        self.label_3.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 0);\n"
"border-radius: 8px;\n"
"font: 76 15pt \"Palatino Linotype\";")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 300, 131, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 12px;\n"
"width:230px;\n"
"height:50px;\n"
"font: 9pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(194, 167,10,80);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgba(194, 167,10,100);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Check out:", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"0000 0000 0000 0000", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"YY/MM", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"CVC", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Fill the card data - ", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Check out", None))
    # retranslateUi

