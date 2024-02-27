import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import pyqtgraph as pg


class Window(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        '''Foundation widgets'''

        # Establish MainWindow appearance
        self.setWindowTitle('Diptera3')
        self.setGeometry(100, 100, 1080, 720)

        # create central widget
        self.main_widget = qtw.QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = qtw.QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # establish left and right sides of GUI
        self.left_side_widget = qtw.QWidget()
        self.left_side_layout = qtw.QVBoxLayout()
        self.left_side_widget.setLayout(self.left_side_layout)
        self.main_layout.addWidget(self.left_side_widget)

        self.right_side_widget = qtw.QWidget()
        self.right_side_layout = qtw.QVBoxLayout()
        self.right_side_widget.setLayout(self.right_side_layout)
        self.main_layout.addWidget(self.right_side_widget)

        '''Menu bar'''

        # actions
        self.close_diptera_action = qtw.QAction('Exit', self)
        self.close_diptera_action.setShortcut('Ctrl+Q')
        # self.close_diptera_action.triggered.connect(self.closeEvent)

        # make menu, add headings, add actions
        self.main_menu = self.menuBar()
        self.file_menu = self.main_menu.addMenu('File')
        self.file_menu.addAction(self.close_diptera_action)

        '''
        Left side
        '''

        '''Plot window'''

        self.plot_window = pg.PlotWidget()
        self.left_side_layout.addWidget(self.plot_window)

        '''Plot toolbar'''

        self.plot_toolbar = qtw.QWidget()
        self.plot_toolbar_layout = qtw.QHBoxLayout()
        self.plot_toolbar.setLayout(self.plot_toolbar_layout)
        self.left_side_layout.addWidget(self.plot_toolbar)

        '''File control'''

        self.file_control = qtw.QGroupBox()
        self.file_control.setTitle('File Control')
        self.left_side_layout.addWidget(self.file_control)

        '''
        Right side
        '''

        '''Scan control'''

        self.scan_control = qtw.QGroupBox()
        self.scan_control.setTitle('Scan Control')
        self.right_side_layout.addWidget(self.scan_control)

        '''Centering control'''

        self.centering_control = qtw.QGroupBox()
        self.centering_control.setTitle('Centering Control')
        self.right_side_layout.addWidget(self.centering_control)

        '''Intensity control'''

        self.intensity_control = qtw.QGroupBox()
        self.intensity_control.setTitle('Intensity Control')
        self.right_side_layout.addWidget(self.intensity_control)

        '''Position control'''

        self.position_control = qtw.QGroupBox()
        self.position_control.setTitle('Position Control')
        self.right_side_layout.addWidget(self.position_control)

        '''Big buttons'''

        self.windows_control = qtw.QGroupBox()
        self.windows_control.setTitle('Windows Control')
        self.right_side_layout.addWidget(self.windows_control)











        #End UI
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = Window()
    sys.exit(app.exec())
