#!/usr/bin/env python3
import argparse
import sys
import os

# Banner
print("""
███╗░░██╗██╗░░░██╗██╗░░░░░██╗░░░░░██████╗░░█████╗░░█████╗░  ░█████╗░██╗░░██╗
████╗░██║██║░░░██║██║░░░░░██║░░░░░╚════██╗██╔══██╗██╔══██╗  ██╔══██╗██║░██╔╝
██╔██╗██║██║░░░██║██║░░░░░██║░░░░░░░███╔═╝██║░░██║██║░░██║  ██║░░██║█████═╝░
██║╚████║██║░░░██║██║░░░░░██║░░░░░██╔══╝░░██║░░██║██║░░██║  ██║░░██║██╔═██╗░
██║░╚███║╚██████╔╝███████╗███████╗███████╗╚█████╔╝╚█████╔╝  ╚█████╔╝██║░╚██╗
╚═╝░░╚══╝░╚═════╝░╚══════╝╚══════╝╚══════╝░╚════╝░░╚════╝░  ░╚════╝░╚═╝░░╚═╝
            NULL200OK 💀🔥 created by NABEEL 🔥💀
""")
print("Terminal-to-GUI: A lightweight Python script to instantly wrap CLI tools into a standalone Graphical User Interface.\n")

def create_advanced_gui(input_file, output_file):
    """
    Reads a Python script, replaces input() with a GUI popup,
    and wraps everything in a tkinter window.
    """
    # 1. Read the original script
    with open(input_file, 'r', encoding='utf-8') as f:
        original_code = f.read()

    # 2. Replace all input() calls with custom_input() (GUI popup)
    modified_code = original_code.replace('input(', 'custom_input(')

    # 3. Indent the whole original code by 8 spaces (to put inside try: block)
    indented_code = "\n".join("        " + line for line in modified_code.splitlines())

    # 4. Build the GUI wrapper (tkinter)
    wrapper_template = f'''
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import threading
import sys
import io

def custom_input(prompt=""):
    """Replaces input() with a simple dialog box"""
    return simpledialog.askstring("Input Required", prompt)

def run_original_logic(display_area):
    # FIX: Tell Python that 'sys' is the global module, not a local variable
    global sys
    
    class WidgetWriter:
        def __init__(self, widget):
            self.widget = widget
        def write(self, s):
            self.widget.insert(tk.END, s)
            self.widget.see(tk.END)
        def flush(self):
            pass

    # Redirect stdout to the text widget
    sys.stdout = WidgetWriter(display_area)
    try:
{indented_code}
    except Exception as e:
        print(f"\\n[Error]: {{e}}")
    finally:
        # Restore original stdout
        sys.stdout = sys.__stdout__

def start_thread():
    """Run the script in a separate thread so GUI doesn't freeze"""
    threading.Thread(target=run_original_logic, args=(txt_area,), daemon=True).start()

# ---------- Build the main window ----------
root = tk.Tk()
root.title("GUI Wrapper Pro")
root.geometry("700x500")
root.configure(bg='#1e1e1e')

label = tk.Label(root, text="Terminal to GUI (No Dependencies)", fg="#00FF00", bg="#1e1e1e", font=("Courier", 14))
label.pack(pady=10)

txt_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, bg="black", fg="#00FF00", font=("Courier", 10))
txt_area.pack(padx=10, pady=10)

button_frame = tk.Frame(root, bg='#1e1e1e')
button_frame.pack(pady=10)

run_button = tk.Button(button_frame, text="RUN SCRIPT", command=start_thread, bg="#00FF00", fg="black", font=("Arial", 10, "bold"))
run_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
'''

    # 5. Write the final GUI script
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(wrapper_template)

    print(f"✅ Success! GUI wrapper created: {output_file}")
    print("   Run it with: python", output_file)

# ---------- Command line argument handling ----------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert any Python CLI script into a GUI application.")
    parser.add_argument("--input", required=True, help="Original Python script to wrap")
    parser.add_argument("--output", default="gui_app_no_limits.py", help="Output filename (default: gui_app_no_limits.py)")
    args = parser.parse_args()

    create_advanced_gui(args.input, args.output)
