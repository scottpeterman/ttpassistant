### Installation and Setup from GitHub Source

To get started with **Visual TTP Assistant** from the GitHub source, follow the instructions below to set up the project in a Python virtual environment.

#### 1. **Clone the Repository**

First, clone the GitHub repository to your local machine:

```bash
git clone https://github.com/scottpeterman/ttpassistant.git
cd ttpassistant
```

#### 2. **Create a Python Virtual Environment**

It’s recommended to create a virtual environment to isolate your project’s dependencies. You can use Python’s built-in `venv` module for this.

To create and activate the virtual environment, run the following commands depending on your operating system:

- **Linux/MacOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

- **Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### 3. **Install Dependencies**

Once the virtual environment is activated, install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This command will install all the necessary libraries, such as `paramiko`, `PyQt6`, `ttp`, and others required by the project.

#### 4. **Run the Application**

After the dependencies are installed, you can run **Visual TTP Assistant**. Assuming the main entry point is configured in `__main__.py`, you can start the application by running:

```bash
python -m ttp_assistant
```

This will launch the tool and allow you to interact with the TTP parsing and execution features via the GUI.

---

### Additional Setup Details

#### Activating the Virtual Environment

Once the environment is set up, every time you work on the project, you need to activate the virtual environment:

- **Linux/MacOS:**

```bash
source venv/bin/activate
```

- **Windows:**

```bash
.\venv\Scripts\activate
```

To deactivate the virtual environment after you are done, simply run:

```bash
deactivate
```

#### Running Tests

If your project includes tests, you can run them within the virtual environment after installing the required test dependencies. For example:

```bash
python -m unittest discover tests
```

Replace `tests` with the actual directory where your test cases reside.

---

### Troubleshooting

1. **Dependency Issues**: If you encounter any dependency conflicts, try updating `pip` and reinstalling the dependencies:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Environment Activation**: If the virtual environment is not activating, ensure you have `python3` (or `python` on Windows) installed and accessible in your system's `PATH`.
