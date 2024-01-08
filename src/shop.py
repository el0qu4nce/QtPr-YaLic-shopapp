# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YaLic_shop.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QLCDNumber,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import shop_res

class Ui_Main_shop(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(673, 513)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgba(235,223,7,255); \n"
"font-family:source-sans-pro;")
        # MainWindow.setSizeGripEnabled(False)
        # MainWindow.setModal(False)
        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 60, 591, 411))
        self.frame.setMouseTracking(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 60, 141, 151))
        self.frame_2.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 110, 101, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;\n"
"width:230px;\n"
"height:50px;\n"
"font: 9pt \"MS Reference Sans Serif\";\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(194, 167,10,80);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgba(182, 156, 10,100);\n"
"text=in cart}")
        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 10, 121, 91))
        icon = QIcon()
        icon.addFile(u"Ya_Lic icons/tshirt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(75, 75))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(230, 60, 141, 151))
        self.frame_3.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 110, 101, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;\n"
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
        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 10, 121, 81))
        icon1 = QIcon()
        icon1.addFile(u"Ya_Lic icons/hood.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QSize(75, 75))
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(400, 60, 141, 151))
        self.frame_4.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 110, 101, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;\n"
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
        self.pushButton_9 = QPushButton(self.frame_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 10, 121, 81))
        icon2 = QIcon()
        icon2.addFile(u"Ya_Lic icons/cotton-polo-shirt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(75, 75))
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(60, 240, 141, 151))
        self.frame_5.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 110, 101, 31))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;\n"
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
        self.pushButton_10 = QPushButton(self.frame_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 10, 121, 81))
        icon3 = QIcon()
        icon3.addFile(u"Ya_Lic icons/backpack.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QSize(75, 75))
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(230, 240, 141, 151))
        self.frame_6.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 110, 101, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;\n"
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
        self.pushButton_11 = QPushButton(self.frame_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(10, 10, 121, 81))
        icon4 = QIcon()
        icon4.addFile(u"Ya_Lic icons/winter-hat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QSize(75, 75))
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(400, 240, 141, 151))
        self.frame_7.setStyleSheet(u"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 110, 101, 31))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;\n"
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
        self.pushButton_12 = QPushButton(self.frame_7)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(10, 10, 121, 81))
        icon5 = QIcon()
        icon5.addFile(u"Ya_Lic icons/cap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(75, 75))
        self.frame_8 = QFrame(MainWindow)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(440, 20, 231, 41))
        self.frame_8.setStyleSheet(u"background-color:rgba(235,223,7,0); ")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 113, 22))
        self.lineEdit.setStyleSheet(u"color: black;\n"
"font: 9pt \"MS Reference Sans Serif\";\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.lcdNumber = QLCDNumber(self.frame_8)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(130, 0, 71, 31))
        self.lcdNumber.setStyleSheet(u"color: black;\n"
"background-color:rgba(194, 167,10,60);\n"
"border: 3px solid rgba(158, 136, 7, 80);\n"
"border-radius: 8px;")
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"buy", None))
        self.pushButton_7.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"buy", None))
        self.pushButton_8.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"buy", None))
        self.pushButton_9.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"buy", None))
        self.pushButton_10.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"buy", None))
        self.pushButton_11.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"buy", None))
        self.pushButton_12.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"In Cart:", None))
    # retranslateUi

