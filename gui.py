from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import cv2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize fileName as None for later access
        self.fileName = None

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
                                           + 'and the corresponding letters. With the right algorithms (convolution) paired with a neural network, '
                                           + 'we can find the patterns that make each letter unique.\n\nWe are using the '
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
            self.page3Banner = QLabel('Convolution', self)
            self.page3Banner.setAlignment(Qt.AlignCenter)
            self.page3Banner.setFont(QFont('Arial', 36))
            self.page3Banner.move(110,30)
            self.page3Banner.setFixedSize(800,100)
            
            # Page 3 Description
            self.page3Description = QLabel('Think of an image as a matrix of pixels. '
                                           +'Convolution is a mathematical operation; for the purposes of image processing it is taking a '
                                           +'small matrix (called a kernel) and running it across an image, performing a specific operation at '
                                           +'each pixel in the matrix.\n\n'
                                           +'By using various kernels, this process lets us extract specific features (such as edges, corners, '
                                           +'or blobs) from an image, which can be used by a neural network to identify patterns that '
                                           +'distinguish different letters.\n\n'
                                           +'By pairing the information from the IAM Handwriting dataset with a neural network, we can\n'
                                           +'predict what letters and words are present in an image of handwriting.', self)
            self.page3Description.setAlignment(Qt.AlignLeft)
            self.page3Description.setFont(QFont('Arial', 14))
            self.page3Description.setWordWrap(True)
            self.page3Description.move(110,150)
            self.page3Description.setFixedSize(800,250)
            
            # Page 3 Images
            # Edges Animation
            script_dir = os.path.dirname(os.path.abspath(__file__))
            page3Image1Path = os.path.join(script_dir, "img", "convolution.gif")
            page3Movie1 = QMovie(page3Image1Path)
            self.page3Image1Label = QLabel(self)
            self.page3Image1Label.setMovie(page3Movie1)
            page3Movie1.start()
            self.page3Image1Label.move(110, 394)
            self.page3Image1Label.setFixedSize(413, 230)
            self.page3Image1Label.setAlignment(Qt.AlignCenter)
            
            # Equation image
            script_dir = os.path.dirname(os.path.abspath(__file__))
            page3Image2Path = os.path.join(script_dir, "img", "convolution-equation.png")
            page3Image2 = QPixmap(page3Image2Path)
            if page3Image2.isNull():
                print("Failed to load image file")
            self.page3Image2Label = QLabel(self)
            self.page3Image2Label.setPixmap(page3Image2)
            self.page3Image2Label.move(560,394)
            self.page3Image2Label.setFixedSize(248,93)
            self.page3Image2Label.setAlignment(Qt.AlignCenter)
            
            # Grid image
            script_dir = os.path.dirname(os.path.abspath(__file__))
            page3Image3Path = os.path.join(script_dir, "img", "convolution-grid.gif")
            page3Movie2 = QMovie(page3Image3Path)
            self.page3Image3Label = QLabel(self)
            self.page3Image3Label.setMovie(page3Movie2)
            page3Movie2.start()
            self.page3Image3Label.move(650, 496)
            self.page3Image3Label.setFixedSize(128, 128)
            self.page3Image3Label.setAlignment(Qt.AlignCenter)
            
            # Show elements unique to Page 3
            self.page3Banner.setVisible(True)
            self.page3Description.setVisible(True)
            self.page3Image1Label.setVisible(True)
            self.page3Image2Label.setVisible(True)
            self.page3Image3Label.setVisible(True)
            
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
            self.page4Description = QLabel('Neural networks consist of multiple layers of artificial neurons. '
                                           +'These neurons are interconnected by weights. The first layer is the input layer, which receives '
                                           +'the visual data. The subsequent layers are hidden layers, which transform the input data using '
                                           +'non-linear functions. The final layer is the output layer, which produces the result of the network.\n\n'
                                           +'In a convolutional neural network , the input data is convolved with a set of learned filters that '
                                           +'are able to detect local patterns in the data, such as edges and corners. '
                                           +'Computer vision neural networks can be trained using a variety of optimization techniques, such as '
                                           +'stochastic gradient descent, to minimize the error between the predicted output and the true output. '
                                           +'Training a neural network involves adjusting the weights of the neurons through backpropagation, '
                                           +'which calculates the gradient of the error with respect to each weight and adjusts the weights '
                                           +'accordingly. \n\n', self)
            self.page4Description.setAlignment(Qt.AlignLeft)
            self.page4Description.setFont(QFont('Arial', 14))
            self.page4Description.setWordWrap(True)
            self.page4Description.move(110,150)
            self.page4Description.setFixedSize(800,250)
            
            # Page 4 Image(s)
            script_dir = os.path.dirname(os.path.abspath(__file__))
            page4ImagePath = os.path.join(script_dir, "img", "FaintEveryAdder-max-1mb.gif")
            page4Movie = QMovie(page4ImagePath)
            self.page4ImageLabel = QLabel(self)
            self.page4ImageLabel.setMovie(page4Movie)
            page4Movie.start()
            self.page4ImageLabel.move(200,330)
            self.page4ImageLabel.setFixedSize(300,169)
            self.page4ImageLabel.setAlignment(Qt.AlignCenter)

            # Show elements unique to Page 4
            self.page4Banner.setVisible(True)
            self.page4Description.setVisible(True)
            self.page4ImageLabel.setVisible(True)
            
        elif pageNumber == 5:
            # Page Contents: Upload an image
            self.label.setText("Page 5")
            
            # Page 5 Unique Elements
            # Page 5 Banner
            self.page5Banner = QLabel('Upload an Image', self)
            self.page5Banner.setAlignment(Qt.AlignCenter)
            self.page5Banner.setFont(QFont('Arial', 36))
            self.page5Banner.move(110,30)
            self.page5Banner.setFixedSize(800,100)
            
            # Page 5 Description
            self.page5Description = QLabel('Upload your own image of a single letter, and the application will attempt to decipher what '
                                           +'it says.\nPreferred file formats: BMP, JPEG, PNG', self)
            self.page5Description.setAlignment(Qt.AlignLeft)
            self.page5Description.setFont(QFont('Arial', 14))
            self.page5Description.setWordWrap(True)
            self.page5Description.move(110,150)
            self.page5Description.setFixedSize(800,250)
            
            # File picker
            # Couldn't find a good way to integrate this with the external file, reimplemented it
            # Can be an improvement for future revisions
            # I have been using img/test-img.jpg and it has been working fine
            
            # script_dir = os.path.dirname(os.path.abspath(__file__))
            self.filePickerButton = QPushButton('Choose File', self)
            self.filePickerButton.move(453, 365)
            self.filePickerButton.setFixedSize(120, 40)
            self.filePickerButton.clicked.connect(self.open_file_dialog)

            # Show elements unique to Page 5
            self.page5Banner.setVisible(True)
            self.page5Description.setVisible(True)
            self.filePickerButton.setVisible(True)
            
        elif pageNumber == 6:
            # Page Contents: Displays uploaded image with deciphered text
            self.label.setText("Page 6")
            
            # Note: not able to navigate back and forth from page 6; user must restart the program to upload another file.
            # Can be an improvement for future revisions
            
            # Page 6 Unique Elements
            # Page 6 Banner
            self.page6Banner = QLabel('Deciphered Text', self)
            self.page6Banner.setAlignment(Qt.AlignCenter)
            self.page6Banner.setFont(QFont('Arial', 36))
            self.page6Banner.move(110,30)
            self.page6Banner.setFixedSize(800,100)
            
            # Page 6 Image (user image)
            userImage = QPixmap(self.fileName[0])
            # Scale the image in case it's too big for the window
            scaledImage = userImage.scaledToWidth(600, Qt.SmoothTransformation)
            self.userImageLabel = QLabel(self)
            # Set the label size to be the same as the scaled image
            self.userImageLabel.setFixedSize(scaledImage.width(), scaledImage.height())
            self.userImageLabel.setPixmap(scaledImage)
            self.userImageLabel.move(200, 150)
            
            # Show elements unique to Page 6
            self.page6Banner.setVisible(True)
            self.userImageLabel.setVisible(True)
            
            
        #elif pageNumber == 7:
            #self.label.setText("Page 7 (Last Page)")
        
        # Set visibility of navigation buttons
        if pageNumber == 1:
            self.buttonPrevious.setVisible(False)
        else:
            self.buttonPrevious.setVisible(True)
        if pageNumber == 5:
            # File picker page
            self.buttonNext.setVisible(False)
        else:
            self.buttonNext.setVisible(True)
        if pageNumber == 6:
            # This is our last page, only viewable after an image has been uploaded.
            self.buttonPrevious.setVisible(False)
            self.buttonNext.setVisible(False)
            # Hide all elements unique to page 5 (file picker page)
            self.filePickerButton.setVisible(False)
            self.page5Banner.setVisible(False)
            self.page5Description.setVisible(False)
            self.filePickerButton.setVisible(False)

        # Show current page number in window title
        self.setWindowTitle(f"Image Analysis v1.0 - Page {pageNumber}")

    def open_file_dialog(self):
        # Assign the file name of the image to a variable
        self.fileName = QFileDialog.getOpenFileName(self, "Open File", "", "Image files (*.png *.jpg *.bmp);; All Files (*)")

        if self.fileName:
            # Display the name of the file
            self.label.setText(self.fileName[0])
            
            # Load the input image
            img = cv2.imread(self.fileName[0])

            if img is not None:
                # Display the name of the file
                self.label.setText(self.fileName[0])

                # Convert the input image to grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Apply thresholding to convert grayscale to binary image
                # ret,thresh = cv2.threshold(gray, 500, 800,0)

                # Display the binary image
                cv2.imshow("Binary image", gray)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                # Navigate to page 6 to display the image
                self.show_page(6)
            else:
                # Display an error message if the image couldn't be loaded
                QMessageBox.warning(self, "Error", "Could not load image file.")


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
            self.page3Banner.setVisible(False)
            self.page3Description.setVisible(False)
            self.page3Image1Label.setVisible(False)
            self.page3Image2Label.setVisible(False)
            self.page3Image3Label.setVisible(False)
            print("Removing unique elements from page 3")
        elif currentPage == 4:
            #
            self.page4Banner.setVisible(False)
            print("Removing unique elements from page 4")
        elif currentPage == 5:
            #
            self.page5Banner.setVisible(False)
            self.page5Description.setVisible(False)
            self.filePickerButton.setVisible(False)
            print("Removing unique elements from page 5")
        #elif currentPage == 6:
            #
            #print("Removing unique elements from page 6")
        #elif currentPage == 7:
            #
            #print("Removing unique elements from page 7")
            

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
            self.page3Banner.setVisible(False)
            self.page3Description.setVisible(False)
            self.page3Image1Label.setVisible(False)
            self.page3Image2Label.setVisible(False)
            self.page3Image3Label.setVisible(False)
            print("Removing unique elements from page 3")
        elif currentPage == 4:
            #
            self.page4Banner.setVisible(False)
            print("Removing unique elements from page 4")
        elif currentPage == 5:
            #
            self.page5Banner.setVisible(False)
            self.page5Description.setVisible(False)
            self.filePickerButton.setVisible(False)
            print("Removing unique elements from page 5")
        #elif currentPage == 6:
            #
            #print("Removing unique elements from page 6")
        #elif currentPage == 7:
            #
            #print("Removing unique elements from page 7")

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.setGeometry(100, 100, 1024, 768)
main_window.show()
sys.exit(app.exec_())
