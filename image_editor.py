import os
import sys

from PIL import Image, ImageEnhance
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.changedFile = ""
        self.setWindowTitle(self.title)
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QGridLayout()

        #toolbar
        self.toolBar = QToolBar("File")
        self.layout.addWidget(self.toolBar)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        open_ac = QAction(QIcon("open.png"), "open", self)
        open_ac.triggered.connect(self.openFileNameDialog)

        save_ac = QAction(QIcon("save.png"), "save", self)
        save_ac.triggered.connect(self.saveFileDialog)

        self.toolBar.addAction(open_ac)
        self.toolBar.addAction(save_ac)

        #slider
        slider_1 = "Contrast"
        slider_2 = "Brightness"
        slider_3 = "Rotation"

        contrastSlider = self.contrastSlider(slider_1)
        brightnessSlider = self.brightnessSlider(slider_2)
        rotationSlider = self.rotationSlider(slider_3)

        self.layout.addWidget(contrastSlider, 1, 0)
        self.layout.addWidget(brightnessSlider, 2, 0)
        self.layout.addWidget(rotationSlider, 3, 0)

        self.setLayout(self.layout)

    def contrastSlider(self, NaMe):
        groupBox = QGroupBox()

        radio1 = QRadioButton(NaMe)

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setSingleStep(5)

        slider.valueChanged.connect(self.contrastChanged)

        radio1.setChecked(True)

        self.contrastLabel = QLabel()
        self.contrastLabel.setGeometry(220, 125, 200, 60)
        self.contrastLabel.setWordWrap(True)
        value = slider.value()
        self.contrastLabel.setText("Value : " + str(value))

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        vbox.addWidget(self.contrastLabel)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def contrastChanged(self, value):
        self.contrastLabel.setText("Value : " + str(value))

        enhancer = ImageEnhance.Contrast(self.pilChangedImage)
        factor = value/50

        temp = os.path.splitext(self.fileName)
        var = (os.path.basename(temp[0]), temp[1])
        CURR_DIR = os.getcwd()

        im_output = enhancer.enhance(factor)
        im_output.save('temp'+temp[1])
        self.changedFile = CURR_DIR + '/temp'+temp[1]
        self.changedImage_(self.changedFile)

    def brightnessSlider(self, NaMe):
        groupBox = QGroupBox()

        radio1 = QRadioButton(NaMe)

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setSingleStep(5)

        slider.valueChanged.connect(self.brightnessChanged)

        radio1.setChecked(True)

        self.brightnessLabel = QLabel()
        self.brightnessLabel.setGeometry(220, 125, 200, 60)
        self.brightnessLabel.setWordWrap(True)
        value = slider.value()
        self.brightnessLabel.setText("Value : " + str(value))

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        vbox.addWidget(self.brightnessLabel)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def brightnessChanged(self, value):
        self.brightnessLabel.setText("Value : " + str(value))
        enhancer = ImageEnhance.Brightness(self.pilChangedImage)
        factor = value/50

        temp = os.path.splitext(self.fileName)
        var = (os.path.basename(temp[0]), temp[1])
        CURR_DIR = os.getcwd()

        im_output = enhancer.enhance(factor)
        im_output.save('temp'+temp[1])
        self.changedFile = CURR_DIR + '/temp'+temp[1]
        self.changedImage_(self.changedFile)
        #self.newsecondDialog(self.changedFile)


    def rotationSlider(self, NaMe):
        groupBox = QGroupBox()

        radio1 = QRadioButton(NaMe)

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setMinimum(0)
        slider.setMaximum(360)
        slider.setValue(0)
        slider.setSingleStep(90)

        slider.valueChanged.connect(self.rotationChanged)

        radio1.setChecked(True)

        self.rotationLabel = QLabel()
        self.rotationLabel.setGeometry(220, 125, 200, 60)
        self.rotationLabel.setWordWrap(True)
        value = slider.value()
        self.rotationLabel.setText("Value : " + str(value))

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        vbox.addWidget(self.rotationLabel)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def rotationChanged(self, value):
        self.rotationLabel.setText("Value : " + str(value))

        temp = os.path.splitext(self.fileName)
        CURR_DIR = os.getcwd()

        im_output = self.pilChangedImage.rotate(value)

        im_output.save('temp'+temp[1])
        self.changedFile = CURR_DIR + '/temp'+temp[1]
        self.changedImage_(self.changedFile)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                       "All Files (*);;JPG/JPEG files (*.jpg);;PNG files(*.png);;"
                                                       "BMP files(*.bmp)", options=options)
        if self.fileName:
            print(self.fileName)

        self.newsecondDialog(self.changedFile)

    def newsecondDialog(self, changedFile):
        left = 10
        top = 10
        width = 656
        height = 1056

        if not changedFile:
            changedFile = self.fileName

        self.win = QWidget()
        self.win.setGeometry(left, top, width, height)

        self.vbox = QVBoxLayout()
        l1 = QLabel()
        l1.setText("Original Image")
        l1.setAlignment(Qt.AlignCenter)

        l2 = QLabel()
        l2.setText("Changed Image")
        l2.setAlignment(Qt.AlignCenter)

        self.label_1 = QLabel(self.win)
        self.label_2 = QLabel(self.win)

        self.origionalImage_()
        self.changedImage_(changedFile)

        self.vbox.addWidget(l1)
        self.vbox.addStretch()
        self.vbox.addWidget(self.label_1)
        self.vbox.addStretch()
        self.vbox.addWidget(l2)
        self.vbox.addStretch()
        self.vbox.addWidget(self.label_2)

        self.win.setLayout(self.vbox)

        self.win.setWindowTitle("Image viewer")
        self.win.show()

    def origionalImage_(self):
        self.label_1.resize(512, 512)
        self.label_1.setAlignment(Qt.AlignCenter)

        # convert image file into pixmap
        self.myPixmap_1 = QPixmap(self.fileName)

        # set pixmap onto the label widget
        myScaledPixmap = self.myPixmap_1.scaled(self.label_1.size(), Qt.KeepAspectRatio)
        self.label_1.setPixmap(myScaledPixmap)

    def changedImage_(self, filename):
        self.label_2.resize(512, 512)
        self.label_2.setAlignment(Qt.AlignCenter)

        # convert image file into pixmap
        self.myPixmap_2 = QPixmap(filename)
        self.pilChangedImage = Image.open(self.fileName)

        # set pixmap onto the label widget
        myScaledPixmap = self.myPixmap_2.scaled(self.label_2.size(), Qt.KeepAspectRatio)
        self.label_2.setPixmap(myScaledPixmap)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        savefileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", ".png",
                                                      "All Files (*);;JPG/JPEG files (*.jpg);;PNG files(*.png);;"
                                                      "BMP files(*.bmp)", options=options)
        if savefileName:
            print(savefileName)

        self.myPixmap_2.save(savefileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
