from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the layout for the introductory page contents

        # Intro page button
        self.buttonGetStarted = QPushButton("Get Started", self)
        self.buttonGetStarted.move(463,650)
        self.buttonGetStarted.clicked.connect(self.show_first_page)

        # Intro page window title
        self.setWindowTitle("Image Analysis v1.0")
        
        # Intro page title banner
        self.introBanner = QLabel('Image Analysis v1.0', self)
        self.introBanner.setAlignment(Qt.AlignCenter)
        self.introBanner.setFont(QFont('Arial', 36))
        self.introBanner.move(110,30)
        self.introBanner.setFixedSize(800,100)
        
        # Intro page flavor text
        self.introText = QLabel('This program is designed to teach you the fundamentals of artificial intelligence and machine learning. '
                                  + 'It will provide a crash course on their applications to image analysis, including topics '
                                  + 'such as convolution and image segmentation.\n\n'
                                  + 'Click Get Started for a quick walkthrough on how artificial intelligence can be used to analyze '
                                  + 'images of handwriting.', self)
        self.introText.setAlignment(Qt.AlignCenter)
        self.introText.setFont(QFont('Arial', 16))
        self.introText.setWordWrap(True)
        self.introText.move(110,150)
        self.introText.setFixedSize(800,200)
        
        # Intro page image
        script_dir = os.path.dirname(os.path.abspath(__file__))
        introImagePath = os.path.join(script_dir, "img", "intro.jpg")
        introImage = QPixmap(introImagePath)
        if introImage.isNull():
            print("Failed to load image file")
        self.introImageLabel = QLabel(self)
        self.introImageLabel.setPixmap(introImage)
        self.introImageLabel.move(300,340)
        self.introImageLabel.setFixedSize(454,300)
        self.introImageLabel.setAlignment(Qt.AlignCenter)

    # Show the first page of the presentation portion of the application
    def show_first_page(self):
        # Remove the Get Started button
        self.buttonGetStarted.deleteLater()
        self.introText.deleteLater()
        self.introBanner.deleteLater()
        self.introImageLabel.deleteLater()

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

    # Used to navigate between pages of the presentation portion of the application
    def show_page(self, pageNumber):
        
        # Set content of the window based on page number
        if pageNumber == 1:
            # Page Contents: Source Image
            
            # Keep track of current page
            # This label is analyzed by show_page to set visible elements for each page of the presentation and update the title bar.
            self.label.setText("Page 1")
            self.label.setVisible(False)
            
            # Page 1 Unique Elements
            # Page 1 Title Banner
            self.page1Banner = QLabel('Source Image', self)
            self.page1Banner.setAlignment(Qt.AlignCenter)
            self.page1Banner.setFont(QFont('Arial', 36))
            self.page1Banner.move(110,30)
            self.page1Banner.setFixedSize(800,100)
            
            # Page 1 Description
            self.page1Description = QLabel('Converting handwritten text to digital characters is no simple process. '
                                        + 'Even focusing purely on the Latin alphabet used in English, the same character '
                                        + 'may be written slightly different from person to person, or even within the same person. '
                                        + 'An efficient machine learning model should be trained on a large data set (collection of images) '
                                        + 'in order to account for these variations. \n\nHowever, images are often not perfectly clear, '
                                        + 'featuring compression artifacts and noise that makes interpretation more difficult. \n\n'
                                        + 'This image has been edited to highlight such artifacts.', self)
            self.page1Description.setAlignment(Qt.AlignLeft)
            self.page1Description.setFont(QFont('Arial', 14))
            self.page1Description.setWordWrap(True)
            self.page1Description.move(110,150)
            self.page1Description.setFixedSize(800,250)

            # Page 1 Image
            script_dir = os.path.dirname(os.path.abspath(__file__))
            page1ImagePath = os.path.join(script_dir, "img", "word-high-contrast.png")
            page1Image = QPixmap(page1ImagePath)
            if page1Image.isNull():
                print("Failed to load image file")
            self.page1ImageLabel = QLabel(self)
            self.page1ImageLabel.setPixmap(page1Image)
            self.page1ImageLabel.move(110,380)
            self.page1ImageLabel.setFixedSize(400,299)
            self.page1ImageLabel.setAlignment(Qt.AlignCenter)
            
            # Show elements unique to Page 1
            self.page1Banner.setVisible(True)
            self.page1Description.setVisible(True)
            self.page1ImageLabel.setVisible(True)
            
            # Note: for proper functionality when navigating pages, we need to modify show_previous_page and show_next_page
            # Both functions check the current page, simply add a line for all elements unique to this page like so:
            # [element].setVisible(False)
            
        elif pageNumber == 2:
            # Page Contents: Dataset
            self.label.setText("Page 2")
            
            # Page 2 Unique Elements
            # Page 2 Title Banner
            self.page2Banner = QLabel('Dataset', self)
            self.page2Banner.setAlignment(Qt.AlignCenter)
            self.page2Banner.setFont(QFont('Arial', 36))
            self.page2Banner.move(110,30)
            self.page2Banner.setFixedSize(800,100)
            
            # Page 2 Description
            self.page2Description = QLabel('A handwriting dataset ideally has thousands of examples of handwriting images '
                                           + 'and the corresponding letters. With the right algorithms (convolution), we can '
                                           + 'find the patterns that make each letter unique.\n\nWe are using the '
                                           + 'IAM Handwriting dataset which contains 115,320 isolated and labeled words.', self)
            self.page2Description.setAlignment(Qt.AlignLeft)
            self.page2Description.setFont(QFont('Arial', 14))
            self.page2Description.setWordWrap(True)
            self.page2Description.move(110,150)
            self.page2Description.setFixedSize(800,250)
            
            # Page 2 Image
            script_dir = os.path.dirname(os.path.abspath(__file__))
            page2ImagePath = os.path.join(script_dir, "img", "dataset.jpg")
            page2Image = QPixmap(page2ImagePath)
            if page2Image.isNull():
                print("Failed to load image file")
            self.page2ImageLabel = QLabel(self)
            self.page2ImageLabel.setPixmap(page2Image)
            self.page2ImageLabel.move(200,330)
            self.page2ImageLabel.setFixedSize(600,240)
            self.page2ImageLabel.setAlignment(Qt.AlignCenter)
            
            # Show elements unique to Page 2
            self.page2Banner.setVisible(True)
            self.page2Description.setVisible(True)
            self.page2ImageLabel.setVisible(True)
            
            #self.imgLabel.setVisible(True)
            
        elif pageNumber == 3:
            # Page Contents: Convolution
            self.label.setText("Page 3")
            
            # Page 3 Unique Elements
            # Page 3 Title Banner
            # Page 3 Description
            # Page 3 Images
            
            # Show elements unique to Page 3
            #self.imgLabel.setVisible(True)
            
        elif pageNumber == 4:
            # Page Contents: Neural Network
            self.label.setText("Page 4")
            
            # Page 4 Unique Elements
            # Page 4 Title Banner
            self.page4Banner = QLabel('Neural Network', self)
            self.page4Banner.setAlignment(Qt.AlignCenter)
            self.page4Banner.setFont(QFont('Arial', 36))
            self.page4Banner.move(110,30)
            self.page4Banner.setFixedSize(800,100)
            
            # Page 4 Description
            
            # Page 4 Image(s)
            
            # Show elements unique to Page 3
            self.page4Banner.setVisible(True)
            
        elif pageNumber == 5:
            # Page Contents: Upload an image
            self.label.setText("Page 5")
            
            # set as new last page!
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
            self.page1Banner.setVisible(False)
            self.page1Description.setVisible(False)
            self.page1ImageLabel.setVisible(False)
            print("Removing unique elements from page 1")
        elif currentPage == 2:
            #
            self.page2Banner.setVisible(False)
            self.page2Description.setVisible(False)
            self.page2ImageLabel.setVisible(False)
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
            self.page1Banner.setVisible(False)
            self.page1Description.setVisible(False)
            self.page1ImageLabel.setVisible(False)
            print("Removing unique elements from page 1")
        elif currentPage == 2:
            #
            self.page2Banner.setVisible(False)
            self.page2Description.setVisible(False)
            self.page2ImageLabel.setVisible(False)
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
