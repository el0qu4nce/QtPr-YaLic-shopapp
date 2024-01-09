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

    def open_closing(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ya_App()
    window.show()

    sys.exit(app.exec())
