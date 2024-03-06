"""
This example demonstrates the use of ImageView with 3-color image stacks.
ImageView is a high-level widget for displaying and analyzing 2D and 3D data.
ImageView provides:

  1. A zoomable region (ViewBox) for displaying the image
  2. A combination histogram and gradient editor (HistogramLUTItem) for
     controlling the visual appearance of the image
  3. A timeline for selecting the currently displayed frame (for 3D data only).
  4. Tools for very basic analysis of image data (see ROI and Norm buttons)

"""
import time
import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
from pyqtgraph.Qt import QtCore

# Interpret image data as row-major instead of col-major
pg.setConfigOptions(imageAxisOrder='row-major')

app = pg.mkQApp("ImageView Example")

## Create window with ImageView widget
win = QtWidgets.QMainWindow()
win.resize(800,800)
imv = pg.ImageView(discreteTimeLine=True)
win.setCentralWidget(imv)
win.show()
win.setWindowTitle('pyqtgraph example: ImageView')
imv.setHistogramLabel("Histogram label goes here")


a = np.load('fScan_5029.npz')
fly = a['fly']
step = a['stp']
counts = a['bsd']
reference = a['ref']
a.close()

# Display the data and assign each frame a time value from 1.0 to 3.0
imv.setImage(counts)
# imv.play(10)

## Set a custom color map
# colors = [
#     (0, 0, 0),
#     (45, 5, 61),
#     (84, 42, 55),
#     (150, 87, 60),
#     (208, 171, 141),
#     (255, 255, 255)
# ]
# cmap = pg.ColorMap(pos=np.linspace(0.0, 1.0, 6), color=colors)
# imv.setColorMap(cmap)

cmap_list = pg.colormap.listMaps()
# print(cmap_list[-1])
# cm = pg.colormap.get(cmap_list[-1])
# imv.setColorMap(cm)

cm_length = len(cmap_list)
index=0
def update():
    global cmap_list, cm_length, index, imv
    if index < cm_length:
        cm = pg.colormap.get(cmap_list[index])
        imv.setColorMap(cm)
        print(cmap_list[index])
        index += 1
    else:
        print('out of maps')




# Start up with an ROI
imv.ui.roiBtn.setChecked(True)
imv.roiClicked()
print(pg.colormap.listMaps())


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(500)

if __name__ == '__main__':
    pg.exec()
