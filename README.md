
# Visual TTP Assistant

**Visual TTP Assistant** is an all-in-one network automation and templating tool designed for network engineers, developers, and automation specialists. This tool simplifies the process of parsing network data, creating dynamic templates, running live commands on network devices, and generating executable scripts. With an integrated editor and terminal console, the tool enables users to modify and execute scripts in real-time, streamlining the entire workflow.

## Purpose

Visual TTP Assistant addresses key challenges in network automation and management:
- **Template-driven Parsing**: Automates the extraction and processing of network data using TTP (Text Template Parsing).
- **Live Device Interaction**: Connects to network devices via SSH, runs commands, and processes the output in real-time.
- **Dynamic Code Generation**: Automatically generates Python scripts based on user inputs and templates.
- **Real-time Code Execution**: Provides an integrated development environment with Ace editor and an OS console where users can modify and run generated code.

![App Screenshot](https://github.com/scottpeterman/ttpassistant/raw/main/screenshots/app.png)

## Key Features

### 1. **Template-Driven Parsing**
- **Text Input and Parsing**: Input raw network data (such as command outputs) and apply a TTP template to extract structured information.
- **Dynamic TTP Template Generation**: Easily create TTP templates to extract key details from unstructured network data.
- **Real-Time JSON Results**: View the parsed JSON results instantly after applying a template.

### 2. **SSH Command Execution**
- **Run Commands on Devices**: Execute SSH commands directly on network devices from within the tool. This is integrated with TTP, allowing you to process the live data using templates.
- **Command History**: Auto-populates command fields with previous inputs, saving time for repeated tasks.
- **Asynchronous Execution**: A separate SSH thread ensures that long-running commands don't block the UI.

### 3. **Dynamic Code Generation and Execution**
- **Code Generation**: Automatically generate Python code based on user input, SSH commands, and templates.
- **Ace Editor with OS Console**: The tool comes with an Ace editor that not only highlights code but also allows users to run the generated scripts in real-time through an integrated OS console (PowerShell, batch, Python, etc.).
- **Fully Functional OS Terminal**: The editor includes a fully operational terminal where you can execute scripts instantly without leaving the environment.
- **Real-time Feedback**: See the output of your code directly in the terminal pane.

### 4. **Integrated Editor and Terminal**
- **Ace-based Editor**: Edit your Python scripts or other code in the Ace editor, with features like syntax highlighting, autocompletion, and keyboard shortcuts.
- **OS Console**: Directly execute the scripts written in the Ace editor. It supports Python, batch, and PowerShell commands.
- **Save and Load Files**: The built-in file menu allows users to save and open scripts, making it easy to resume work later.

## Workflow

### Step 1: Input Network Data and Template
- Input raw network command output in the **Text Source** area.
- Create or load a **TTP template** to structure and extract relevant data.
- The **JSON Result** panel immediately displays the parsed output after applying the TTP template.

### Step 2: Execute SSH Commands
- Use the **SSH Runner** to connect to a network device and run custom commands.
- The output from the device can be processed using the TTP template in real-time.
- **Code Generation**: Automatically generate Python scripts that execute the same SSH commands. 

### Step 3: Modify and Run Generated Code
- The generated code is displayed in the **Ace Editor**, where you can edit or modify it as needed.
- Run the script directly from the Ace editor via the integrated OS console.
- View live results in the terminal pane below the editor.

### Step 4: Save or Load Work
- Save your session, including the template, input data, and results, for future use.
- Load previously saved sessions and templates to continue working without starting from scratch.

---
