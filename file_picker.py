from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import cv2
import sys

class FilePicker(QMainWindow):
    def __init__(self):
        super(FilePicker, self).__init__()

        #Load the design UI
        uic.loadUi("filePickerDialog.ui", self)

        # Define our Widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")

        # Click the drop down box
        self.button.clicked.connect(self.clicker)

        # Show the app
        self.show()

    def clicker(self):
        # Assign the file name of the image to a variable
        fileName = QFileDialog.getOpenFileName(self, "Open File", "", "Image files (*.png *.jpg *.bmp);; All Files (*)")

        if fileName:
            # Display the name of the file
            self.label.setText(fileName[0])
            
            # load the input image
            img = cv2.imread(fileName[0])

            # convert the input image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # apply thresholding to convert grayscale to binary image
            #ret,thresh = cv2.threshold(gray, 500, 800,0)

            # display the binary image
            cv2.imshow("Binary image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


app = QApplication(sys.argv)
UIWindow = FilePicker()
app.exec_()

