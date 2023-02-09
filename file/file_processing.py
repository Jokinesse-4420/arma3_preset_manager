import tkinter as tk
from tkinter import filedialog, messagebox


def get_files_path():
    root = tk.Tk()
    root.withdraw()
    files_path = filedialog.askopenfilename(title='First preset'), filedialog.askopenfilename(title='Second preset')
    while files_path[0] == files_path[1] or (len(files_path[0]) == 0 or len(files_path[1]) == 0):
        messagebox.showerror('ERROR', 'The same preset has been selected twice or 1 of the presets is not selected')
        files_path = filedialog.askopenfilename(title='First preset'), filedialog.askopenfilename(title='Second preset')
    return files_path


def file_to_list(files_path):
    fo = open(files_path[0], 'r', encoding='utf-8')
    so = open(files_path[1], 'r', encoding='utf-8')
    files = fo.readlines(), so.readlines()
    fo.close()
    so.close()
    return files


def extract_content(files_path):
    files = file_to_list(files_path)
    content = files[0][88:-10], files[1][88:-10]
    return content
