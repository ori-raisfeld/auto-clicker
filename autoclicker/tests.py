from PyQt5 import QtWidgets
import sys
import help

class helpUI(help.Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton_2.clicked.connect(self.close)

class KeyGrabber(QtWidgets.QWidget):
    def __init__(self):
        try:
            super().__init__()
            layout = QtWidgets.QVBoxLayout(self)
            self.button = QtWidgets.QPushButton('start')
            layout.addWidget(self.button)
            self.button.setCheckable(True)
            self.button.toggled.connect(self.show_widget)
            self.help = helpUI()
        except Exception as error:
            print(error.__str__())

    def show_widget(self):
        try:
            self.help.show()
        except Exception as error:
            print(error.__str__())

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        grabber = KeyGrabber()
        grabber.show()
        sys.exit(app.exec_())
    except Exception as error:
        print(str(error))