# PyScript-to-GUI Wrapper 🚀

A powerful, zero-dependency Python tool that instantly transforms your Command-Line Interface (CLI) scripts into clean, functional Graphical User Interfaces (GUI).

## 🌟 Overview
Tired of running your scripts in a boring black terminal? This tool acts as an **Automated Wrapper**. It takes any standard Python script and generates a new file featuring a modern "Dark Mode" GUI. 

Unlike other wrappers, this one handles `input()` prompts by converting them into interactive pop-up dialogs and ensures your UI never freezes during heavy tasks.

## ✨ Key Features
- **Zero External Dependencies:** Built entirely on `tkinter`. The output file runs on any machine with Python installed—no `pip install` required for the GUI.
- **Smart Input Handling:** Automatically detects `input()` calls and replaces them with GUI-based input dialogs.
- **Real-time Logging:** Redirects all `print()` outputs to a sleek, terminal-style text area within the window.
- **Multi-Threaded Execution:** Runs your original script logic in a background thread to keep the interface responsive.
- **Hacker Aesthetic:** Features a "Dark Grey & Lime Green" theme for a professional, technical look.

## 🛠️ How It Works
1. **Source Parsing:** It reads your source code and injects an indentation wrapper.
2. **Dynamic Replacement:** It replaces standard CLI `input()` with a custom GUI function.
3. **Stream Redirection:** It "hijacks" `sys.stdout` to capture text and display it in the GUI's console area.
4. **Code Generation:** It outputs a standalone `.py` file ready for use or conversion to `.exe`.

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone (https://github.com/NULL200OK/PyScript-to-GUI.git)
cd PyScript-to-GUI

2. Run the Converter
Pass your terminal script as the input:

Bash
python converter.py --input my_script.py --output my_new_app.py
3. Run your New GUI!
Bash
python my_new_app.py
###📋 Requirements
Python 3.x
No external libraries needed! (Uses built-in tkinter, threading, and argparse).

###🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page].

Generated with ❤️ to make Python tools more accessible.
