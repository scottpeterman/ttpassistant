import json

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMessageBox

from ttp_assistant.dialogs.about import AboutDialog
from ttp_assistant.dialogs.examples_dialog import ExampleSelectionDialog, open_example_dialog
from ttp_assistant.dialogs.table_dialog import TableDialog
from ttp_assistant.dialogs.tassist_dialog import create_variable_dialog, get_default_value_dialog
from ttp_assistant.helpers.example_ttp import examples
from ttp_assistant.helpers.parser_examples import p_examples
from ttp import ttp
from ttp_assistant.helpers.HighlighterTEWidget import SyntaxHighlighter
from ttp_assistant.helpers.helper import PlainTextOnlyTextEdit, clear
from ttp_assistant.Library.customTE import VariableTextEdit
from ttp_assistant.Library.utils import  create_variable, generate_ttp_assisted_template
from ttp_assistant.Library.utils import save_solution_to_yaml, load_solution_from_yaml  # Save/Load utilities
from ttp_assistant.dialogs.runner_dialog import RunnerDialog


class TTPAssistedParsingWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TTPAssistedParsingWidget, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.resize(1000, 600)
        self.setObjectName("parsers")

        # Main vertical layout (parent)
        self.mainLayout = QtWidgets.QVBoxLayout(self)

        # Splitter for proportional resizing between the left and right sections
        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.mainLayout.addWidget(self.splitter)

        # Left side: Source and Template within a vertical layout
        self.left_widget = QtWidgets.QWidget(self.splitter)
        self.left_layout = QtWidgets.QVBoxLayout(self.left_widget)
        self.left_layout.setContentsMargins(5, 5, 5, 5)  # Add padding

        # Grouping the Text Source and Template in a QGroupBox
        self.source_group = QtWidgets.QGroupBox("Text Source", self.left_widget)
        self.source_layout = QtWidgets.QVBoxLayout(self.source_group)
        self.teSource = VariableTextEdit(self.source_group)
        self.teSource.setObjectName("teSource")
        self.source_layout.addWidget(self.teSource)
        self.left_layout.addWidget(self.source_group)

        self.template_group = QtWidgets.QGroupBox("TTP Template", self.left_widget)
        self.template_layout = QtWidgets.QVBoxLayout(self.template_group)
        self.teTemplate = PlainTextOnlyTextEdit(self.template_group)
        self.teTemplate.setObjectName("teTemplate")
        self.teTemplate.setReadOnly(True)
        self.template_layout.addWidget(self.teTemplate)
        self.left_layout.addWidget(self.template_group)

        # Right side: JSON Result
        self.right_widget = QtWidgets.QWidget(self.splitter)
        self.right_layout = QtWidgets.QVBoxLayout(self.right_widget)
        self.right_layout.setContentsMargins(5, 5, 5, 5)  # Add padding

        # JSON Result Group Box
        self.result_group = QtWidgets.QGroupBox("JSON Result", self.right_widget)
        self.result_layout = QtWidgets.QVBoxLayout(self.result_group)
        self.teResult = QtWidgets.QTextEdit(self.result_group)
        self.teResult.setObjectName("teResult")
        self.result_layout.addWidget(self.teResult)
        self.right_layout.addWidget(self.result_group)

        # Highlighters for the text boxes
        self.source_highlighter = SyntaxHighlighter(self.teSource.document())
        self.template_highlighter = SyntaxHighlighter(self.teTemplate.document())
        self.result_highlighter = SyntaxHighlighter(self.teResult.document())

        # Install event filter for mouse move events
        self.teSource.installEventFilter(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # Set up the context menu for creating variables
        self.teSource.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.teSource.customContextMenuRequested.connect(self.show_context_menu)
        self.reassign_highlighters()

        # Buttons at the bottom (Example, Clear, Save, Load, Edit, Run, Table)
        self.buttons_layout = QtWidgets.QHBoxLayout()

        # Example Button
        self.pbExample = QtWidgets.QPushButton("Example", self)
        self.pbExample.setStyleSheet("background-color: #4682B4; color: white; border-radius: 5px;")
        self.pbExample.clicked.connect(self.loadExample)
        self.buttons_layout.addWidget(self.pbExample)

        # Clear Button
        self.pbClear = QtWidgets.QPushButton("Clear", self)
        self.pbClear.setStyleSheet("background-color: #8B6508; color: white; border-radius: 5px;")
        self.pbClear.clicked.connect(lambda: clear(self))
        self.buttons_layout.addWidget(self.pbClear)

        # Save Button
        self.pbSave = QtWidgets.QPushButton("Save", self)
        self.pbSave.setStyleSheet("background-color: #4682B4; color: white; border-radius: 5px;")
        self.pbSave.clicked.connect(lambda: save_solution_to_yaml(self))  # Use utility
        self.buttons_layout.addWidget(self.pbSave)

        # Load Button
        self.pbLoad = QtWidgets.QPushButton("Load", self)
        self.pbLoad.setStyleSheet("background-color: #4682B4; color: white; border-radius: 5px;")
        self.pbLoad.clicked.connect(lambda: load_solution_from_yaml(self))  # Use utility
        self.buttons_layout.addWidget(self.pbLoad)

        # Placeholder Buttons: Edit, Run, Table with different colors


        self.pbRun = QtWidgets.QPushButton("Run", self)
        self.pbRun.setStyleSheet("background-color: #32CD32; color: white; border-radius: 5px;")  # LimeGreen color
        self.pbRun.clicked.connect(self.create_runner_dialog)

        self.buttons_layout.addWidget(self.pbRun)

        self.pbTable = QtWidgets.QPushButton("Table", self)
        self.pbTable.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")  # DodgerBlue color
        self.pbTable.clicked.connect(self.loadTable)
        self.buttons_layout.addWidget(self.pbTable)

        self.pbAbout = QtWidgets.QPushButton("About", self)
        self.pbAbout.setStyleSheet("background-color: #aa42f5; color: white; border-radius: 5px;")  # Tomato color

        self.pbAbout.clicked.connect(self.showAbout)

        self.buttons_layout.addWidget(self.pbAbout)

        # Add buttons layout below the splitter
        self.mainLayout.addLayout(self.buttons_layout)

        # Additional Highlighters reassignment and setup
        self.reassign_highlighters()

    def showAbout(self):
        adialog = AboutDialog(self)
        adialog.exec()
    def show_context_menu(self, position):
        """Display the custom context menu when text is highlighted."""
        cursor = self.teSource.textCursor()
        if cursor.hasSelection():
            menu = QtWidgets.QMenu(self)
            create_var_action = QtGui.QAction("Create Variable", self)
            create_var_action.triggered.connect(self.create_variable_dialog)
            menu.addAction(create_var_action)
            menu.exec(self.teSource.viewport().mapToGlobal(position))


    def create_runner_dialog(self):
        # Pass the current TTP template to the RunnerDialog
        current_template = self.teTemplate.toPlainText()

        # Create the RunnerDialog with the current TTP template
        dialog = RunnerDialog(self, ttp_template=current_template)

        # Execute the dialog (this will open it)
        dialog.exec()

    def eventFilter(self, obj, event):
        if obj == self.teSource:
            # Debugging output for the event type
            # print(f"\nEvent type: {event.type()}", flush=True)

            # Handle right-click events
            if event.type() == QtCore.QEvent.Type.MouseButtonPress and event.button() == QtCore.Qt.MouseButton.RightButton:
                # Check if there is user-selected text first
                cursor = self.teSource.textCursor()

                # Step 1: Check for user-selected text first
                if cursor.hasSelection():
                    print("User selected text detected", flush=True)
                    # Fix: Use globalPosition() instead of globalPos()
                    self.show_create_variable_context_menu(event.globalPosition().toPoint())
                    return True  # Event handled (stop further processing)

                # Step 2: If no user-selected text, check for predefined variables
                cursor_pos = self.teSource.cursorForPosition(event.pos())
                variable = self.get_variable_at_cursor(cursor_pos)
                if variable:
                    print(f"Predefined variable detected: {variable}", flush=True)
                    # Fix: Use globalPosition() instead of globalPos()
                    self.show_delete_context_menu(event.globalPosition().toPoint(), variable)
                    return True  # Event handled

                print("No Variable Found and no text selected", flush=True)

        return super().eventFilter(obj, event)

    def show_create_variable_context_menu(self, position):
        """Display the context menu for creating a variable when user-selected text is right-clicked."""
        print("Showing Create Variable context menu", flush=True)

        menu = QtWidgets.QMenu(self)
        create_var_action = QtGui.QAction("Create Variable", self)
        create_var_action.triggered.connect(lambda: create_variable_dialog(self, parent=self))
        menu.addAction(create_var_action)
        menu.exec(position)

    def show_delete_context_menu(self, position, variable):
        """Display a context menu for deleting the selected variable."""
        print(f"Showing Delete Variable context menu for variable: {variable}", flush=True)

        menu = QtWidgets.QMenu(self)
        delete_action = QtGui.QAction("Delete Variable", self)
        delete_action.triggered.connect(lambda: self.delete_variable(variable))
        menu.addAction(delete_action)
        menu.exec(position)

    def get_variable_at_cursor(self, cursor):
        """Check if the current cursor position overlaps with any predefined variable."""
        cursor_pos = cursor.position()

        # Debugging output for cursor position
        print(f"Checking cursor position: {cursor_pos} for variables", flush=True)

        # Iterate over predefined variables in highlighted_ranges
        for var in self.teSource.highlighted_ranges:
            if var['start'] <= cursor_pos <= var['end']:
                print(f"Cursor over variable: {var}", flush=True)
                return var  # Return the variable that the cursor is over

        # No predefined variable found
        print("Cursor not in any variable range", flush=True)
        return None

    def delete_variable(self, variable):
        """Delete the variable from the highlighted ranges and update the template."""
        print("Deleting Variable")
        # Remove the variable from the highlighted_ranges
        self.teSource.highlighted_ranges = [
            var for var in self.teSource.highlighted_ranges if var != variable
        ]

        # Debugging output for after deletion
        print(f"Variable deleted. Updated highlights: {self.teSource.highlighted_ranges}", flush=True)

        # Update highlights in the editor and regenerate the template
        self.teSource.update_highlights()
        self.update_ttp_assisted_template()

    def loadExample(self):
        """Open a dialog to let the user select an example, then load it."""
        # Clear any existing variable information to avoid state corruption
        self.teSource.highlighted_ranges = []  # Clear the variable ranges
        self.teSource.update_highlights()  # Clear existing highlights
        self.teTemplate.clear()  # Clear the TTP template

        # Reset template after clearing
        self.update_ttp_assisted_template()

        # Now proceed with loading the new example
        open_example_dialog(self)
        # Reapply syntax highlighting after example loading
        self.reassign_highlighters()

    def update_syntax_highlighting(self):
        """Update syntax highlighting based on current mode."""
        # Set up different highlighters for different text areas
        self.source_highlighter.set_syntax_type("plain")  # Source in plain mode
        self.template_highlighter.set_syntax_type("jinja")  # Template highlighting as Jinja
        self.result_highlighter.set_syntax_type("json")  # Result highlighting as JSON

    def reassign_highlighters(self):
        """Reinitialize and reassign highlighters to the current widgets."""
        # Create new highlighter instances and attach them to the current QTextDocument
        self.source_highlighter = SyntaxHighlighter(self.teSource.document())
        self.template_highlighter = SyntaxHighlighter(self.teTemplate.document())
        self.result_highlighter = SyntaxHighlighter(self.teResult.document())

        # Update syntax highlighting based on the current mode
        self.update_syntax_highlighting()

    def update_ttp_assisted_template(self):
        template_text = generate_ttp_assisted_template(self)
        self.teTemplate.setPlainText(template_text)
        self.update_ttp_assisted()

    def update_ttp_assisted(self):
        data_to_parse = self.teSource.toPlainText()
        ttp_template = self.teTemplate.toPlainText()

        if not data_to_parse.strip() or not ttp_template.strip():
            self.teResult.clear()
            return

        try:
            parser = ttp(data=data_to_parse, template=ttp_template)
            parser.parse()
            result = parser.result(format='json')[0]
            self.teResult.setPlainText(result)
        except Exception as e:
            self.teResult.setPlainText(f"Error Parsing Via TTP Assisted: {e}")

    def loadTable(self):
        """Attempt to load JSON from teResult and display it in a table."""
        try:
            # Get the content from teResult and try to parse it as JSON
            json_text = self.teResult.toPlainText()
            json_data = json.loads(json_text)

            # Open the table dialog with the parsed data
            dialog = TableDialog(json_data, self)
            dialog.exec()

        except json.JSONDecodeError:
            # Show an error if the data is not valid JSON
            QMessageBox.critical(self, "Error", "The result is not valid JSON.")
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", "Unable to process result data into a table")


def main():
    import sys
    print(f"Debug webengine here: http://127.0.0.1:9222/")
    print("cli python uglyeditor.py --webEngineArgs --remote-debugging-port=9222")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

    dark_palette = QtGui.QPalette()

    dark_palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtCore.Qt.GlobalColor.white)
    dark_palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(35, 35, 35))
    dark_palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, QtCore.Qt.GlobalColor.white)
    dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, QtCore.Qt.GlobalColor.white)
    dark_palette.setColor(QtGui.QPalette.ColorRole.Text, QtCore.Qt.GlobalColor.white)
    dark_palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtCore.Qt.GlobalColor.white)
    dark_palette.setColor(QtGui.QPalette.ColorRole.BrightText, QtCore.Qt.GlobalColor.red)

    app.setPalette(dark_palette)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Visual TTP")

    # Create the parsing widget
    ui = TTPAssistedParsingWidget()
    MainWindow.setCentralWidget(ui)

    # Get screen size to set window to 70% of the screen
    screen = app.primaryScreen()
    screen_size = screen.size()
    screen_width = screen_size.width()
    screen_height = screen_size.height()

    # Set window to 70% of screen size
    window_width = int(screen_width * 0.7)
    window_height = int(screen_height * 0.7)
    MainWindow.resize(window_width, window_height)

    # Center the window on the screen
    qtRectangle = MainWindow.frameGeometry()
    centerPoint = screen.geometry().center()
    qtRectangle.moveCenter(centerPoint)
    MainWindow.move(qtRectangle.topLeft())

    # Set initial splitter sizes: 2/3 for the left side, 1/3 for the right side
    ui.splitter.setStretchFactor(0, 2)  # Left side takes 2 parts
    ui.splitter.setStretchFactor(1, 1)  # Right side takes 1 part

    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()