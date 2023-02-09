from file import file_processing as file
import os
import re


PATTERN = "<tr.*\\s*.*\\s*.*\\s.*\\s.*\\s.*\\s.*\\s.*\\s.*</tr>"
FILE_PATH = file.get_files_path()

def extract_content():
    files = file.file_to_list(FILE_PATH)
    content = files[0][88:-10], files[1][88:-10]
    return content

def extract_header():
    files = file.file_to_list(FILE_PATH)
    header = files[0][1:89]
    return header

def extract_footer():
    files = file.file_to_list(FILE_PATH)
    footer = files[0][-10:]
    return footer

def extract_mods():
    os.chdir('.//temp')
    f1 = open('temp.html','r',encoding='utf-8')
    f2 = open('temp2.html','r',encoding='utf-8')
    lists = list_creation(f1.read(),f2.read())
    f1.close()
    f2.close()
    os.chdir('..//')
    file.delete_temp()
    return lists

def list_creation(html_temp,html_temp2):
    liste_temp = re.findall(PATTERN, html_temp)
    liste_temp2 = re.findall(PATTERN, html_temp2)
    return set(liste_temp), set(liste_temp2)
