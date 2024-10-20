from PyQt6.QtGui import QAction, QColor, QTextCursor, QMouseEvent, QCursor
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QTextEdit, QMenu, QMessageBox, QInputDialog
import sys

class VariableTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.highlighted_ranges = []  # Holds the ranges for variables
        self.setMouseTracking(True)  # Enable mouse tracking to detect hover
        print("Mouse tracking enabled:", self.hasMouseTracking())
        sys.stdout.flush()  # Force the print to show immediately

    def mouseMoveEvent(self, event: QMouseEvent):
        """Handle mouse movement to detect if we're hovering over a variable."""
        cursor = self.cursorForPosition(event.pos())
        selection_start = cursor.position()

        # Debugging output
        # print(f"\nMouse Event at position {event.pos()}", flush=True)
        # print(f"Cursor position: {selection_start}", flush=True)
        # print(f"Number of highlighted ranges: {len(self.highlighted_ranges)}", flush=True)

        # Check if mouse is over any highlighted range
        in_variable = False
        for idx, variable in enumerate(self.highlighted_ranges):
            print(f"Checking range {idx}: {variable['start']} to {variable['end']}", flush=True)
            if variable['start'] <= selection_start <= variable['end']:
                print(f"Cursor IN variable range {idx}!", flush=True)

                # Force cursor to PointingHandCursor
                self.viewport().setCursor(Qt.CursorShape.PointingHandCursor)
                print("Cursor set to PointingHandCursor", flush=True)
                in_variable = True
                break

        if not in_variable:
            print("Cursor not in any variable range", flush=True)
            self.viewport().setCursor(Qt.CursorShape.IBeamCursor)  # Revert back to I-beam when not in variable
            print("Cursor set to IBeamCursor", flush=True)

        # Ensure the event is passed on to other handlers if needed
        super().mouseMoveEvent(event)

    def viewportEvent(self, event):
        """Override viewportEvent to prevent cursor reset."""
        if event.type() == QEvent.Type.MouseMove:
            return QTextEdit.viewportEvent(self, event)
        return super().viewportEvent(event)

    def enterEvent(self, event):
        """Ensure the cursor is set when the mouse enters the widget."""
        print("Mouse entered widget", flush=True)
        super().enterEvent(event)

    def leaveEvent(self, event):
        """Revert the cursor to default when the mouse leaves the widget."""
        print("Mouse left widget", flush=True)
        self.viewport().setCursor(Qt.CursorShape.IBeamCursor)  # Reset cursor when leaving widget
        super().leaveEvent(event)

    def assign_variable(self):
        """Allow users to select text and assign a variable to it."""
        cursor = self.textCursor()
        selected_text = cursor.selectedText()
        if not selected_text:
            QMessageBox.warning(self, "No Selection", "Please select some text to assign a variable.")
            return

        # Get the start and end positions of the selected text
        start = min(cursor.position(), cursor.anchor())
        end = max(cursor.position(), cursor.anchor())
        print(f"Selected text range: {start} to {end}", flush=True)

        # Ask for the variable name
        var_name, ok = QInputDialog.getText(self, "Variable Name", "Enter variable name:")
        if not ok or not var_name.strip():
            return

        # Ask for match type
        match_types = [
            "None", "WORD", "PHRASE", "ORPHRASE", "_line_", "ROW",
            "DIGIT", "IP", "PREFIX", "IPV6", "PREFIXV6", "MAC", "re"
        ]
        match_type, ok = QInputDialog.getItem(
            self, "Select Match Type", "Choose a TTP match variable type:", match_types, 0, False
        )
        if not ok:
            return

        # Add the variable range
        self.highlighted_ranges.append({
            'start': start,
            'end': end,
            'var_name': var_name.strip(),
            'match_types': [match_type.upper() if match_type != "None" else None]
        })

        print(f"Added new variable range: {start} to {end}", flush=True)
        print(f"Current highlighted ranges: {self.highlighted_ranges}", flush=True)

        # Update the highlights in the widget
        self.update_highlights()

    def update_highlights(self):
        """Update the highlighted areas in the text editor."""
        extra_selections = []
        for rng in self.highlighted_ranges:
            selection = QTextEdit.ExtraSelection()
            cursor = self.textCursor()
            cursor.setPosition(rng['start'])
            cursor.setPosition(rng['end'], QTextCursor.MoveMode.KeepAnchor)
            selection.cursor = cursor
            selection.format.setBackground(QColor("#0352fc"))  # Light green background
            extra_selections.append(selection)
        self.setExtraSelections(extra_selections)
        print(f"Updated highlights. Current ranges: {self.highlighted_ranges}")  # Debug print
