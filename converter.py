import argparse
import os

def create_advanced_gui(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        original_code = f.read()
print("""

███╗░░██╗██╗░░░██╗██╗░░░░░██╗░░░░░██████╗░░█████╗░░█████╗░  ░█████╗░██╗░░██╗
████╗░██║██║░░░██║██║░░░░░██║░░░░░╚════██╗██╔══██╗██╔══██╗  ██╔══██╗██║░██╔╝
██╔██╗██║██║░░░██║██║░░░░░██║░░░░░░░███╔═╝██║░░██║██║░░██║  ██║░░██║█████═╝░
██║╚████║██║░░░██║██║░░░░░██║░░░░░██╔══╝░░██║░░██║██║░░██║  ██║░░██║██╔═██╗░
██║░╚███║╚██████╔╝███████╗███████╗███████╗╚█████╔╝╚█████╔╝  ╚█████╔╝██║░╚██╗
╚═╝░░╚══╝░╚═════╝░╚══════╝╚══════╝╚══════╝░╚════╝░░╚════╝░  ░╚════╝░╚═╝░░╚═╝
                         NULL200OK 💀🔥created by NABEEL 🔥💀
"Terminal-to-GUI: A lightweight Python script to instantly wrap CLI tools into a standalone Graphical User Interface."
""")

    # معالجة الكود الأصلي: استبدال input() بدالة مخصصة تظهر صندوق إدخال
    modified_code = original_code.replace('input(', 'custom_input(')
    indented_code = "\n".join("        " + line for line in modified_code.splitlines())

    wrapper_template = f"""
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import threading
import sys
import io

def custom_input(prompt=""):
    # دالة بديلة لـ input() تفتح نافذة إدخال صغيرة
    return simpledialog.askstring("Input Required", prompt)

def run_original_logic(display_area):
    class WidgetWriter:
        def __init__(self, widget):
            self.widget = widget
        def write(self, s):
            self.widget.insert(tk.END, s)
            self.widget.see(tk.END)
        def flush(self):
            pass

    sys.stdout = WidgetWriter(display_area)
    try:
{indented_code}
    except Exception as e:
        print(f"\\n[Error]: {{e}}")
    finally:
        sys.stdout = sys.__stdout__

def start_thread():
    threading.Thread(target=run_original_logic, args=(txt_area,), daemon=True).start()

# إعداد واجهة tkinter
root = tk.Tk()
root.title("GUI Wrapper Pro")
root.geometry("700x500")
root.configure(bg='#1e1e1e')

lbl = tk.Label(root, text="Terminal to GUI (No Dependencies)", fg="#00FF00", bg="#1e1e1e", font=("Courier", 14))
lbl.pack(pady=10)

txt_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, bg="black", fg="#00FF00", font=("Courier", 10))
txt_area.pack(padx=10, pady=10)

btn_frame = tk.Frame(root, bg='#1e1e1e')
btn_frame.pack(pady=10)

run_btn = tk.Button(btn_frame, text="RUN SCRIPT", command=start_thread, bg="#00FF00", fg="black", font=("Arial", 10, "bold"))
run_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(wrapper_template)
    print(f"✅ تم إنشاء الملف بنجاح: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="gui_app_no_limits.py")
    args = parser.parse_args()
    create_advanced_gui(args.input, args.output)
