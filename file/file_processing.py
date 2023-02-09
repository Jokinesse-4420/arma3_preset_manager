import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox


def get_files_path():
    root = tk.Tk()
    root.withdraw()
    files_path = filedialog.askopenfilename(title='First preset'), filedialog.askopenfilename(title='Second preset')
    while files_path[0] == files_path[1] or (len(files_path[0]) == 0 or len(files_path[1]) == 0):
        result = messagebox.askretrycancel('ERROR', 'The same preset has been selected twice or 1 of the presets is not selected')
        if not result:
            sys.exit()
        files_path = filedialog.askopenfilename(title='First preset'), filedialog.askopenfilename(title='Second preset')
    return files_path


def file_to_list(files_path):
    fo = open(files_path[0], 'r', encoding='utf-8')
    so = open(files_path[1], 'r', encoding='utf-8')
    files = fo.readlines(), so.readlines()
    fo.close()
    so.close()
    return files


def create_temp(content):
    try:
        os.mkdir('temp')
        os.chdir('.\\temp')
        fw = open('temp.html', 'w', encoding='utf-8')
        sw = open('temp2.html', 'w', encoding='utf-8')
        fw.writelines(content[0])
        sw.writelines(content[1])
        fw.close()
        sw.close()
        os.chdir('..\\')
    except FileExistsError:
        messagebox.showerror('Hint', 'folder already exist')


def delete_temp():
    try:
        os.chdir('.\\temp')
        os.remove('temp.html')
        os.remove('temp2.html')
        os.chdir('..\\')
        os.rmdir('temp')
    except FileNotFoundError:
        messagebox.showerror('ERROR', 'error in supression')
