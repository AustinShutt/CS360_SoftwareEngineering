from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize button and set layout for intro page
        self.buttonGetStarted = QPushButton("Get Started", self)
        self.buttonGetStarted.move(463,650)
        self.buttonGetStarted.clicked.connect(self.show_first_page)

        # Set layout for first page
        self.setWindowTitle("Image Analysis v1.0")
        
        # Create intro flavor text label
        self.introLabel = QLabel('This program is designed to teach you the fundamentals of artificial intelligence, machine learning, '
                                  + 'and how it is used to analyze images. It will provide a short crash course in image analysis, including topics '
                                  + 'such as convolution, image segmentation, and machine learning.', self)
        self.introLabel.setAlignment(Qt.AlignCenter)
        self.introLabel.setFont(QFont('Arial', 16))
        self.introLabel.setWordWrap(True)
        self.introLabel.move(110,150)
        self.introLabel.setFixedSize(800,100)

    def show_first_page(self):
        # Remove the Get Started button
        self.buttonGetStarted.deleteLater()
        self.introLabel.deleteLater()

        # Initialize buttons for navigation
        self.buttonPrevious = QPushButton("Previous", self)
        self.buttonPrevious.move(50, 650)
        self.buttonPrevious.clicked.connect(self.show_previous_page)

        self.buttonNext = QPushButton("Next", self)
        self.buttonNext.move(874, 650)
        self.buttonNext.clicked.connect(self.show_next_page)

        # Initialize label to display content
        self.label = QLabel(self)
        self.show_page(1)

    def show_page(self, pageNumber):
        # Set content of the window based on page number
        
        if pageNumber == 1:
            # Keep track of current page
            self.label.setText("Page 1")
            self.label.setVisible(False)
            
            # Add stuff to the page
            self.p1textbox = QLabel("flavor text for Page 1", self)
            self.p1textbox.setGeometry(212, 212, 500, 300)
            self.p1textbox.setAlignment(Qt.AlignCenter)
            self.p1textbox.setFont(QFont('Arial', 16))
            
            # Show elements unique to this page
            self.p1textbox.setVisible(True)
            
            # Note: for proper functionality when navigating pages, we need to modify show_previous_page and show_next_page
            # Both functions check the current page, simply add a line for all elements unique to this page like so:
            # [element].setVisible(False)
            
        elif pageNumber == 2:
            self.label.setText("Page 2")
            
            # Add stuff to the page
            # Adding an image to page 2
            script_dir = os.path.dirname(os.path.abspath(__file__))
            imagePath = os.path.join(script_dir, "img", "default.png")
            pixmap = QPixmap(imagePath)
            if pixmap.isNull():
                print("Failed to load image file")
            self.imgLabel = QLabel(self)
            self.imgLabel.setPixmap(pixmap)
            self.imgLabel.setGeometry(50, 50, 924, 600)
            self.imgLabel.setAlignment(Qt.AlignCenter)
            
            # Show elements unique to this page
            self.imgLabel.setVisible(True)
            
        elif pageNumber == 3:
            self.label.setText("Page 3")
        elif pageNumber == 4:
            self.label.setText("Page 4")
        elif pageNumber == 5:
            self.label.setText("Page 5")
        elif pageNumber == 6:
            self.label.setText("Page 6")
        elif pageNumber == 7:
            self.label.setText("Page 7 (Last Page)")
            

        # Set visibility of navigation buttons
        if pageNumber == 1:
            self.buttonPrevious.setVisible(False)
        else:
            self.buttonPrevious.setVisible(True)
        if pageNumber == 7:
            self.buttonNext.setVisible(False)
        else:
            self.buttonNext.setVisible(True)

        # Show current page number in window title
        self.setWindowTitle(f"Image Analysis v1.0 - Page {pageNumber}")

    # Functionality to show previous/next pages - hide elements from current page
    def show_previous_page(self):
        # Find what page we're on
        currentPage = int(self.label.text().split()[1])
        self.show_page(currentPage - 1)
        
        # Hide elements unique to the current page
        if currentPage == 1:
            #
            self.p1textbox.setVisible(False)
            print("Removing unique elements from page 1")
        elif currentPage == 2:
            #
            self.imgLabel.setVisible(False)
            print("Removing unique elements from page 2")
        elif currentPage == 3:
            #
            print("Removing unique elements from page 3")
        elif currentPage == 4:
            #
            print("Removing unique elements from page 4")
        elif currentPage == 5:
            #
            print("Removing unique elements from page 5")
        elif currentPage == 6:
            #
            print("Removing unique elements from page 6")
        elif currentPage == 7:
            #
            print("Removing unique elements from page 7")
            

    def show_next_page(self):
        currentPage = int(self.label.text().split()[1])
        self.show_page(currentPage + 1)
        
        # Hide elements unique to the current page
        if currentPage == 1:
            #
            self.p1textbox.setVisible(False)
            print("Removing unique elements from page 1")
        elif currentPage == 2:
            #
            self.imgLabel.setVisible(False)
            print("Removing unique elements from page 2")
        elif currentPage == 3:
            #
            print("Removing unique elements from page 3")
        elif currentPage == 4:
            #
            print("Removing unique elements from page 4")
        elif currentPage == 5:
            #
            print("Removing unique elements from page 5")
        elif currentPage == 6:
            #
            print("Removing unique elements from page 6")
        elif currentPage == 7:
            #
            print("Removing unique elements from page 7")

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.setGeometry(100, 100, 1024, 768)
main_window.show()
sys.exit(app.exec_())
