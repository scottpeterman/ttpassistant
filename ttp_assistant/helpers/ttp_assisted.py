from PyQt6 import QtCore, QtWidgets, QtGui

from ttp_assistant.helpers.helper import PlainTextOnlyTextEdit


class HighlightedTextEdit(PlainTextOnlyTextEdit):
    selection_changed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.highlighted_ranges = []

    def show_context_menu(self, pos):
        cursor = self.cursorForPosition(pos)
        if self.textCursor().hasSelection():
            menu = QtWidgets.QMenu(self)
            assign_action = QtGui.QAction("Assign Variable", self)
            assign_action.triggered.connect(self.assign_variable)
            menu.addAction(assign_action)
            menu.exec(self.mapToGlobal(pos))
        else:
            menu = self.createStandardContextMenu()
            menu.exec(self.mapToGlobal(pos))

    def assign_variable(self):
        cursor = self.textCursor()
        selected_text = cursor.selectedText()
        if not selected_text:
            QtWidgets.QMessageBox.warning(self, "No Selection", "Please select some text to assign a variable.")
            return

        # Ask for variable name
        var_name, ok = QtWidgets.QInputDialog.getText(self, "Variable Name", "Enter variable name:")
        if not ok or not var_name.strip():
            return

        # Ask for match variable type
        match_types = [
            "None", "WORD", "PHRASE", "ORPHRASE", "_line_", "ROW",
            "DIGIT", "IP", "PREFIX", "IPV6", "PREFIXV6", "MAC", "re"
        ]
        match_type, ok = QtWidgets.QInputDialog.getItem(
            self, "Select Match Type", "Choose a TTP match variable type:", match_types, 0, False
        )
        if not ok:
            return

        if match_type.lower() == 're':
            regex, ok = QtWidgets.QInputDialog.getText(self, "Enter Regular Expression", "Enter regex for the variable:")
            if not ok or not regex.strip():
                return
            match_type = f're("{regex.strip()}")'
        else:
            match_type = match_type.upper() if match_type != "None" else None

        # Store the variable assignment
        start = min(cursor.position(), cursor.anchor())
        end = max(cursor.position(), cursor.anchor())
        self.highlighted_ranges.append({
            'start': start,
            'end': end,
            'var_name': var_name.strip(),
            'match_type': match_type
        })

        # Update highlights
        self.update_highlights()
        self.selection_changed.emit()

    def update_highlights(self):
        extra_selections = []
        for rng in self.highlighted_ranges:
            selection = QtWidgets.QTextEdit.ExtraSelection()
            cursor = self.textCursor()
            cursor.setPosition(rng['start'])
            cursor.setPosition(rng['end'], QtGui.QTextCursor.MoveMode.KeepAnchor)
            selection.cursor = cursor
            selection.format.setBackground(QtGui.QColor("#C1E1C1"))  # Light green background
            extra_selections.append(selection)
        self.setExtraSelections(extra_selections)

    def clear_highlights(self):
        self.highlighted_ranges = []
        self.setExtraSelections([])
        self.selection_changed.emit()
