# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YaLic_opening.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import opening_res

class Ui_Main_opening(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(434, 469)
        MainWindow.setStyleSheet(u"background-color:rgba(235,223,7,200); \n"
"font-family:source-sans-pro;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(140, 370, 151, 51))
        self.pushButton_start.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 400, 71, 61))
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
        # icon = QIcon()
        # icon.addFile(u"Ya_Lic icons/github_240_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(50, 50))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 400, 121, 61))
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
        self.start = QFrame(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(90, 50, 261, 121))
        self.start.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-radius:7px;\n"
"font-size: 14pt;\n"
"font-weight:bold;\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.verticalLayout = QVBoxLayout(self.start)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.start)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"source-sans-pro"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 0);\n"
"")
        self.label.setScaledContents(False)
        self.label.setIndent(12)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.start)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 0);\n"
"border-radius: 8px;\n"
"font: 76 15pt \"Palatino Linotype\";")

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(130, 220, 181, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(14)
        self.textEdit_4.setFont(font1)
        self.textEdit_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgba(0,0,0,0);\n"
"border-radius: 8px;")
        # self.textEdit_4.setTabStopWidth(84)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ya.Licey ShopApp", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"Start shopping", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"   Yandex Licey", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Merchandise shop", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your name", None))
    # retranslateUi
