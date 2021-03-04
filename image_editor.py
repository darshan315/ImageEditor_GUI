import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QGridLayout()

        self.btn_1 = QPushButton("Load Image")
        self.btn_1.clicked.connect(self.openFileNameDialog)

        self.btn_2 = QPushButton("Save Image")
        self.btn_2.clicked.connect(self.saveFileDialog)

        layout.addWidget(self.btn_1)
        layout.addWidget(self.btn_2)

        self.setLayout(layout)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                       "All Files (*);;JPG/JPEG files (*.jpg);;PNG files(*.png);;"
                                                       "BMP files(*.bmp)", options=options)
        if self.fileName:
            print(self.fileName)

        self.newsecondDialog()

    def newsecondDialog(self):
        left = 10
        top = 10
        width = 656
        height = 1056

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
        self.changedImage_()

        self.vbox.addWidget(l1)
        self.vbox.addStretch()
        self.vbox.addWidget(self.label_1)
        self.vbox.addStretch()
        self.vbox.addWidget(l2)
        self.vbox.addStretch()
        self.vbox.addWidget(self.label_2)

        self.win.setLayout(self.vbox)

        self.win.setWindowTitle("QLabel Demo")
        self.win.show()

    def origionalImage_(self):
        self.label_1.resize(512, 512)
        self.label_1.setAlignment(Qt.AlignCenter)

        # convert image file into pixmap
        self.myPixmap_1 = QPixmap(self.fileName)

        # set pixmap onto the label widget
        myScaledPixmap = self.myPixmap_1.scaled(self.label_1.size(), Qt.KeepAspectRatio)
        self.label_1.setPixmap(myScaledPixmap)

    def changedImage_(self):
        self.label_2.resize(512, 512)
        self.label_2.setAlignment(Qt.AlignCenter)

        # convert image file into pixmap
        self.myPixmap_2 = QPixmap(self.fileName)

        # set pixmap onto the label widget
        myScaledPixmap = self.myPixmap_1.scaled(self.label_1.size(), Qt.KeepAspectRatio)
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

