from PyQt6 import QtWidgets
from ttp_assistant.Library.utils import load_solution_from_memory
from ttp_assistant.helpers.example_data import examples


class ExampleSelectionDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ExampleSelectionDialog, self).__init__(parent)
        self.setWindowTitle("Select an Example")
        screen_size = QtWidgets.QApplication.primaryScreen().size()
        dialog_width = int(screen_size.width() * 0.50)  # 50% of the screen width
        dialog_height = int(screen_size.height() * 0.50)  # Optionally set the height to 50% as well
        self.resize(dialog_width, dialog_height)
        # Create a layout for the dialog
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create a QTableWidget to list the examples
        self.table_widget = QtWidgets.QTableWidget(self)
        self.table_widget.setRowCount(len(examples))
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Example", "Description"])
        self.table_widget.horizontalHeader().setStretchLastSection(True)  # Stretch description column

        # Populate the table with example data
        for row, (example_name, example_data) in enumerate(examples.items()):
            # Accessing the description from each example
            description = example_data.get("description", "No description available")

            self.table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(example_name))
            self.table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(description))


        self.layout.addWidget(self.table_widget)
        # Adjust the column width as a percentage of the table width
        dialog_width = self.size().width()  # Get the current dialog width
        self.table_widget.setColumnWidth(0, int(dialog_width * 0.30))  # Set first column to 30%
        self.table_widget.horizontalHeader().setStretchLastSection(True)  # Stretch the second column

        # Add OK and Cancel buttons
        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def get_selected_example(self):
        """Return the selected example's key from the examples dict."""
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            example_name = self.table_widget.item(selected_row, 0).text()
            return example_name
        return None

# Usage Example
def open_example_dialog(parent_ref):
    dialog = ExampleSelectionDialog()
    if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
        selected_example = dialog.get_selected_example()
        if selected_example:
            print(f"Selected Example: {selected_example}")
            # Now load the example data (e.g., call load_solution_from_yaml)
            example_data = examples[selected_example]
            load_solution_from_memory(parent_ref, example_data)
