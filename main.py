from PyQt5.QtWidgets import QApplication, QLineEdit
from QKeyBoard import KeyboardWidget

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        keyboard_widget.show()
        keyboard_widget.setTextBox(self)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    keyboard_widget = KeyboardWidget()
    keyboard_widget.setGeometry(0, 100, 800, 180)
    keyboard_widget.set_keyboard_color("green", "white")
    keyboard_widget.hide()

    line_edit = CustomLineEdit()
    line_edit.setGeometry(0, 0, 810, 40)
    line_edit.show()

    sys.exit(app.exec_())



