import os
import time

from file import file_processing as file

#Selection des chemins d'accès vers les fichiers et mise en variable des lites
files_path = file.get_files_path()
content = file.extract_content(files_path)

#TEST
os.mkdir('temp')
os.chdir('.\\temp')

fw = open('temp.html','w',encoding='utf-8')
sw = open('temp2.html','w',encoding='utf-8')

#Ecriture du contenu des 2 preset d'origine
fw.writelines(content[0])
sw.writelines(content[1])

fw.close()
sw.close()
os.remove('temp.html')
os.remove('temp2.html')
os.chdir('..\\')
os.rmdir('temp')
