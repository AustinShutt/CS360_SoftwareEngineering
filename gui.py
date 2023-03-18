from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# Third window class
class ThirdWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ThirdWindow, self).__init__(parent)
        # Set window title
        self.setWindowTitle("Image Analysis v1.0 - Page 3")
        # Set window size
        self.setFixedWidth(1024)
        self.setFixedHeight(768)
        # Load third page
        self.loadPage3()

    def loadPage3(self):
        # Next button
        self.nextButton = QPushButton('Next', self)
        self.nextButton.move(750, 650)

        # Previous button
        self.prevButton = QPushButton('Previous', self)
        self.prevButton.move(150, 650)
        self.prevButton.clicked.connect(self.goBack)

        # Text label
        self.textLabel = QLabel('Page 3 is loading this is super cool', self)
        self.textLabel.setFixedSize(400,100)
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.textLabel.setFont(QFont('Arial', 16))
        self.textLabel.size
        self.textLabel.move(300, 300)

        # Show all the widgets
        self.show()

    def goBack(self):
        # Go back to SecondWindow
        self.hide()
        self.parent().show()

# Second window class
class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        # Set window title
        self.setWindowTitle("Image Analysis v1.0 - Page 2")
        # Set window size
        self.setFixedWidth(1024)
        self.setFixedHeight(768)
        # Load second page
        self.loadPage2()

    def loadPage2(self):
        # Next button
        self.nextButton = QPushButton('Next', self)
        self.nextButton.move(750, 650)
        self.nextButton.clicked.connect(self.loadPage3)

        # Previous button
        self.prevButton = QPushButton('Previous', self)
        self.prevButton.move(150, 650)
        self.prevButton.clicked.connect(self.goBack)

        # Show all the widgets
        self.show()

    def goBack(self):
        # Go back to MainWindow
        self.hide()
        self.parent().show()

    def loadPage3(self):
        # Load third page
        print('Loading Page 3')
        self.hide()
        self.thirdWindow = ThirdWindow(self)
        self.thirdWindow.show()

# First window class
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Set window title
        self.setWindowTitle("Image Analysis v1.0")
        # Set window size
        self.setFixedWidth(1024)
        self.setFixedHeight(768)
        # Load first page
        self.loadPage1()

    def loadPage1(self):
        # Create title Label
        self.titleLabel = QLabel('Image Analysis v1.0', self)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(QFont('Arial', 36))
        # Alignment
        self.titleLabel.move(130,30)
        self.titleLabel.setFixedSize(800,100)

        # Create intro text label
        self.introLabel = QLabel('This program is designed to teach you the fundamentals of artificial intelligence, machine learning,'
                                  + 'and how it is used to analyze images. It will provide a short crash course in image analysis, including topics '
                                  + 'such as convolution, image segmentation, and machine learning.', self)
        self.introLabel.setAlignment(Qt.AlignCenter)
        self.introLabel.setFont(QFont('Arial', 16))
        self.introLabel.setWordWrap(True)
        # Alignment
        self.introLabel.move(110,150)
        self.introLabel.setFixedSize(800,100)

        # Create Get Started button
        self.startButton = QPushButton('Get Started', self)
        self.startButton.move(480,400)

        # startButton functionality
        @pyqtSlot()
        def on_click():
            # Test
            print('You clicked Get Started')
            self.hide()
            self.secondWindow = SecondWindow(self)
            self.secondWindow.show()

        # Add click functionality to startButton
        self.startButton.clicked.connect(on_click)

        # Show all the widgets
        self.show()
        
# Requirement for every GUI app using *Qt
# One and only one instance allowed
# [] = CLAs
app = QApplication([])

# Create window instance
window = MainWindow()

# Start the app
app.exec()
