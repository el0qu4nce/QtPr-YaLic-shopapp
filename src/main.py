import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets

from opening import Ui_Main_opening
from shop import Ui_Main_shop
from checkout import Ui_Main_checkout
from closing import Ui_Main_closing

class Ya_App(QMainWindow):
    def __init__(self):
        super(Ya_App, self).__init__()
        self.ui = Ui_Main_opening()
        self.ui.setupUi(self)
        self.ui.pushButton_start.clicked.connect(lambda: self.open_shop())
        self.ui_shop = Ui_Main_shop()

        self.ui_checkout = Ui_Main_checkout()

        self.ui_closing = Ui_Main_closing()

    def open_shop(self):
        # print('hello world')
        self.close()
        self.ui_shop.setupUi(self)
        self.show()
        self.ui_shop.pushButton.clicked.connect(lambda: self.open_checkout())
        self.ui_shop.pushButton_2.clicked.connect(lambda: self.open_checkout())
        self.ui_shop.pushButton_3.clicked.connect(lambda: self.open_checkout())
        self.ui_shop.pushButton_4.clicked.connect(lambda: self.open_checkout())
        self.ui_shop.pushButton_5.clicked.connect(lambda: self.open_checkout())
        self.ui_shop.pushButton_6.clicked.connect(lambda: self.open_checkout())

    def open_checkout(self):
        self.close()
        self.ui_checkout.setupUi(self)
        self.show()
        self.ui_checkout.pushButton.clicked.connect(lambda: self.open_closing())

    def open_closing(self): #problem with design
        self.close()

    #     self.close()
    #     self.ui_closing.setupUi(self)
    #     self.show()
    #     self.ui_shop
    #
    # def open_shop_1(self):
    #     self.ui_shop_1 = Ui_Main_shop()
    #     self.ui_shop_1.setupUi(self)
    #     self.show()
    #     print('task2')
    #     # self.ui.pushButton_start.clicked.connect(lambda: self.open_shop())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ya_App()
    window.show()

    sys.exit(app.exec())


# class Ya_shop(QMainWindow):
#     def __init__(self):
#         super(Ya_shop, self).__init__()
#         self.ui = Ui_Main_opening()
#         self.ui.setupUi(self)
#         self.Ui_Main_shop = Ui_Main_shop
#         self.Ui_Main_checkout = Ui_Main_checkout
#         self.Ui_Main_closing = Ui_Main_closing
#         # self.ui.pushButton.clicked.connect(self.open_shop())
#         self.ui.pushButton.clicked.connect(self.open_shop())
#         self.Ui_Main_shop = Ui_Main_shop
#         self.ui.pushButton.clicked.connect(self.open_checkout())
#         self.ui.pushButton.clicked.connect(self.open_closing())
#
#
#     def open_shop(self): #функция вызова диалогового окна
#         self.new_window = QtWidgets.QDialog()
#         self.Ui_Main_shop.setupUi(self, self.new_window)
#         self.new_window.show()
#         # print('Yes')
#
#     def open_checkout(self):
#         self.checkout_window = QtWidgets.QDialog()
#         self.Ui_Main_checkout.setupUi(self, self.checkout_window)
#         self.checkout_window.show()
#
#     def open_closing(self):
#         self.close_window = QtWidgets.QDialog()
#         self.Ui_Main_closing.setupUi(self, self.close_window)
#         self.close_window.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ya_shop()
#     window.show()
#
#     sys.exit(app.exec())
