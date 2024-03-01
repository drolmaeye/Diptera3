import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import pyqtgraph as pg


class FileSpinbox(qtw.QSpinBox):

    def __init__(self):
        super().__init__()



class Window(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        # create central widget
        self.main_widget = qtw.QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = qtw.QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.my_spinbox = FileSpinbox()
        self.my_spinbox.setMaximum(100000)
        self.main_layout.addWidget(self.my_spinbox)

        self.my_spinbox.valueChanged.connect(self.show_new_value)



        self.show()

    def show_new_value(self):
        value = self.my_spinbox.value()
        leading_value = str(value).zfill(3)
        return print(leading_value)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = Window()
    sys.exit(app.exec())
