import os
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QSplitter, QDialog, QFileDialog, QStatusBar, QMenuBar,  QMessageBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QKeySequence, QAction
from ttp_assistant.Library.editor import Editor
from ttp_assistant.qtwincon_widget import Ui_Terminal


class AceEditorTerminalDialog(QDialog):
    def __init__(self, parent=None):
        super(AceEditorTerminalDialog, self).__init__(parent)
        self.setWindowTitle("Editor with Terminal")
        self.resize(900, 600)

        # Layout setup
        self.main_layout = QVBoxLayout(self)
        self.setup_menu()

        # Splitter to divide the Ace editor and terminal
        self.splitter = QSplitter(Qt.Orientation.Vertical)
        self.main_layout.addWidget(self.splitter)

        # Add the Ace Editor
        self.ace_editor_widget = Editor(self)
        self.ace_editor_widget.setMinimumSize(QSize(0, 300))
        self.splitter.addWidget(self.ace_editor_widget)

        # Add the Terminal widget
        self.terminal_widget = Ui_Terminal()
        self.terminal_widget.setMinimumSize(QSize(0, 150))
        self.splitter.addWidget(self.terminal_widget)

        # Add status bar
        self.statusbar = QStatusBar(self)
        self.main_layout.addWidget(self.statusbar)

        # File handling
        self.file_to_open = None

    def setup_menu(self):
        """Sets up the menu bar and actions."""
        self.menuBar = QMenuBar(self)
        self.main_layout.addWidget(self.menuBar)

        # File menu
        self.file_menu = self.menuBar.addMenu("File")

        self.new_action = QAction(QIcon("icons/new.png"), "New", self)
        self.new_action.setShortcut(QKeySequence.StandardKey.New)
        self.new_action.triggered.connect(self.new_file)
        self.file_menu.addAction(self.new_action)

        self.open_action = QAction(QIcon("icons/open.png"), "Open", self)
        self.open_action.setShortcut(QKeySequence.StandardKey.Open)
        self.open_action.triggered.connect(self.open_file)
        self.file_menu.addAction(self.open_action)

        self.save_action = QAction(QIcon("icons/save.png"), "Save", self)
        self.save_action.setShortcut(QKeySequence.StandardKey.Save)
        self.save_action.triggered.connect(self.save_file)
        self.file_menu.addAction(self.save_action)

        self.save_as_action = QAction(QIcon("icons/saveas.png"), "Save As...", self)
        self.save_as_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        self.save_as_action.triggered.connect(self.save_file_as)
        self.file_menu.addAction(self.save_as_action)

        self.exit_action = QAction(QIcon("icons/exit.png"), "Exit", self)
        self.exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)

        # Code menu
        self.code_menu = self.menuBar.addMenu("Code")

        self.run_action = QAction("Run", self)
        self.run_action.setShortcut(QKeySequence("Ctrl+R"))
        self.run_action.triggered.connect(self.run_code)
        self.code_menu.addAction(self.run_action)

    def new_file(self):
        """Create a new empty file in the editor."""
        self.ace_editor_widget.page().runJavaScript("editor.setValue('');")
        self.file_to_open = None
        self.statusbar.showMessage("New File")

    def open_file(self):
        """Open an existing file in the editor."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            self.ace_editor_widget.loadFile(file_path)
            self.file_to_open = file_path
            self.statusbar.showMessage(f"Opened {file_path}")

    def save_file(self):
        """Save the current file."""
        if self.file_to_open:
            self.ace_editor_widget.page().runJavaScript("editor.getValue();", self.handle_save_result(self.file_to_open))
        else:
            self.save_file_as()

    def save_file_as(self):
        """Save the current file with a new name."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save As", "", "All Files (*)")
        if file_path:
            self.file_to_open = file_path
            self.ace_editor_widget.page().runJavaScript("editor.getValue();", self.handle_save_result(file_path))

    def handle_save_result(self, file_path):
        """Handle the save result from the JavaScript editor."""
        def callback(result):
            if result:
                try:
                    with open(file_path, 'w') as file:
                        file.write(result)
                    self.statusbar.showMessage(f"Saved {file_path}")
                except Exception as e:
                    self.show_error(f"Error saving file: {str(e)}")

        return callback

    def run_code(self):
        """Run the current script in the terminal."""
        if not self.file_to_open:
            self.show_error("No file to run. Please save the file first.")
            return

        full_path = os.path.abspath(self.file_to_open)
        _, extension = os.path.splitext(full_path)

        # Determine the correct interpreter based on file extension
        if extension == ".py":
            self.terminal_widget.backend.write_data(f"{sys.executable} -u {full_path}\r\n")
        elif extension == ".bat":
            self.terminal_widget.backend.write_data(f"{full_path}\r\n")
        elif extension == ".ps1":
            self.terminal_widget.backend.write_data(f"powershell -File {full_path}\r\n")
        else:
            self.show_error(f"Unsupported file type: {extension}")

    def show_error(self, message):
        """Show an error message box."""
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = AceEditorTerminalDialog()
    dialog.show()
    sys.exit(app.exec())
