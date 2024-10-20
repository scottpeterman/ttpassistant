import json

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QFileDialog, QInputDialog
import yaml

# Custom representer to handle multiline strings cleanly
class LiteralString(str): pass


def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')


# Add custom representer for LiteralString (multiline strings)
yaml.add_representer(LiteralString, literal_str_representer)


def save_solution_to_yaml(widget):
    """Prompt user for description, file path and save solution to YAML."""
    file_path, _ = QFileDialog.getSaveFileName(widget, "Save Solution", "", "YAML Files (*.yaml)")
    if file_path:
        description, ok = QInputDialog.getText(widget, "Enter Description", "Describe this solution:")
        if ok:
            # Collect the data
            source_text = widget.teSource.toPlainText()
            template = widget.teTemplate.toPlainText()
            result = widget.teResult.toPlainText()

            # Use LiteralString to preserve newlines for source text and template
            source_text_block = LiteralString(source_text)
            template_block = LiteralString(template)

            # Parse the result from JSON string to a Python object (list/dict)
            try:
                result_data = json.loads(result)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                result_data = result  # Fall back to raw result if parsing fails

            # Collect highlighted ranges (variables)
            highlighted_ranges = []
            for var in widget.teSource.highlighted_ranges:
                highlighted_ranges.append({
                    'start': var['start'],
                    'end': var['end'],
                    'var_name': var['var_name'],
                    'filters': var.get('filters', []),
                    'functions': var.get('functions', [])
                })

            # Prepare YAML data
            data = {
                'description': description,
                'source_text': source_text_block,
                'template': template_block,
                'result': result_data,  # Save as structured YAML
                'variables': highlighted_ranges  # Save variable ranges
            }

            # Write the YAML data to the file
            try:
                with open(file_path, 'w') as file:
                    yaml.dump(data, file, default_flow_style=False)
                    print(f"Solution saved to {file_path}")
            except Exception as e:
                print(f"Error saving solution: {e}")


def load_solution_from_yaml(widget):
    """Prompt user to select YAML file and load solution."""
    file_path, _ = QFileDialog.getOpenFileName(widget, "Load Solution", "", "YAML Files (*.yaml)")
    if file_path:
        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)

                # Debugging: Print to ensure data is loaded correctly
                print(f"Loaded Data: {data}")

                # Load the fields directly since there's no templates list
                widget.teSource.setPlainText(data.get('source_text', ''))
                widget.teTemplate.setPlainText(data.get('template', ''))
                widget.teResult.setPlainText(json.dumps(data.get('result', ''), indent=2))  # Pretty print result

                # Re-populate variables (highlighted ranges)
                highlighted_ranges = data.get('variables', [])
                widget.teSource.highlighted_ranges = []  # Clear existing ranges
                for var in highlighted_ranges:
                    widget.teSource.highlighted_ranges.append({
                        'start': var['start'],
                        'end': var['end'],
                        'var_name': var['var_name'],
                        'filters': var.get('filters', []),
                        'functions': var.get('functions', [])
                    })

                # Update highlights in the editor
                widget.teSource.update_highlights()

                print(f"Solution loaded from {file_path}")
        except Exception as e:
            print(f"Error loading solution: {e}")

def load_solution_from_memory(widget, example_data):
    """Load example solution from memory (predefined examples) into the UI."""
    try:
        # Populate the text fields
        widget.teSource.setPlainText(example_data.get('source_text', ''))
        widget.teTemplate.setPlainText(example_data.get('template', ''))
        widget.teResult.setPlainText(json.dumps(example_data.get('result', ''), indent=2))  # Pretty print result

        # Populate the variables (highlighted ranges)
        highlighted_ranges = example_data.get('variables', [])
        widget.teSource.highlighted_ranges = []  # Clear existing ranges
        for var in highlighted_ranges:
            widget.teSource.highlighted_ranges.append({
                'start': var['start'],
                'end': var['end'],
                'var_name': var['var_name'],
                'filters': var.get('filters', []),
                'functions': var.get('functions', [])
            })

        # Update highlights in the editor
        widget.teSource.update_highlights()

        print(f"Example loaded successfully from memory.")

    except Exception as e:
        print(f"Error loading example from memory: {e}")

def create_variable(self, var_name, var_filter=None, var_function=None, parent_ref=None):
    """Create or update a variable with the provided filter and function, with type awareness."""
    cursor = parent_ref.teSource.textCursor()
    start_pos = cursor.selectionStart()  # Get the start position of the selection
    end_pos = cursor.selectionEnd()  # Get the end position of the selection

    # Check if the variable already exists in the highlighted_ranges
    existing_var = next((rng for rng in parent_ref.teSource.highlighted_ranges if rng['var_name'] == var_name), None)

    # Initialize a type tracker
    current_type = 'string'  # Assume we start with a string by default

    if existing_var:
        # If the variable exists, append the new filter and function to the existing lists
        if var_filter:
            existing_var['filters'].append(var_filter)
        if var_function:
            # Track the current type based on the functions
            if 'to_int' in var_function or 'to_float' in var_function:
                current_type = 'numeric'
            existing_var['functions'].append(var_function)
    else:
        # If the variable does not exist, create a new entry with filters and functions as lists
        parent_ref.teSource.highlighted_ranges.append({
            'start': start_pos,
            'end': end_pos,
            'var_name': var_name,
            'filters': [var_filter] if var_filter else [],  # Initialize with filter if provided
            'functions': [var_function] if var_function else [],  # Initialize with function if provided
            'type': current_type  # Track the type (string, int, etc.)
        })

    # Debugging output
    print(f"Updated highlights. Current ranges: {parent_ref.teSource.highlighted_ranges}")

    cursor.clearSelection()  # Deselect the text
    parent_ref.teSource.setTextCursor(cursor)  # Update the cursor in the text editor

    # Update highlights in the editor and regenerate the template
    parent_ref.teSource.update_highlights()
    parent_ref.update_ttp_assisted_template()



def generate_ttp_assisted_template(self):
    sample_text = self.teSource.toPlainText()
    lines = sample_text.splitlines(keepends=True)  # Keep the line endings
    line_positions = []
    current_pos = 0

    # Calculate start and end positions of each line
    for line in lines:
        line_length = len(line)
        line_start = current_pos
        line_end = current_pos + line_length
        line_positions.append({'index': len(line_positions), 'start': line_start, 'end': line_end, 'text': line})
        current_pos += line_length

    # Identify variables for each line
    line_variables = {}
    for rng in self.teSource.highlighted_ranges:
        for line_info in line_positions:
            line_start = line_info['start']
            line_end = line_info['end']
            if rng['start'] >= line_start and rng['end'] <= line_end:
                idx = line_info['index']
                if idx not in line_variables:
                    line_variables[idx] = []
                line_variables[idx].append(rng)
                break

    # Generate the TTP template lines based on highlighted variables
    template_lines = []
    for line_info in line_positions:
        idx = line_info['index']
        line_text = line_info['text']

        # If the line has variables, process it
        if idx in line_variables:
            vars_in_line = line_variables[idx]
            vars_in_line.sort(key=lambda x: x['start'])  # Sort variables by start position
            line_start = line_info['start']
            new_line = ''
            last_pos = line_start

            # Process each variable in the line
            for var in vars_in_line:
                var_start = var['start']
                var_end = var['end']
                rel_start = var_start - line_start
                rel_end = var_end - line_start

                # Add text before the variable
                new_line += line_text[last_pos - line_start:rel_start]

                # Chain filters and functions
                var_string = f"{{{{ {var['var_name']}"  # Correct: Four braces are needed in f-string to produce {{ }}
                if var['filters']:
                    var_string += ' | ' + ' | '.join(var['filters'])
                if var['functions']:
                    var_string += ' | ' + ' | '.join(var['functions'])
                var_string += " }}"  # Three braces are needed to produce two closing braces }}

                # Add the variable string
                new_line += var_string
                last_pos = var_end

            # Add the remaining text after the last variable
            new_line += line_text[last_pos - line_start:]
            template_lines.append(new_line)
        else:
            # Skip lines without variables (to match the original behavior)
            pass

    return ''.join(template_lines)


