import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class KeyboardWidget(QWidget):
    def __init__(self, parent=None):
        super(KeyboardWidget, self).__init__(parent)
        self.currentTextBox = ''
        self.signalMapper = QSignalMapper(self)
        self.signalMapper.mapped[int].connect(self.buttonClicked)
        self.initUI()
        self.names = self.names_small
        self.sym_state = False  
        self.isCaps = False  
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)  
    def set_keyboard_color(self, background_color, text_color):
        self.setStyleSheet(f"background-color: {background_color}; color: {text_color};")

    @pyqtSlot()
    def do_caps(self):
        self.buttonAdd()
        self.caps_button.setText("ABC")
        self.caps_button.clicked.disconnect()
        self.caps_button.clicked.connect(self.do_small)

    @pyqtSlot()
    def do_small(self):
        self.names = self.names_small
        self.buttonAdd()
        self.caps_button.setText("abc")
        self.caps_button.clicked.disconnect()
        self.caps_button.clicked.connect(self.do_caps)

    def initUI(self):
        self.layout = QGridLayout()
        self.names_small = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '(', ')',
                            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.names_sym = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '~', '`',
                          '@', '#', '$', '%', '^', '&&', '*', '(', ')', '_', '-', '+', '=',
                          '|', '[', ']', '{', '}', "'", '"', '<', '>', '?', '\\', '/', '!']

        self.names = self.names_small
        self.buttonAdd()

        clear_button = QPushButton('Delall')
        clear_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        clear_button.setFont(QFont('Arial', 12))
        clear_button.KEY_CHAR = Qt.Key_Clear
        self.layout.addWidget(clear_button, 4, 0, 1, 2)
        clear_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(clear_button, clear_button.KEY_CHAR)

        space_button = QPushButton('Space')
        space_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        space_button.setFont(QFont('Arial', 12))
        space_button.KEY_CHAR = Qt.Key_Space
        self.layout.addWidget(space_button, 4, 2, 1, 2)
        space_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(space_button, space_button.KEY_CHAR)

        back_button = QPushButton('Del')
        back_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        back_button.setFont(QFont('Arial', 12))
        back_button.KEY_CHAR = Qt.Key_Backspace
        self.layout.addWidget(back_button, 4, 4, 1, 2)
        back_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(back_button, back_button.KEY_CHAR)

        enter_button = QPushButton('Enter')
        enter_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        enter_button.setFont(QFont('Arial', 12))
        enter_button.KEY_CHAR = Qt.Key_Enter
        self.layout.addWidget(enter_button, 4, 6, 1, 2)
        enter_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(enter_button, enter_button.KEY_CHAR)

        done_button = QPushButton('✔')
        done_button.setFixedHeight(25)
        done_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        done_button.setFont(QFont('Arial', 12))
        done_button.KEY_CHAR = Qt.Key_Home
        self.layout.addWidget(done_button, 4, 9, 1, 1)
        done_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(done_button, done_button.KEY_CHAR)

        caps_button = QPushButton('ABC')
        caps_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        caps_button.setFont(QFont('Arial', 12))
        caps_button.setFixedWidth(72)
        caps_button.KEY_CHAR = Qt.Key_Up
        self.layout.addWidget(caps_button, 3, 9, 1, 1)
        caps_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(caps_button, caps_button.KEY_CHAR)

        sym_button = QPushButton('@!#')
        sym_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        caps_button.setFixedWidth(70)
        sym_button.setFont(QFont('Arial', 12))
        sym_button.KEY_CHAR = Qt.Key_Down
        self.layout.addWidget(sym_button, 4, 8, 1, 1)
        sym_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(sym_button, sym_button.KEY_CHAR)

        self.setGeometry(0, 0, 800, 180)
        self.setLayout(self.layout)

    def buttonAdd(self):
        positions = [(i, j) for i in range(6) for j in range(10)]
        for position, name in zip(positions, self.names):
            if name == '':
                continue
            button = QPushButton(name)
            button.setFixedSize(72,28)
            button.KEY_CHAR = ord(name[-1])
            button.clicked.connect(self.signalMapper.map)
            self.signalMapper.setMapping(button, button.KEY_CHAR)
            self.layout.addWidget(button, *position)
                
    def buttonClicked(self, char_ord):
        if char_ord == Qt.Key_Home or char_ord == Qt.Key_Enter:
            self.hide()
            return
        if self.currentTextBox:
            if char_ord == Qt.Key_Up:
                self.toggleCaps()
                return
            elif char_ord == Qt.Key_Down:
                if self.sym_state:
                    self.names = self.names_small
                    self.sym_state = False
                else:
                    self.names = self.names_sym
                    self.sym_state = True
                self.buttonAdd()
                return
            elif char_ord == Qt.Key_Backspace:
                current_text = self.currentTextBox.text()
                self.currentTextBox.setText(current_text[:-1])
            elif char_ord == Qt.Key_Clear:
                self.currentTextBox.clear()
            elif char_ord == Qt.Key_Space:
                current_text = self.currentTextBox.text()
                self.currentTextBox.setText(current_text + ' ')
            else:
                current_text = self.currentTextBox.text()
                new_char = chr(char_ord).upper() if self.isCaps else chr(char_ord).lower()
                self.currentTextBox.setText(current_text + new_char)

    def setTextBox(self, textBox):
        self.currentTextBox = textBox
    def toggleCaps(self):
        self.isCaps = not self.isCaps
        for button in self.findChildren(QPushButton):
            if button.text().isalpha():
                button.setText(button.text().upper() if self.isCaps else button.text().lower())
