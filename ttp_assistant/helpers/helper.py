import json
import jmespath
import yaml
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTextEdit
from jinja2 import Template
from ttp import ttp


def clear(self):
    """Clear the source, template, result, and reset variable highlights."""
    # Clear the text areas (Source, Template, Result)
    self.teResult.clear()      # Clear the result area
    self.teSource.clear()      # Clear the source area
    self.teTemplate.clear()    # Clear the template area

    # Reset the variable state by clearing highlighted ranges
    self.teSource.highlighted_ranges = []  # Clear variable highlights

    # Update highlights in the editor
    self.teSource.update_highlights()  # Clear existing highlights

    # Reset the template after clearing
    self.update_ttp_assisted_template()

    # Reapply syntax highlighting after clearing
    self.reassign_highlighters()


def notify(self, message, info):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg.setText(info)
    msg.setWindowTitle(message)
    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    retval = msg.exec()

class PlainTextOnlyTextEdit(QTextEdit):
    def insertFromMimeData(self, mime_data):
        # Get the plain text from mime_data and insert it.
        plain_text = mime_data.text()
        self.textCursor().insertText(plain_text)

def render_jpath(self):
    parsed_output = ""
    try:
        parsed_output = json.loads(self.teSource.toPlainText())  # Load into dictionary
    except Exception as e:
        self.teResult.setText(f"Error loading json source")

    jp_qry = self.teTemplate.toPlainText()  # example query
    outputdict = {}
    try:
        outputdict = jmespath.search(jp_qry, parsed_output)  # run the query, output is a dictionary
        result = json.dumps(outputdict, indent=2)  # Strip the outer list object
        self.teResult.setText(result)
    except Exception as e:
        self.teResult.setText(f"Error Rendering JMesPath: {e}")

def render_jinja(self):
    try:
        config_dict = yaml.safe_load(self.teSource.toPlainText())
        template_text = self.teTemplate.toPlainText()
        jinja_template = Template(template_text)

        result = jinja_template.render(config_dict)
        self.teResult.setPlainText(result)
    except yaml.parser.ParserError as err:
        self.teResult.setPlainText(f"YAML Error: Parsing Error: {err}")
    except Exception as e:
        self.teResult.setPlainText(str(e))

def render_ttp(self):
    data_to_parse = self.teSource.toPlainText()
    ttp_template = self.teTemplate.toPlainText()

    try:
        parser = ttp(data=data_to_parse, template=ttp_template)
        parser.parse()
        result = parser.result(format='json')[0]
        self.teResult.setPlainText(result)

    except Exception as e:
        if "index out of range" in str(e):
            e = str(e) + " ... No Data?"
        self.teResult.setPlainText(f"Error Parsing Via TTP: {e}")

def render_event(self, mode):
        if mode == "Mode":
            self.notify("Select Mode", "Please select a mode first ... TTP, Jinja etc")
            return
        if mode == "TTP":
            render_ttp(self)
        elif mode == "Jinja2":
            render_jinja(self)
        elif mode == "JMesPath":
            render_jpath(self)
        elif mode == "TTP Assisted":
            # Do nothing; rendering is on-the-fly
            pass