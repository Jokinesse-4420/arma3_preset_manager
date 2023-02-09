import tkinter as tk
from tkinter import filedialog
from file import extractor as extract


def write_new_preset(mods_sets):
    mods_list = list(mods_sets)
    np = open(set_new_preset_path()+'.html','w',encoding='utf-8')
    np.writelines(extract.extract_header())
    np.writelines(mods_list)
    np.writelines(extract.extract_footer())
    np.close()

def set_new_preset_path():
    root = tk.Tk()
    root.withdraw()
    return filedialog.asksaveasfilename(title='new preset')
