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

        # create scan control groupbox and add to the right side layout
        self.scan_control = qtw.QGroupBox()
        self.scan_control.setTitle('Scan Control')
        self.scan_control_layout = qtw.QGridLayout()
        self.scan_control.setLayout(self.scan_control_layout)
        self.right_side_layout.addWidget(self.scan_control)

        # create scan control widgets
        self.select_axis_label = qtw.QLabel('Stage')
        self.relative_min_label = qtw.QLabel('Relative min.')
        self.step_size_label = qtw.QLabel('Step size')
        self.relative_max_label = qtw.QLabel('Relative max.')
        self.num_points_label = qtw.QLabel('Points')

        self.fly_checkbox = qtw.QCheckBox('Fly axis')
        self.fly_axis = qtw.QComboBox()
        self.fly_axis.addItems(['Cen Y', 'Cen Z', 'More'])
        self.fly_min = qtw.QLineEdit()
        self.fly_stepsize = qtw.QLineEdit()
        self.fly_max = qtw.QLineEdit()
        self.fly_numpts = qtw.QLineEdit()

        self.step_checkbox = qtw.QCheckBox('Step axis')
        self.step_axis = qtw.QComboBox()
        self.step_axis.addItems(['Cen Y', 'Cen Z', 'More'])
        self.step_min = qtw.QLineEdit()
        self.step_stepsize = qtw.QLineEdit()
        self.step_max = qtw.QLineEdit()
        self.step_numpts = qtw.QLineEdit()

        self.scan_directory_label = qtw.QLabel('Scan directory')
        self.scan_directory = qtw.QLineEdit()
        self.scan_number_label = qtw.QLabel('Scan no.')
        self.scan_number = qtw.QLineEdit()
        self.select_directory_button = qtw.QPushButton('Browse')

        self.count_time_label = qtw.QLabel('Count time (s)')
        self.count_time = qtw.QLineEdit()
        self.start_scan_button = qtw.QPushButton('START SCAN')
        self.fly_y_button = qtw.QPushButton('Fly y')
        self.fly_z_button = qtw.QPushButton('Fly z')

        # add scan control widgets to scan control groupbox
        self.scan_control_layout.addWidget(self.select_axis_label, 0, 1, 1, 2)
        self.scan_control_layout.addWidget(self.relative_min_label, 0, 3)
        self.scan_control_layout.addWidget(self.step_size_label, 0, 4)
        self.scan_control_layout.addWidget(self.relative_max_label, 0, 5)
        self.scan_control_layout.addWidget(self.num_points_label, 0, 6)

        self.scan_control_layout.addWidget(self.fly_checkbox, 1, 0)
        self.scan_control_layout.addWidget(self.fly_axis, 1, 1, 1, 2)
        self.scan_control_layout.addWidget(self.fly_min, 1, 3)
        self.scan_control_layout.addWidget(self.fly_stepsize, 1, 4)
        self.scan_control_layout.addWidget(self.fly_max, 1, 5)
        self.scan_control_layout.addWidget(self.fly_numpts, 1, 6)

        self.scan_control_layout.addWidget(self.step_checkbox, 2, 0)
        self.scan_control_layout.addWidget(self.step_axis, 2, 1, 1, 2)
        self.scan_control_layout.addWidget(self.step_min, 2, 3)
        self.scan_control_layout.addWidget(self.step_stepsize, 2, 4)
        self.scan_control_layout.addWidget(self.step_max, 2, 5)
        self.scan_control_layout.addWidget(self.step_numpts, 2, 6)

        self.scan_control_layout.addWidget(self.scan_directory_label, 3, 0)
        self.scan_control_layout.addWidget(self.scan_directory, 3, 1, 1, 3)
        self.scan_control_layout.addWidget(self.scan_number_label, 3, 4)
        self.scan_control_layout.addWidget(self.scan_number, 3, 5)
        self.scan_control_layout.addWidget(self.select_directory_button, 3, 6)

        self.scan_control_layout.addWidget(self.count_time_label, 4, 0, 1, 2)
        self.scan_control_layout.addWidget(self.count_time, 4, 2)
        self.scan_control_layout.addWidget(self.start_scan_button, 4, 3, 1, 2)
        self.scan_control_layout.addWidget(self.fly_y_button, 4, 5)
        self.scan_control_layout.addWidget(self.fly_z_button, 4, 6)

        '''Centering control'''

        # create centering control groupbox and add to the right side layout
        self.centering_control = qtw.QGroupBox()
        self.centering_control.setTitle('Centering Control')
        self.centering_control_layout = qtw.QGridLayout()
        self.centering_control.setLayout(self.centering_control_layout)
        self.right_side_layout.addWidget(self.centering_control)

        # create centering control widgets
        self.delta_omega_label = qtw.QLabel(u'\u0394\u03c9')
        self.y_minus_label = qtw.QLabel('y at ' + u'\u03c9' + '-')
        self.y_zero_label = qtw.QLabel('y at ' + u'\u03c9' + '0')
        self.y_plus_label = qtw.QLabel('y at ' + u'\u03c9' + '+')
        self.x_correction_label = qtw.QLabel('x correction')
        self.y_correction_label = qtw.QLabel('y correction')

        self.centering_checkbox = qtw.QCheckBox('Enable')
        self.delta_omega = qtw.QLineEdit()
        self.y_minus = qtw.QLineEdit()
        self.y_zero = qtw.QLineEdit()
        self.y_plus = qtw.QLineEdit()
        self.x_correciton = qtw.QLineEdit()
        self.y_correction = qtw.QLineEdit()

        self.target_x_position_label = qtw.QLabel('Final target position -->')
        self.target_x_position = qtw.QPushButton('')

        # add centering control widgets to centering control groupbox
        self.centering_control_layout.addWidget(self.delta_omega_label, 0, 1)
        self.centering_control_layout.addWidget(self.y_minus_label, 0, 2)
        self.centering_control_layout.addWidget(self.y_zero_label, 0, 3)
        self.centering_control_layout.addWidget(self.y_plus_label, 0, 4)
        self.centering_control_layout.addWidget(self.x_correction_label, 0, 5)
        self.centering_control_layout.addWidget(self.y_correction_label, 0, 6)

        self.centering_control_layout.addWidget(self.centering_checkbox, 1, 0)
        self.centering_control_layout.addWidget(self.delta_omega, 1, 1)
        self.centering_control_layout.addWidget(self.y_minus, 1, 2)
        self.centering_control_layout.addWidget(self.y_zero, 1, 3)
        self.centering_control_layout.addWidget(self.y_plus, 1, 4)
        self.centering_control_layout.addWidget(self.x_correciton, 1, 5)
        self.centering_control_layout.addWidget(self.y_correction, 1, 6)

        self.centering_control_layout.addWidget(self.target_x_position_label, 2, 3, 1, 2)
        self.centering_control_layout.addWidget(self.target_x_position, 2, 5)

        '''Intensity control'''

        # create intensity control groupbox and add to the right side layout
        self.intensity_control = qtw.QGroupBox()
        self.intensity_control.setTitle('Intensity Control')
        self.intensity_control_layout = qtw.QGridLayout()
        self.intensity_control.setLayout(self.intensity_control_layout)
        self.right_side_layout.addWidget(self.intensity_control)

        # create intensity control widgets
        self.active_counter_label = qtw.QLabel('Active counter')
        self.scale_factor_label = qtw.QLabel('Scale factor')
        self.data_type_label = qtw.QLabel('Data type')
        self.scaling_label = qtw.QLabel('2D scaling')

        self.i_signal_label = qtw.QLabel('I(signal)')
        self.i_signal_counter = qtw.QComboBox()
        self.scale_factor = qtw.QLineEdit()
        self.data_type = qtw.QComboBox()
        self.scaling_max = qtw.QSpinBox()
        self.colors = qtw.QSpinBox()

        self.i_reference_checkbox = qtw.QCheckBox('I(reference)')
        self.i_reference_counter = qtw.QComboBox()
        self.scaling_min = qtw.QSpinBox()

        # add intensity control widgets to intensity control groupbox
        self.intensity_control_layout.addWidget(self.active_counter_label, 0, 1, 1, 2)
        self.intensity_control_layout.addWidget(self.scale_factor_label, 0, 3)
        self.intensity_control_layout.addWidget(self.data_type_label, 0, 4)
        self.intensity_control_layout.addWidget(self.scaling_label, 0, 5, 1, 2)

        self.intensity_control_layout.addWidget(self.i_signal_label, 1, 0)
        self.intensity_control_layout.addWidget(self.i_signal_counter, 1, 1, 1, 2)
        self.intensity_control_layout.addWidget(self.scale_factor, 1, 3, 2, 1)
        self.intensity_control_layout.addWidget(self.data_type, 1, 4, 2, 1)
        self.intensity_control_layout.addWidget(self.scaling_max, 1, 5)
        self.intensity_control_layout.addWidget(self.colors, 1, 6, 2, 1)

        self.intensity_control_layout.addWidget(self.i_reference_checkbox, 2, 0)
        self.intensity_control_layout.addWidget(self.i_reference_counter, 2, 1, 1, 2)
        self.intensity_control_layout.addWidget(self.scaling_min, 2, 5)

        '''Position control'''

        # create position control groupbox and add to the right side layout
        self.position_control = qtw.QGroupBox()
        self.position_control.setTitle('Position Control')
        self.position_control_layout = qtw.QGridLayout()
        self.position_control.setLayout(self.position_control_layout)
        self.right_side_layout.addWidget(self.position_control)

        # create position control widgets
        self.active_element_label = qtw.QLabel('Active element')
        self.minimum_position_label = qtw.QLabel('Minimum')
        self.center_position_label = qtw.QLabel('Center')
        self.maximum_position_label = qtw.QLabel('Maximum')
        self.width_label = qtw.QLabel('Width')

        self.horizontal_axis_label = qtw.QLabel('Horizontal axis')
        self.active_horizontal_axis = qtw.QLineEdit()
        self.minimum_position_button = qtw.QPushButton('')
        self.center_position_button = qtw.QPushButton('')
        self.maximum_position_button = qtw.QPushButton('')
        self.markers_width = qtw.QLineEdit()

        self.vertical_axis_label = qtw.QLabel('Vertical axis')
        self.active_vertical_axis = qtw.QLineEdit()
        self.center_position = qtw.QLineEdit()

        # add position control widgets to position control groupbox
        self.position_control_layout.addWidget(self.active_element_label, 0, 1, 1, 2)
        self.position_control_layout.addWidget(self.minimum_position_label, 0, 3)
        self.position_control_layout.addWidget(self.center_position_label, 0, 4)
        self.position_control_layout.addWidget(self.maximum_position_label, 0, 5)
        self.position_control_layout.addWidget(self.width_label, 0, 6)

        self.position_control_layout.addWidget(self.horizontal_axis_label, 1, 0)
        self.position_control_layout.addWidget(self.active_horizontal_axis, 1, 1, 1, 2)
        self.position_control_layout.addWidget(self.minimum_position_button, 1, 3)
        self.position_control_layout.addWidget(self.center_position_button, 1, 4)
        self.position_control_layout.addWidget(self.maximum_position_button, 1, 5)
        self.position_control_layout.addWidget(self.markers_width, 1, 6)

        self.position_control_layout.addWidget(self.vertical_axis_label, 2, 0)
        self.position_control_layout.addWidget(self.active_vertical_axis, 2, 1, 1, 2)
        self.position_control_layout.addWidget(self.center_position, 2, 4)

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
