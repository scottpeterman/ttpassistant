from PyQt6 import QtCore, QtGui, QtWidgets

from ttp_assistant.Library.utils import create_variable


def get_default_value_dialog(widget):
    dialog = QtWidgets.QDialog(widget)
    dialog.setWindowTitle("Default Value")

    layout = QtWidgets.QVBoxLayout()

    # Radio buttons for string or number
    string_radio = QtWidgets.QRadioButton("String")
    number_radio = QtWidgets.QRadioButton("Number")
    string_radio.setChecked(True)  # Default to string
    layout.addWidget(string_radio)
    layout.addWidget(number_radio)

    # Input for the default value
    default_value_label = QtWidgets.QLabel("Enter default value:")
    default_value_input = QtWidgets.QLineEdit()  # User can input the value
    layout.addWidget(default_value_label)
    layout.addWidget(default_value_input)

    # OK and Cancel buttons
    button_box = QtWidgets.QDialogButtonBox(
        QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
    layout.addWidget(button_box)

    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    dialog.setLayout(layout)

    # Show the dialog and capture the user's input
    if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
        default_value = default_value_input.text()

        # Check if the value is a string or number based on radio selection
        if string_radio.isChecked():
            return f"'{default_value}'"  # Enclose in quotes for string
        else:
            return default_value  # Return as-is for number

    return None  # Return None if dialog is canceled


function_lookup = {
    # Functions that require values
    "default": True,
    "contains_re": True,
    "startswith_re": True,
    "endswith_re": True,
    "exclude_re": True,
    "exclude": True,
    "dns": True,
    "rdns": True,
    "sformat": True,
    "uptimeparse": True,
    "replaceall": True,
    "resub": True,
    "resuball": True,
    "lookup": True,
    "rlookup": True,
    "geoip_lookup": True,
    "gpvlookup": True,
    "greaterthan": True,  # Still require input
    "lessthan": True,  # Still require input
    "equal": True,
    "notequal": True,

    # Functions that do not require values
    "is_ip": False,
    "mac_eui": False,
    "void": False,
    "isdigit": False,
    "notdigit": False,
    "count": False,  # Does not require a value
    "to_int": False,  # No extra input needed, it converts matched data
    "to_float": False,
    "to_ip": False,
    "to_str": False,
    "to_list": False,
    "to_net": False,
    "to_cidr": False
}


def get_function_value_dialog(widget, function_name):
    dialog = QtWidgets.QDialog(widget)
    dialog.setWindowTitle(f"Function Value for {function_name}")

    layout = QtWidgets.QVBoxLayout()

    # Radio buttons for string or number selection (similar to the old default dialog)
    data_type_label = QtWidgets.QLabel("Select Data Type:")
    layout.addWidget(data_type_label)

    string_radio = QtWidgets.QRadioButton("String")
    number_radio = QtWidgets.QRadioButton("Number")
    string_radio.setChecked(True)  # Default to string
    layout.addWidget(string_radio)
    layout.addWidget(number_radio)

    # Input field for the function value
    value_label = QtWidgets.QLabel(f"Enter value for {function_name}:")
    value_input = QtWidgets.QLineEdit()
    layout.addWidget(value_label)
    layout.addWidget(value_input)

    # OK and Cancel buttons
    button_box = QtWidgets.QDialogButtonBox(
        QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
    layout.addWidget(button_box)

    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    dialog.setLayout(layout)

    # Show the dialog and capture the user's input
    if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
        function_value = value_input.text().strip()

        # Ensure value is provided
        if not function_value:
            QtWidgets.QMessageBox.warning(widget, "Invalid Input", "Value cannot be empty.")
            return None

        # Determine the data type based on the radio button selection
        if string_radio.isChecked():
            # If it's a string, return the value wrapped in quotes
            return f"'{function_value}'"
        elif number_radio.isChecked():
            # If it's a number, validate that it's a valid number
            try:
                # Try converting the input to a float (or int)
                float(function_value)
                return function_value  # Return the numeric value as-is
            except ValueError:
                # Show an error message if the input is not a valid number
                QtWidgets.QMessageBox.warning(widget, "Invalid Input", "Please enter a valid number.")
                return None

    return None  # Return None if dialog is canceled


def create_variable_dialog(widget, parent):
    widget.parent = parent
    cursor = widget.teSource.textCursor()  # Get the current cursor
    selected_text = cursor.selectedText()  # Get the selected text

    # If no text is selected, provide a default name
    if not selected_text:
        selected_text = "new_var"

    dialog = QtWidgets.QDialog(widget)
    dialog.setWindowTitle("Create Variable")

    layout = QtWidgets.QVBoxLayout()

    # Input for variable name
    var_name_label = QtWidgets.QLabel("Variable Name:")
    var_name_input = QtWidgets.QLineEdit(f"var_{selected_text}")  # Default to "var_<selected_text>"
    layout.addWidget(var_name_label)
    layout.addWidget(var_name_input)

    # Dropdown for filters
    filter_label = QtWidgets.QLabel("Match Filter:")
    filter_combo = QtWidgets.QComboBox()
    match_types = [
        "", "WORD", "PHRASE", "ORPHRASE", "_line_", "ROW",
        "DIGIT", "IP", "PREFIX", "IPV6", "PREFIXV6", "MAC", "re"
    ]
    for item in match_types:
        filter_combo.addItem(item)

    layout.addWidget(filter_label)
    layout.addWidget(filter_combo)

    # Function List - expression builder
    function_label = QtWidgets.QLabel("Functions (in sequence):")
    layout.addWidget(function_label)

    function_list_widget = QtWidgets.QListWidget()
    layout.addWidget(function_list_widget)

    # Add function and remove buttons
    function_buttons_layout = QtWidgets.QHBoxLayout()
    add_function_btn = QtWidgets.QPushButton("Add Function")
    remove_function_btn = QtWidgets.QPushButton("Remove Function")
    up_button = QtWidgets.QPushButton("Move Up")
    down_button = QtWidgets.QPushButton("Move Down")
    function_buttons_layout.addWidget(add_function_btn)
    function_buttons_layout.addWidget(remove_function_btn)
    function_buttons_layout.addWidget(up_button)
    function_buttons_layout.addWidget(down_button)
    layout.addLayout(function_buttons_layout)

    # OK and Cancel buttons
    button_box = QtWidgets.QDialogButtonBox(
        QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
    layout.addWidget(button_box)

    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    dialog.setLayout(layout)

    # Functionality for adding functions
    def add_function():
        function_name, ok = QtWidgets.QInputDialog.getItem(widget, "Select Function",
                                                           "Choose function:", list(function_lookup.keys()), 0, False)
        if ok and function_name:
            if function_lookup[function_name]:
                # If the function requires a value, open the dialog to get the value
                function_value = get_function_value_dialog(widget, function_name)
                if function_value:
                    function_list_widget.addItem(f"{function_name}({function_value})")
            else:
                # If the function does not require a value, just add it with empty parentheses
                function_list_widget.addItem(f"{function_name}()")

    add_function_btn.clicked.connect(add_function)

    # Functionality for removing selected function
    def remove_function():
        current_row = function_list_widget.currentRow()
        if current_row >= 0:
            function_list_widget.takeItem(current_row)

    remove_function_btn.clicked.connect(remove_function)

    # Move up and down
    def move_up():
        current_row = function_list_widget.currentRow()
        if current_row > 0:
            item = function_list_widget.takeItem(current_row)
            function_list_widget.insertItem(current_row - 1, item)
            function_list_widget.setCurrentRow(current_row - 1)

    def move_down():
        current_row = function_list_widget.currentRow()
        if current_row < function_list_widget.count() - 1:
            item = function_list_widget.takeItem(current_row)
            function_list_widget.insertItem(current_row + 1, item)
            function_list_widget.setCurrentRow(current_row + 1)

    up_button.clicked.connect(move_up)
    down_button.clicked.connect(move_down)

    # Show the dialog and capture the selections
    if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
        var_name = var_name_input.text()  # Get the variable name from the input
        var_filter = filter_combo.currentText() if filter_combo.currentText() else None  # Get the selected filter

        # Capture the list of functions in the expression builder
        function_chain = []
        for i in range(function_list_widget.count()):
            function_chain.append(function_list_widget.item(i).text())

        # Proceed with variable creation
        create_variable(widget, var_name, var_filter, " | ".join(function_chain), parent_ref=widget.parent)
