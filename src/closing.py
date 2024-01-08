# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YaLic_closing.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import closing_res

class Ui_Main_closing(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 306)
        Dialog.setStyleSheet(u"background-color:rgba(235,223,7,255); \n"
"font-family:source-sans-pro;")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 220, 71, 61))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,10);\n"
"border: 3px solid rgba(194, 167,10,10);\n"
"border-radius: 1px;\n"
"width:230px;\n"
"height:50px;\n"
"font: 9pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(194, 167,10,10);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgba(194, 167,10,10);\n"
"}")
        icon = QIcon()
        icon.addFile(u"Ya_Lic icons/github_240_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(50, 50))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(270, 230, 121, 41))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,10);\n"
"border: 3px solid rgba(194, 167,10,10);\n"
"border-radius: 1px;\n"
"width:230px;\n"
"height:50px;\n"
"font: 9pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(194, 167,10,10);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgba(194, 167,10,10);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Ya_Lic icons/lyceum_logo_b64692c23b.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(100, 40))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 220, 51, 51))
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:rgba(194, 167,10,10);\n"
"border: 3px solid rgba(194, 167,10,10);\n"
"border-radius: 1px;\n"
"width:230px;\n"
"height:50px;\n"
"font: 15pt \"MS Reference Sans Serif\";\n"
"\n"
"")
        self.label.setScaledContents(False)
        self.label.setIndent(12)
        self.start = QFrame(Dialog)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(70, 10, 261, 121))
        self.start.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-radius:7px;\n"
"font-size: 14pt;\n"
"font-weight:bold;\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.verticalLayout = QVBoxLayout(self.start)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.start)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"source-sans-pro"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 0);\n"
"")
        self.label_2.setScaledContents(False)
        self.label_2.setIndent(12)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.start)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 0);\n"
"border-radius: 8px;\n"
"font: 76 15pt \"Palatino Linotype\";")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 140, 261, 43))
        self.label_4.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 0);\n"
"border-radius: 8px;\n"
"font: 76 12pt \"Palatino Linotype\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u00d7", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"   Yandex Licey", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Merchandise shop", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Thanks for your purchase!", None))
    # retranslateUi

