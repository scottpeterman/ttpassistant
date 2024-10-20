from ruamel.yaml import YAML

class TTPLibraryAssistant:
    def __init__(self):
        self.yaml = YAML()

    def save_solution_to_yaml(self, file_path, description, source_text, template, result):
        """Save the current template solution, source, and result to a YAML file."""
        data = {
            'templates': [{
                'description': description,
                'source_text': source_text,
                'template': template,
                'result': result
            }]
        }

        # Write to the YAML file
        try:
            with open(file_path, 'w') as file:
                self.yaml.dump(data, file)
            print(f"Solution saved to {file_path}")
        except Exception as e:
            print(f"Error saving solution: {e}")

    def load_solution_from_yaml(self, file_path):
        """Load a template solution from a YAML file and return the fields."""
        try:
            with open(file_path, 'r') as file:
                data = self.yaml.load(file)
                if 'templates' in data and len(data['templates']) > 0:
                    template_data = data['templates'][0]  # Load the first template for simplicity
                    return template_data.get('source_text', ''), template_data.get('template', ''), template_data.get('result', '')
                else:
                    print("No valid templates found in the file.")
                    return '', '', ''
        except Exception as e:
            print(f"Error loading solution: {e}")
            return '', '', ''
