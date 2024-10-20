import csv

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog, \
    QMessageBox
import json


class TableDialog(QDialog):
    def __init__(self, json_data, parent=None):
        super(TableDialog, self).__init__(parent)
        self.setWindowTitle("Table View")
        screen_size = QtWidgets.QApplication.primaryScreen().size()
        dialog_width = int(screen_size.width() * 0.50)  # 50% of the screen width
        dialog_height = int(screen_size.height() * 0.50)  # Optionally set the height to 50% as well
        self.resize(dialog_width, dialog_height)
        # Layout setup
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget(self)
        layout.addWidget(self.tableWidget)

        # Export button
        button_layout = QHBoxLayout()
        self.exportButton = QPushButton("Export to CSV", self)
        button_layout.addWidget(self.exportButton)
        layout.addLayout(button_layout)

        # Set layout
        self.setLayout(layout)

        # Connect the export button
        self.exportButton.clicked.connect(self.export_to_csv)

        # Load the JSON data into the table
        self.load_data(json_data)

    def flatten_json(self, data):
        """Recursively flatten lists inside the JSON until we get records."""
        while isinstance(data, list) and len(data) == 1:
            data = data[0]
        return data

    def load_data(self, json_data):
        try:
            # Parse the JSON data (handle the list issue)
            data = self.flatten_json(json_data)

            # Make sure we have a list of records
            if isinstance(data, list) and isinstance(data[0], dict):
                headers = list(data[0].keys())  # Use the keys from the first record as headers
                self.tableWidget.setColumnCount(len(headers))
                self.tableWidget.setHorizontalHeaderLabels(headers)
                self.tableWidget.setRowCount(len(data))

                # Load data into the table
                for row, record in enumerate(data):
                    for col, key in enumerate(headers):
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(record.get(key, ""))))
            else:
                raise ValueError("Invalid data format")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
            self.reject()

    def export_to_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV files (*.csv)")
        if path:
            try:
                with open(path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    # Write the headers
                    headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in
                               range(self.tableWidget.columnCount())]
                    writer.writerow(headers)

                    # Write the data
                    for row in range(self.tableWidget.rowCount()):
                        row_data = [self.tableWidget.item(row, col).text() for col in
                                    range(self.tableWidget.columnCount())]
                        writer.writerow(row_data)

                QMessageBox.information(self, "Success", "Data exported successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export data: {e}")
