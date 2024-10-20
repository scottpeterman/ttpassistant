from pathlib import Path
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextBrowser, QDialogButtonBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About TTP Assistant")
        self.setMinimumSize(400, 500)  # Set a reasonable default size

        # Create the main layout
        layout = QVBoxLayout()

        # Get the absolute path to the current file (where the script is located)
        base_path = Path(__file__).resolve().parent.parent  # Go up one directory from 'dialogs'

        # Construct the path to the splash image
        splash_image_path = base_path / "icons" / "about_python.png"

        # Debug: Print the path to ensure it's correct
        print(f"Image path: {splash_image_path}")
        if not splash_image_path.exists():
            print("Error: Image file not found!")

        # Splash graphic (taking 50% of the vertical space)
        splash_label = QLabel(self)
        splash_pixmap = QPixmap(str(splash_image_path))  # Provide the path to the splash image

        # Scale the image to fit nicely within 50% of the dialog
        scaled_pixmap = splash_pixmap.scaledToHeight(250, Qt.TransformationMode.SmoothTransformation)  # Adjust size

        # Set the scaled pixmap on the QLabel
        splash_label.setPixmap(scaled_pixmap)
        splash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the splash label to the layout
        layout.addWidget(splash_label, stretch=1)  # Set stretch to 1 for equal spacing

        # Text browser for information (taking 50% of the vertical space)
        text_browser = QTextBrowser(self)
        text_browser.setHtml("""
            <h1>TTP Assistant</h1>
            <p><strong>Version:</strong> 0.1.0</p>
            <p><strong>License:</strong> GPLv3</p>
            <p>Visual TTP Assistant is an all-in-one network automation and templating tool designed for network engineers, developers, and automation specialists.</p>
            <p><strong>Features:</strong></p>
            <ul>
                <li>Template-driven parsing</li>
                <li>Live device interaction</li>
                <li>Dynamic code generation and execution</li>
                <li>Integrated editor and terminal</li>
            </ul>
        """)
        layout.addWidget(text_browser, stretch=1)  # Set stretch to 1 for equal spacing

        # Dialog buttons (OK button to close the dialog)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

        # Set the layout for the dialog
        self.setLayout(layout)
