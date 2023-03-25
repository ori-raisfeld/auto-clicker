from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget

import pyautogui
from datetime import datetime
import keyboard
import help
import message_sender
global key

class helpUI(help.Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton_2.clicked.connect(self.close)
        self.send.clicked.connect(self.send_message)
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        MainWindow.show()
    def send_message(self):
        message_sender.send_message(self.name_input.text(), self.issue_input.toPlainText(), self.email_input.text())
        self.close()

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        try:
            self.delta_time = QTimer()
            pyautogui.FAILSAFE = False
            self.show_time = lambda: float(datetime.now().strftime('%S.%f')[:-5]) + float(datetime.now().strftime('%M')) + float(datetime.now().strftime('%H'))
            self.helpUI = helpUI()
            MainWindow.setObjectName("Auto clicker")
            MainWindow.resize(581, 506)
            MainWindow.setFixedSize(581, 506)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.stop = QtWidgets.QPushButton(self.centralwidget)
            self.stop.setGeometry(QtCore.QRect(340, 390, 121, 41))
            self.stop.setObjectName("stop")
            self.start = QtWidgets.QPushButton(self.centralwidget)
            self.start.setGeometry(QtCore.QRect(70, 390, 121, 41))
            self.start.setObjectName("start")
            self.general = QtWidgets.QGroupBox(self.centralwidget)
            self.general.setGeometry(QtCore.QRect(0, 0, 581, 181))
            self.general.setObjectName("general")
            self.repeation = QtWidgets.QGroupBox(self.general)
            self.repeation.setGeometry(QtCore.QRect(270, 100, 311, 71))
            self.repeation.setAutoFillBackground(True)
            self.repeation.setTitle("")
            self.repeation.setObjectName("repeation")
            self.repeat_forever = QtWidgets.QRadioButton(self.repeation)
            self.repeat_forever.setGeometry(QtCore.QRect(10, 10, 91, 17))
            self.repeat_forever.setObjectName("repeat_forever")
            self.repeat_how_many = QtWidgets.QRadioButton(self.repeation)
            self.repeat_how_many.setGeometry(QtCore.QRect(10, 40, 91, 17))
            self.repeat_how_many.setObjectName("repeat_how_many")
            self.repeation_input = QtWidgets.QSpinBox(self.repeation)
            self.repeation_input.setGeometry(QtCore.QRect(70, 40, 61, 16))
            self.repeation_input.setObjectName("repeation_input")
            self.times_label = QtWidgets.QLabel(self.repeation)
            self.times_label.setGeometry(QtCore.QRect(140, 40, 47, 13))
            self.times_label.setObjectName("times_label")
            self.intervals = QtWidgets.QGroupBox(self.general)
            self.intervals.setGeometry(QtCore.QRect(0, 30, 581, 71))
            self.intervals.setObjectName("intervals")
            self.minutes_box = QtWidgets.QSpinBox(self.intervals)
            self.minutes_box.setGeometry(QtCore.QRect(20, 40, 61, 22))
            self.minutes_box.setObjectName("minutes_box")
            self.minutes_label = QtWidgets.QLabel(self.intervals)
            self.minutes_label.setGeometry(QtCore.QRect(20, 20, 47, 13))
            self.minutes_label.setObjectName("minutes_label")
            self.seconds_box = QtWidgets.QSpinBox(self.intervals)
            self.seconds_box.setGeometry(QtCore.QRect(260, 40, 61, 22))
            self.seconds_box.setObjectName("seconds_box")
            self.seconds_label = QtWidgets.QLabel(self.intervals)
            self.seconds_label.setGeometry(QtCore.QRect(260, 20, 47, 13))
            self.seconds_label.setObjectName("seconds_label")
            self.milliseconds_box = QtWidgets.QSpinBox(self.intervals)
            self.milliseconds_box.setGeometry(QtCore.QRect(510, 40, 61, 22))
            self.milliseconds_box.setObjectName("milliseconds_box")
            self.milliseconds_label = QtWidgets.QLabel(self.intervals)
            self.milliseconds_label.setGeometry(QtCore.QRect(510, 20, 61, 16))
            self.milliseconds_label.setObjectName("milliseconds_label")
            self.keyboard_settings = QtWidgets.QGroupBox(self.general)
            self.keyboard_settings.setGeometry(QtCore.QRect(20, 100, 241, 71))
            self.keyboard_settings.setTitle("")
            self.keyboard_settings.setObjectName("keyboard_settings")
            self.keyboard_input = QtWidgets.QTextEdit(self.keyboard_settings)
            self.keyboard_input.setGeometry(QtCore.QRect(0, 30, 241, 31))
            self.keyboard_input.setObjectName("keyboard_input")
            self.keyboard_input_label = QtWidgets.QLabel(self.keyboard_settings)
            self.keyboard_input_label.setGeometry(QtCore.QRect(0, 10, 101, 16))
            self.keyboard_input_label.setObjectName("keyboard_input_label")
            self.hotkeys = QtWidgets.QGroupBox(self.centralwidget)
            self.hotkeys.setGeometry(QtCore.QRect(0, 174, 581, 109))
            self.hotkeys.setObjectName("hotkeys")
            self.start_input_label = QtWidgets.QLabel(self.hotkeys)
            self.start_input_label.setGeometry(QtCore.QRect(20, 20, 101, 16))
            self.start_input_label.setObjectName("start_input_label")
            self.start_input = QtWidgets.QLineEdit(self.hotkeys)
            self.start_input.setGeometry(QtCore.QRect(20, 40, 91, 21))
            self.start_input.setObjectName("start_input")
            self.stop_input_label = QtWidgets.QLabel(self.hotkeys)
            self.stop_input_label.setGeometry(QtCore.QRect(140, 20, 101, 16))
            self.stop_input_label.setObjectName("stop_input_label")
            self.stop_input = QtWidgets.QLineEdit(self.hotkeys)
            self.stop_input.setGeometry(QtCore.QRect(140, 40, 91, 21))
            self.stop_input.setObjectName("stop_input")
            self.line = QtWidgets.QFrame(self.hotkeys)
            self.line.setGeometry(QtCore.QRect(110, 6, 31, 101))
            self.line.setFrameShape(QtWidgets.QFrame.VLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.save = QtWidgets.QPushButton(self.hotkeys)
            self.save.setGeometry(QtCore.QRect(240, 10, 75, 23))
            self.save.setObjectName("save")
            self.clear = QtWidgets.QPushButton(self.hotkeys)
            self.clear.setGeometry(QtCore.QRect(240, 60, 75, 23))
            self.clear.setObjectName("clear")
            self.options = QtWidgets.QComboBox(self.centralwidget)
            self.options.setGeometry(QtCore.QRect(210, 290, 121, 41))
            self.options.setObjectName("options")
            self.options.addItem("")
            self.options.addItem("")
            self.options.addItem("")
            self.options.addItem("")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)
            self.help = QtWidgets.QPushButton(self.centralwidget)
            self.help.setGeometry(QtCore.QRect(490, 10, 91, 21))
            self.help.setObjectName("help")

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
        except Exception as error:
            print(error.__str__())

    def retranslateUi(self, MainWindow):
        try:
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.stop.setText(_translate("MainWindow", "stop"))
            self.start.setText(_translate("MainWindow", "start"))
            self.general.setTitle(_translate("MainWindow", "auto clicker | auto button presser"))
            self.repeat_forever.setText(_translate("MainWindow", "repeat forever"))
            self.repeat_how_many.setText(_translate("MainWindow", "repeat"))
            self.times_label.setText(_translate("MainWindow", "times"))
            self.intervals.setTitle(_translate("MainWindow", "click intervals"))
            self.minutes_label.setText(_translate("MainWindow", "minutes"))
            self.seconds_label.setText(_translate("MainWindow", "seconds"))
            self.milliseconds_label.setText(_translate("MainWindow", "milliseconds"))
            self.keyboard_input_label.setText(_translate("MainWindow", "keyboard presses"))
            self.hotkeys.setTitle(_translate("MainWindow", "hotkey settings"))
            self.start_input_label.setText(_translate("MainWindow", "start"))
            self.stop_input_label.setText(_translate("MainWindow", "stop"))
            self.save.setText(_translate("MainWindow", "save"))
            self.clear.setText(_translate("MainWindow", "clear hotkeys"))
            self.options.setItemText(0, _translate("MainWindow", "keyboard"))
            self.options.setItemText(1, _translate("MainWindow", "left click"))
            self.options.setItemText(2, _translate("MainWindow", "right click"))
            self.options.setItemText(3, _translate("MainWindow", "middle click"))
            self.note_label = QtWidgets.QLabel(self.hotkeys)
            self.note_label.setGeometry(QtCore.QRect(380, 0, 161, 39))
            self.note_label.setObjectName("note_label")
            self.other_option_start = QtWidgets.QComboBox(self.hotkeys)
            self.other_option_start.setGeometry(QtCore.QRect(380, 60, 71, 21))
            self.other_option_start.setObjectName("other_option_start")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.other_option_start.addItem("")
            self.accept_other = QtWidgets.QCheckBox(self.hotkeys)
            self.accept_other.setGeometry(QtCore.QRect(370, 80, 181, 31))
            self.accept_other.setObjectName("accept_other")
            self.line_2 = QtWidgets.QFrame(self.hotkeys)
            self.line_2.setGeometry(QtCore.QRect(450, 40, 16, 51))
            self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")
            self.help.setText(_translate("MainWindow", "help"))
            self.other_option_2 = QtWidgets.QComboBox(self.hotkeys)
            self.other_option_2.setGeometry(QtCore.QRect(460, 60, 71, 21))
            self.other_option_2.setObjectName("other_option_2")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.other_option_2.addItem("")
            self.start_other = QtWidgets.QLabel(self.hotkeys)
            self.start_other.setGeometry(QtCore.QRect(380, 40, 47, 13))
            self.start_other.setObjectName("start_other")
            self.stop_other = QtWidgets.QLabel(self.hotkeys)
            self.stop_other.setGeometry(QtCore.QRect(460, 40, 47, 13))
            self.stop_other.setObjectName("stop_other")
            self.note_label.setText(_translate("MainWindow", "(if you can\'t write the \n"
                                                             " hotkey you want, use this)"))
            self.other_option_start.setItemText(0, _translate("MainWindow", "tab"))
            self.other_option_start.setItemText(1, _translate("MainWindow", "enter"))
            self.other_option_start.setItemText(2, _translate("MainWindow", "space"))
            self.other_option_start.setItemText(3, _translate("MainWindow", "a"))
            self.other_option_start.setItemText(4, _translate("MainWindow", "b"))
            self.other_option_start.setItemText(5, _translate("MainWindow", "c"))
            self.other_option_start.setItemText(6, _translate("MainWindow", "d"))
            self.other_option_start.setItemText(7, _translate("MainWindow", "e"))
            self.other_option_start.setItemText(8, _translate("MainWindow", "f"))
            self.other_option_start.setItemText(9, _translate("MainWindow", "g"))
            self.other_option_start.setItemText(10, _translate("MainWindow", "h"))
            self.other_option_start.setItemText(11, _translate("MainWindow", "i"))
            self.other_option_start.setItemText(12, _translate("MainWindow", "j"))
            self.other_option_start.setItemText(13, _translate("MainWindow", "k"))
            self.other_option_start.setItemText(14, _translate("MainWindow", "l"))
            self.other_option_start.setItemText(15, _translate("MainWindow", "m"))
            self.other_option_start.setItemText(16, _translate("MainWindow", "n"))
            self.other_option_start.setItemText(17, _translate("MainWindow", "o"))
            self.other_option_start.setItemText(18, _translate("MainWindow", "p"))
            self.other_option_start.setItemText(19, _translate("MainWindow", "q"))
            self.other_option_start.setItemText(20, _translate("MainWindow", "r"))
            self.other_option_start.setItemText(21, _translate("MainWindow", "s"))
            self.other_option_start.setItemText(22, _translate("MainWindow", "t"))
            self.other_option_start.setItemText(23, _translate("MainWindow", "u"))
            self.other_option_start.setItemText(24, _translate("MainWindow", "v"))
            self.other_option_start.setItemText(25, _translate("MainWindow", "w"))
            self.other_option_start.setItemText(26, _translate("MainWindow", "x"))
            self.other_option_start.setItemText(27, _translate("MainWindow", "y"))
            self.other_option_start.setItemText(28, _translate("MainWindow", "z"))
            self.other_option_start.setItemText(29, _translate("MainWindow", "A"))
            self.other_option_start.setItemText(30, _translate("MainWindow", "B"))
            self.other_option_start.setItemText(31, _translate("MainWindow", "C"))
            self.other_option_start.setItemText(32, _translate("MainWindow", "D"))
            self.other_option_start.setItemText(33, _translate("MainWindow", "E"))
            self.other_option_start.setItemText(34, _translate("MainWindow", "F"))
            self.other_option_start.setItemText(35, _translate("MainWindow", "G"))
            self.other_option_start.setItemText(36, _translate("MainWindow", "H"))
            self.other_option_start.setItemText(37, _translate("MainWindow", "I"))
            self.other_option_start.setItemText(38, _translate("MainWindow", "J"))
            self.other_option_start.setItemText(39, _translate("MainWindow", "K"))
            self.other_option_start.setItemText(40, _translate("MainWindow", "L"))
            self.other_option_start.setItemText(41, _translate("MainWindow", "M"))
            self.other_option_start.setItemText(42, _translate("MainWindow", "N"))
            self.other_option_start.setItemText(43, _translate("MainWindow", "O"))
            self.other_option_start.setItemText(44, _translate("MainWindow", "P"))
            self.other_option_start.setItemText(45, _translate("MainWindow", "Q"))
            self.other_option_start.setItemText(46, _translate("MainWindow", "R"))
            self.other_option_start.setItemText(47, _translate("MainWindow", "S"))
            self.other_option_start.setItemText(48, _translate("MainWindow", "T"))
            self.other_option_start.setItemText(49, _translate("MainWindow", "U"))
            self.other_option_start.setItemText(50, _translate("MainWindow", "V"))
            self.other_option_start.setItemText(51, _translate("MainWindow", "W"))
            self.other_option_start.setItemText(52, _translate("MainWindow", "X"))
            self.other_option_start.setItemText(53, _translate("MainWindow", "Y"))
            self.other_option_start.setItemText(54, _translate("MainWindow", "Z"))
            self.other_option_start.setItemText(55, _translate("MainWindow", "1"))
            self.other_option_start.setItemText(56, _translate("MainWindow", "2"))
            self.other_option_start.setItemText(57, _translate("MainWindow", "3"))
            self.other_option_start.setItemText(58, _translate("MainWindow", "4"))
            self.other_option_start.setItemText(59, _translate("MainWindow", "5"))
            self.other_option_start.setItemText(60, _translate("MainWindow", "6"))
            self.other_option_start.setItemText(61, _translate("MainWindow", "7"))
            self.other_option_start.setItemText(62, _translate("MainWindow", "8"))
            self.other_option_start.setItemText(63, _translate("MainWindow", "9"))
            self.other_option_start.setItemText(64, _translate("MainWindow", "0"))
            self.other_option_start.setItemText(65, _translate("MainWindow", "\\"))
            self.other_option_start.setItemText(66, _translate("MainWindow", "["))
            self.other_option_start.setItemText(67, _translate("MainWindow", "]"))
            self.other_option_start.setItemText(68, _translate("MainWindow", "="))
            self.other_option_start.setItemText(69, _translate("MainWindow", "-"))
            self.other_option_start.setItemText(70, _translate("MainWindow", "/"))
            self.other_option_start.setItemText(71, _translate("MainWindow", "`"))
            self.other_option_start.setItemText(72, _translate("MainWindow", "~"))
            self.accept_other.setText(_translate("MainWindow", "use this instead of the text box"))
            self.other_option_2.setItemText(2, _translate("MainWindow", "space"))
            self.other_option_2.setItemText(3, _translate("MainWindow", "a"))
            self.other_option_2.setItemText(4, _translate("MainWindow", "b"))
            self.other_option_2.setItemText(5, _translate("MainWindow", "c"))
            self.other_option_2.setItemText(6, _translate("MainWindow", "d"))
            self.other_option_2.setItemText(7, _translate("MainWindow", "e"))
            self.other_option_2.setItemText(8, _translate("MainWindow", "f"))
            self.other_option_2.setItemText(9, _translate("MainWindow", "g"))
            self.other_option_2.setItemText(10, _translate("MainWindow", "h"))
            self.other_option_2.setItemText(11, _translate("MainWindow", "i"))
            self.other_option_2.setItemText(12, _translate("MainWindow", "j"))
            self.other_option_2.setItemText(13, _translate("MainWindow", "k"))
            self.other_option_2.setItemText(14, _translate("MainWindow", "l"))
            self.other_option_2.setItemText(15, _translate("MainWindow", "m"))
            self.other_option_2.setItemText(16, _translate("MainWindow", "n"))
            self.other_option_2.setItemText(17, _translate("MainWindow", "o"))
            self.other_option_2.setItemText(18, _translate("MainWindow", "p"))
            self.other_option_2.setItemText(19, _translate("MainWindow", "q"))
            self.other_option_2.setItemText(20, _translate("MainWindow", "r"))
            self.other_option_2.setItemText(21, _translate("MainWindow", "s"))
            self.other_option_2.setItemText(22, _translate("MainWindow", "t"))
            self.other_option_2.setItemText(23, _translate("MainWindow", "u"))
            self.other_option_2.setItemText(24, _translate("MainWindow", "v"))
            self.other_option_2.setItemText(25, _translate("MainWindow", "w"))
            self.other_option_2.setItemText(26, _translate("MainWindow", "x"))
            self.other_option_2.setItemText(27, _translate("MainWindow", "y"))
            self.other_option_2.setItemText(28, _translate("MainWindow", "z"))
            self.other_option_2.setItemText(29, _translate("MainWindow", "A"))
            self.other_option_2.setItemText(30, _translate("MainWindow", "B"))
            self.other_option_2.setItemText(31, _translate("MainWindow", "C"))
            self.other_option_2.setItemText(32, _translate("MainWindow", "D"))
            self.other_option_2.setItemText(33, _translate("MainWindow", "E"))
            self.other_option_2.setItemText(34, _translate("MainWindow", "F"))
            self.other_option_2.setItemText(35, _translate("MainWindow", "G"))
            self.other_option_2.setItemText(36, _translate("MainWindow", "H"))
            self.other_option_2.setItemText(37, _translate("MainWindow", "I"))
            self.other_option_2.setItemText(38, _translate("MainWindow", "J"))
            self.other_option_2.setItemText(39, _translate("MainWindow", "K"))
            self.other_option_2.setItemText(40, _translate("MainWindow", "L"))
            self.other_option_2.setItemText(41, _translate("MainWindow", "M"))
            self.other_option_2.setItemText(42, _translate("MainWindow", "N"))
            self.other_option_2.setItemText(43, _translate("MainWindow", "O"))
            self.other_option_2.setItemText(44, _translate("MainWindow", "P"))
            self.other_option_2.setItemText(45, _translate("MainWindow", "Q"))
            self.other_option_2.setItemText(46, _translate("MainWindow", "R"))
            self.other_option_2.setItemText(47, _translate("MainWindow", "S"))
            self.other_option_2.setItemText(48, _translate("MainWindow", "T"))
            self.other_option_2.setItemText(49, _translate("MainWindow", "U"))
            self.other_option_2.setItemText(50, _translate("MainWindow", "V"))
            self.other_option_2.setItemText(51, _translate("MainWindow", "W"))
            self.other_option_2.setItemText(52, _translate("MainWindow", "X"))
            self.other_option_2.setItemText(53, _translate("MainWindow", "Y"))
            self.other_option_2.setItemText(54, _translate("MainWindow", "Z"))
            self.other_option_2.setItemText(55, _translate("MainWindow", "1"))
            self.other_option_2.setItemText(56, _translate("MainWindow", "2"))
            self.other_option_2.setItemText(57, _translate("MainWindow", "3"))
            self.other_option_2.setItemText(58, _translate("MainWindow", "4"))
            self.other_option_2.setItemText(59, _translate("MainWindow", "5"))
            self.other_option_2.setItemText(60, _translate("MainWindow", "6"))
            self.other_option_2.setItemText(61, _translate("MainWindow", "7"))
            self.other_option_2.setItemText(62, _translate("MainWindow", "8"))
            self.other_option_2.setItemText(63, _translate("MainWindow", "9"))
            self.other_option_2.setItemText(64, _translate("MainWindow", "0"))
            self.other_option_2.setItemText(65, _translate("MainWindow", "\\"))
            self.other_option_2.setItemText(66, _translate("MainWindow", "["))
            self.other_option_2.setItemText(67, _translate("MainWindow", "]"))
            self.other_option_2.setItemText(68, _translate("MainWindow", "="))
            self.other_option_2.setItemText(69, _translate("MainWindow", "-"))
            self.other_option_2.setItemText(70, _translate("MainWindow", "/"))
            self.other_option_2.setItemText(71, _translate("MainWindow", "`"))
            self.other_option_2.setItemText(72, _translate("MainWindow", "~"))
            self.start_other.setText(_translate("MainWindow", "start"))
            self.stop_other.setText(_translate("MainWindow", "stop"))
            MainWindow.setCentralWidget(self.centralwidget)
        except Exception as error:
            print(error.__str__())

    def connect(self):
        try:
            global key
            self.delta_time.timeout.connect(self.update)
            self.clicking = {'active':False, 'time':1.1, 'type':'keyboard', 'amount':1, 'last':float(self.show_time())}
            self.start.clicked.connect(self.begin)
            self.stop.clicked.connect(self.stopClicking)
            self.save.clicked.connect(self.set_hotkey)
            self.clear.clicked.connect(self.clear_hotkey)
            self.help.clicked.connect(self.help_widget)
            self.time_count = 0
            self.start_hotkey = None
            self.stop_hotkey = None
            self.repeation_input.setMaximum(9999)
            self.start_input.setMaxLength(1)
            self.stop_input.setMaxLength(1)
            self.same_hotkey_wait = self.show_time()
            self.last_key = None
            key = None
            self.Minimized = False

            self.milliseconds_box.valueChanged.connect(lambda: self.not_zero('milliseconds'))
            self.seconds_box.valueChanged.connect(lambda: self.not_zero('seconds'))
            self.minutes_box.valueChanged.connect(lambda: self.not_zero('minutes'))

            self.delta_time.start()
        except Exception as error:
            print(error.__str__())

    def help_widget(self):
        self.helpUI.show()
        MainWindow.hide()

    def update(self):
        try:
            global key
            self.datetime = datetime.now()

            if self.options.currentText() != "keyboard":
                self.keyboard_input.hide()
                self.keyboard_input_label.hide()
            else:
                self.keyboard_input.show()
                self.keyboard_input_label.show()

            if self.last_key != key and key == self.start_hotkey or key == self.stop_hotkey:
                self.last_key = key
                if key == self.start_hotkey and not self.clicking['active']:
                    print("clicked start")
                    self.begin()

                elif key == self.stop_hotkey and self.clicking['active']:
                    print("clicked stop")
                    self.stopClicking()
                key = None

        except Exception as error:
            print(error.__str__())
        self.click()

    def click(self):
        try:
            if self.clicking['active'] and self.clicking['amount'] != 0 and self.check_time(self.clicking['last'], self.get_goal_time):
                self.clicking['last'] = float(self.show_time())
                match self.clicking['type']:
                    case "left click":
                        pyautogui.leftClick()
                    case "right click":
                        pyautogui.rightClick()
                    case "keyboard":
                        pyautogui.write(self.keyboard_input.toPlainText())
                    case "middle click":
                        pyautogui.middleClick()
                if self.clicking['amount'] != None:
                    self.clicking['amount'] -= 1
            elif self.clicking['active'] and not self.check_time(self.clicking['last'], self.get_goal_time):
                if self.clicking['last'] > self.get_goal_time:
                    self.clicking['last'] = 0
            if self.clicking['amount'] != None and self.clicking['active'] and self.clicking['amount'] <= 0:
                self.stopClicking()
        except Exception as error:
            print(error.__str__())
    def default(self):
        self.repeat_forever.click()
        self.stop.setEnabled(False)
        self.seconds_box.setValue(1)
        self.repeation_input.setMinimum(1)

    def begin(self):
        self.clicking['active'] = True
        self.clicking['time'] = self.get_goal_time
        self.clicking['type'] = self.options.currentText()
        self.clicking['amount'] = self.repeation_input.value() if self.repeat_how_many.isChecked() else None

        self.options.setEnabled(False)
        self.stop.setEnabled(True)
        self.start.setEnabled(False)
        self.milliseconds_box.setEnabled(False)
        self.seconds_box.setEnabled(False)
        self.minutes_box.setEnabled(False)
        self.repeat_forever.setEnabled(False)
        self.repeat_how_many.setEnabled(False)
        self.repeation_input.setEnabled(False)
        self.keyboard_input.setEnabled(False)
        self.start_input.setEnabled(False)
        self.stop_input.setEnabled(False)
        self.save.setEnabled(False)
        self.clear.setEnabled(False)
        self.accept_other.setEnabled(False)


    def stopClicking(self):
        self.clicking['active'] = False

        self.options.setEnabled(True)
        self.stop.setEnabled(False)
        self.start.setEnabled(True)
        self.milliseconds_box.setEnabled(True)
        self.seconds_box.setEnabled(True)
        self.minutes_box.setEnabled(True)
        self.repeat_forever.setEnabled(True)
        self.repeat_how_many.setEnabled(True)
        self.repeation_input.setEnabled(True)
        self.keyboard_input.setEnabled(True)
        self.start_input.setEnabled(True)
        self.stop_input.setEnabled(True)
        self.save.setEnabled(True)
        self.clear.setEnabled(True)
        self.accept_other.setEnabled(True)

    @property
    def get_goal_time(self):
        self.time = self.milliseconds_box.value() / 100
        self.time += self.seconds_box.value()
        self.time += self.minutes_box.value() * 60

        return self.time

    def not_zero(self, type):
        if self.get_goal_time != 0:
            return

        match type:
            case 'minutes':
                self.minutes_box.setValue(1)
            case 'seconds':
                self.seconds_box.setValue(1)
            case 'milliseconds':
                self.milliseconds_box.setValue(1)
    def check_time(self, last : float, goal : float):
        current = float(self.show_time())
        if current - last >= goal:
            return True
        else:
            return False

    def set_hotkey(self):
        if self.accept_other.isChecked():
            self.start_hotkey = self.other_option_start.currentText()
            self.stop_hotkey = self.other_option_2.currentText()
        else:
            self.start_hotkey = self.start_input.text()
            self.stop_hotkey = self.stop_input.text()

        self.start.setText("start\n(" + self.start_hotkey + ")")
        self.stop.setText("stop\n(" + self.stop_hotkey + ")")
    def clear_hotkey(self):
        self.start_hotkey = None
        self.stop_hotkey = None
        self.start.setText("start")
        self.stop.setText("stop")

    def save_data(self):
        import os
        import json

        file_name = "prefs.json"
        app_data_folder = os.getenv("LOCALAPPDATA")
        directory = "auto clicker"
        file_path = os.path.join(app_data_folder, directory, file_name)

        if not os.path.exists(os.path.join(app_data_folder, directory)):
            os.makedirs(os.path.join(app_data_folder, directory))

        data = {"start_hotkey":self.start_hotkey, "stop_hotkey":self.stop_hotkey, "time_minutes":self.minutes_box.value(), "time_seconds":self.seconds_box.value(), "time_milliseconds":self.milliseconds_box.value(), "type":self.options.currentText(), "text":self.keyboard_input.toPlainText()}

        with open(file_path, "w") as file:
            json.dump(data, file)
    def load_data(self):
        import os
        import json

        file_name = "prefs.json"
        app_data_folder = os.getenv("LOCALAPPDATA")
        directory = "auto clicker"
        file_path = os.path.join(app_data_folder, directory, file_name)

        if not os.path.exists(os.path.join(app_data_folder, directory)):
            return

        with open(file_path, "r") as file:
            data = json.load(file)
            self.milliseconds_box.setValue(data['time_milliseconds'])
            self.minutes_box.setValue(data['time_minutes'])
            self.seconds_box.setValue(data['time_seconds'])
            self.options.setCurrentText(data['type'])
            self.keyboard_input.setText(data['text'])
            self.start_input.setText(data['start_hotkey'])
            self.stop_input.setText(data['stop_hotkey'])
            self.set_hotkey()
            self.start_input.setText("")
            self.stop_input.setText("")

class MainWindow(QtWidgets.QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.hook = keyboard.on_press(self.keyboardEventReceived)
        global key

    def keyboardEventReceived(self, event):
        global key
        if event.event_type == 'down':
            key = event.name

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.default()
    ui.connect()
    ui.load_data()
    MainWindow.closed.connect(lambda: ui.save_data())
    MainWindow.show()
    sys.exit(app.exec_())