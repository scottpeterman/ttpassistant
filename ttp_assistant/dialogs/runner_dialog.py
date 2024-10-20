import base64
import os
import json
import yaml
from PyQt6.QtGui import QPalette, QTextCursor
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QTextEdit, QComboBox, QGroupBox, QFormLayout
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer
from PySSHPass.pysshpass import SSHClientWrapper
from jinja2 import Template
from ttp import ttp
from ttp_assistant.dialogs.about import AboutDialog
from ttp_assistant.ace_and_term import AceEditorTerminalDialog
from ttp_assistant.helpers.HighlighterTEWidget import SyntaxHighlighter
from ttp_assistant.helpers.pycode_examples import simple1


class SSHWorker(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self, host, username, password, commands, prompt, prompt_count):
        super(SSHWorker, self).__init__()
        self.host = host
        self.username = username
        self.password = password
        self.commands = commands
        self.prompt = prompt
        self.prompt_count = prompt_count

    def run(self):
        client = None
        try:
            # Initialize SSHClientWrapper
            client = SSHClientWrapper(
                host=self.host,
                user=self.username,
                password=self.password,
                cmds=self.commands,
                prompt=self.prompt,
                prompt_count=int(self.prompt_count),
                invoke_shell=True,  # Set invoke_shell to True for interactive shell mode
                timeout=15,          # You can adjust the timeout as needed
                delay=0.5            # You can adjust the delay between commands as needed
            )

            # Connect to the SSH client
            client.connect()

            # Run the commands and capture the output
            output = client.run_commands()
            self.output_signal.emit(output)

            # Close the connection
            client.close()

        except Exception as e:
            self.output_signal.emit(f"Error: {e}")
        finally:
            try:
                client.close()
            except:
                pass


class RunnerDialog(QDialog):
    HISTORY_FILE = "ssh_history.yaml"

    def __init__(self, parent=None, ttp_template=None):
        super(RunnerDialog, self).__init__(parent)
        print(f"Parent style: {parent.style().objectName() if parent else 'No parent'}")
        print(f"Dialog style: {self.style().objectName()}")
        print(
            f"Parent palette window color: {parent.palette().color(QPalette.ColorRole.Window).name() if parent else 'No parent'}")
        print(f"Dialog palette window color: {self.palette().color(QPalette.ColorRole.Window).name()}")
        self.history = {}
        self.ensure_history_file_exists()  # Ensure the history file exists
        self.load_history()  # Load the history on startup

        self.setupUi()
        self.populate_combo_boxes()  # Ensure combo boxes are populated with history


        # Set the size of the dialog to 70% of the screen
        screen_geometry = QApplication.primaryScreen().geometry()
        self.resize(screen_geometry.width() * 0.7, screen_geometry.height() * 0.7)

        self.adjust_sizes()  # Initial size adjustment

        # Enable Min/Max/Restore buttons
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowMinMaxButtonsHint)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowCloseButtonHint)
        # Initialize fields with provided template
        if ttp_template:
            self.teTemplate.setText(ttp_template)

        # Connect the Run button
        self.pbRun.clicked.connect(self.run_ssh_commands)



        # Connect the Re-render button
        self.pbRender.setText("Render")
        self.pbRender.clicked.connect(self.render_template)

        # Worker thread for SSH streaming
        self.ssh_worker = None

    def setupUi(self):
        self.setWindowTitle("SSH Runner")
        self.resize(900, 600)

        # Main layout
        self.verticalLayout = QVBoxLayout(self)

        # Create form section using QGroupBox
        self.formSection = QHBoxLayout()

        # Left group for connection details
        self.connectionGroup = QGroupBox("Connection Details")
        connectionLayout = QFormLayout()
        connectionLayout.setSpacing(10)

        # Host input
        self.cbHost = QComboBox()
        self.cbHost.setEditable(True)
        self.cbHost.setMinimumWidth(200)
        connectionLayout.addRow("Host:", self.cbHost)

        # Username input
        self.cbUsername = QComboBox()
        self.cbUsername.setEditable(True)
        connectionLayout.addRow("Username:", self.cbUsername)

        # Password input
        self.lePassword = QLineEdit()
        self.lePassword.setEchoMode(QLineEdit.EchoMode.Password)
        connectionLayout.addRow("Password:", self.lePassword)

        self.connectionGroup.setLayout(connectionLayout)
        self.formSection.addWidget(self.connectionGroup)

        # Right group for command settings
        self.settingsGroup = QGroupBox("Command Settings")
        settingsLayout = QFormLayout()
        settingsLayout.setSpacing(10)

        # PySSHPass Commands
        self.cbPySSHCommands = QComboBox()
        self.cbPySSHCommands.setEditable(True)
        self.cbPySSHCommands.setMinimumWidth(300)
        settingsLayout.addRow("PySSHPass Commands:", self.cbPySSHCommands)

        # Prompt settings
        promptLayout = QHBoxLayout()
        self.cbPrompt = QComboBox()
        self.cbPrompt.setEditable(True)
        promptLayout.addWidget(QLabel("Prompt:"))
        promptLayout.addWidget(self.cbPrompt)

        self.cbPromptCount = QComboBox()
        self.cbPromptCount.setEditable(True)
        promptLayout.addWidget(QLabel("Count:"))
        promptLayout.addWidget(self.cbPromptCount)

        settingsLayout.addRow("", promptLayout)

        # Move Run, Single Device ComboBox, and Generate Code buttons under Prompt/Count
        self.command_buttons_layout = QHBoxLayout()
        self.pbRun = QPushButton("Run")
        self.cbCodeType = QComboBox()
        self.cbCodeType.addItems(["Single Device", "Other Option 1", "Other Option 2"])
        self.pbGenerateCode = QPushButton("Generate Code")

        # Add buttons to the layout
        self.command_buttons_layout.addWidget(self.pbRun)
        self.command_buttons_layout.addWidget(self.cbCodeType)
        self.command_buttons_layout.addWidget(self.pbGenerateCode)

        # Add buttons layout to the settings group below the Prompt/Count
        settingsLayout.addRow("", self.command_buttons_layout)

        self.settingsGroup.setLayout(settingsLayout)
        self.formSection.addWidget(self.settingsGroup)

        # Add form section to main layout
        self.verticalLayout.addLayout(self.formSection)

        # Output window
        self.verticalLayout_10 = QVBoxLayout()
        self.label_7 = QLabel("Output")
        self.teOutput = QTextEdit()
        self.teOutput.setStyleSheet(
            "QTextEdit { color: #00FF00; background-color: black; }")  # Green text, black background
        self.verticalLayout_10.addWidget(self.label_7)
        self.verticalLayout_10.addWidget(self.teOutput)
        self.verticalLayout.addLayout(self.verticalLayout_10)

        # Template and Result (Two text areas side by side)
        self.horizontalLayout_7 = QHBoxLayout()

        # TTP Template
        self.verticalLayout_12 = QVBoxLayout()
        self.label_9 = QLabel("TTP Template")
        self.teTemplate = QTextEdit()
        self.verticalLayout_12.addWidget(self.label_9)
        self.verticalLayout_12.addWidget(self.teTemplate)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        # Result (JSON Result)
        self.verticalLayout_11 = QVBoxLayout()
        self.label_8 = QLabel("Result")
        self.teResult = QTextEdit()
        self.verticalLayout_11.addWidget(self.label_8)
        self.verticalLayout_11.addWidget(self.teResult)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        # Apply syntax highlighting
        self.jinja_highlighter = SyntaxHighlighter(self.teTemplate.document())
        self.jinja_highlighter.set_syntax_type("jinja")  # Jinja for template area

        self.json_highlighter = SyntaxHighlighter(self.teResult.document())
        self.json_highlighter.set_syntax_type("json")  # JSON for result area

        # Render button
        self.horizontalLayout_8 = QHBoxLayout()
        self.pbRender = QPushButton("Re-render")
        self.horizontalLayout_8.addWidget(self.pbRender)
        self.horizontalLayout_8.addStretch()
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        # Connect the "Generate Code" button to its method
        self.pbGenerateCode.clicked.connect(self.generate_code)

    def generate_code(self):
        # Get inputs from the form
        host = self.cbHost.currentText()
        username = self.cbUsername.currentText()
        password = self.lePassword.text()
        pysshcommands = self.cbPySSHCommands.currentText()
        prompt = self.cbPrompt.currentText()
        prompt_count = self.cbPromptCount.currentText()

        # Ensure all fields are populated
        if not host or not username or not password or not pysshcommands or not prompt or not prompt_count:
            QMessageBox.warning(self, "Missing Data", "Please provide all required fields for code generation.")
            return

        # Choose the Jinja template based on the selected code type
        if self.cbCodeType.currentText() == "Single Device":
            template = Template(simple1)  # Load the template from pycode_examples
            # Render the template with the form data
            rendered_code = template.render(
                host=host,
                user=username,
                password=password,
                cmds=pysshcommands,
                prompt=prompt,
                prompt_count=prompt_count
            )

            # Base64 encode the rendered code
            encoded_code = base64.b64encode(rendered_code.encode()).decode()

            # Display the generated code in a new AceEditorTerminalDialog
            code_dialog = AceEditorTerminalDialog(self)
            code_dialog.setWindowTitle("Generated Code")

            # Use QTimer to ensure the JavaScript environment is ready
            def inject_code():
                code_dialog.ace_editor_widget.page().runJavaScript(
                    f"replaceSelectionWithDecodedBase64('{encoded_code}');"
                )

            # Set a short delay (e.g., 100ms) before injecting the code
            QTimer.singleShot(1000, inject_code)

            # Show the dialog
            code_dialog.exec()

        else:
            # Handle other code generation cases (if needed)
            pass

    def adjust_sizes(self):
        """Adjust minimum sizes of the combo boxes based on the window size."""
        window_width = self.width()
        combo_min_width = window_width * 0.20  # Set the combo box width to 15% of window width

        # Set minimum widths for combo boxes
        self.cbHost.setMinimumWidth(combo_min_width)
        self.cbUsername.setMinimumWidth(combo_min_width)
        self.lePassword.setMinimumWidth(combo_min_width)
        self.cbPySSHCommands.setMinimumWidth(window_width * 0.5)  # Set this wider, 50%
        self.cbPrompt.setMinimumWidth(combo_min_width)
        self.cbPromptCount.setMinimumWidth(combo_min_width)

    def resizeEvent(self, event):
        """Handle the window resize event."""
        super().resizeEvent(event)
        self.adjust_sizes()  # Adjust combo box sizes dynamically

    def update_output(self, output):
        # Append the output to the teOutput field
        self.teOutput.append(output)
        self.pbRun.setEnabled(True)
        self.teOutput.moveCursor(QTextCursor.MoveOperation.End)

    def render_template(self):
        # Get the output and template data
        output = self.teOutput.toPlainText()
        template = self.teTemplate.toPlainText()
        if not output or not template:
            QMessageBox.warning(self, "Missing Data", "Both template and output are required for rendering.")
            return

        try:
            parser = ttp(data=output, template=template)
            parser.parse()
            result = parser.result()
            self.teResult.setPlainText(json.dumps(result, indent=2))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to render template: {e}")

    def run_ssh_commands(self):
        self.teOutput.clear()
        self.pbRun.setEnabled(False)

        # Get inputs from the dialog
        host = self.cbHost.currentText()
        username = self.cbUsername.currentText()
        password = self.lePassword.text()
        pysshcommands = self.cbPySSHCommands.currentText()
        prompt = self.cbPrompt.currentText()
        prompt_count = self.cbPromptCount.currentText()

        if not host or not username or not password or not pysshcommands:
            QMessageBox.warning(self, "Missing Data", "Please provide all required fields.")
            return

        # Save the inputs to history (but not the password)
        self.save_history('Host', host)
        self.save_history('Username', username)
        self.save_history('PySSHPass Commands', pysshcommands)
        self.save_history('Prompt', prompt)
        self.save_history('Prompt Count', prompt_count)

        # Start the SSH worker thread
        self.ssh_worker = SSHWorker(host, username, password, pysshcommands, prompt, prompt_count)
        self.ssh_worker.output_signal.connect(self.update_output)
        self.ssh_worker.start()

    def save_history(self, field_name, text):
        """Add the entered text to the combo box's history and persist it."""
        if text not in self.history.get(field_name, []):
            if field_name not in self.history:
                self.history[field_name] = []
            self.history[field_name].insert(0, text)  # Add the new entry at the beginning
            self.history[field_name] = self.history[field_name][:10]  # Keep only the last 10 entries

            self.save_history_to_file()

    def populate_combo_boxes(self):
        print(f"Populating from history...")
        """Populate combo boxes with history from the YAML file."""
        if 'Host' in self.history:
            for item in self.history['Host']:
                self.cbHost.addItem(item)
        if 'Username' in self.history:
            for item in self.history['Username']:
                self.cbUsername.addItem(item)
        if 'PySSHPass Commands' in self.history:
            for item in self.history['PySSHPass Commands']:
                self.cbPySSHCommands.addItem(item)
        if 'Prompt' in self.history:
            for item in self.history['Prompt']:
                self.cbPrompt.addItem(item)
        if 'Prompt Count' in self.history:
            for item in self.history['Prompt Count']:
                self.cbPromptCount.addItem(item)

    def load_history(self):
        """Load history from the YAML file."""
        if os.path.exists(self.HISTORY_FILE):
            with open(self.HISTORY_FILE, 'r') as file:
                self.history = yaml.safe_load(file) or {}

        else:
            self.history = {}

    def save_history_to_file(self):
        """Save the current history to the YAML file."""
        with open(self.HISTORY_FILE, 'w') as file:
            yaml.safe_dump(self.history, file)

    def ensure_history_file_exists(self):
        """Ensure the history file exists and create a template if not."""
        if not os.path.exists(self.HISTORY_FILE):
            # Create an empty template for the first run
            template_history = {
                'Host': [],
                'Username': [],
                'PySSHPass Commands': [],
                'Prompt': [],
                'Prompt Count': []
            }
            with open(self.HISTORY_FILE, 'w') as file:
                yaml.safe_dump(template_history, file)
            print(f"Created template history file at {self.HISTORY_FILE}")
        else:
            print(f"History file exists: {self.HISTORY_FILE}")

