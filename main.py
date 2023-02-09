from file import file_processing as file
from file import extractor as extractor

files_path = file.get_files_path()
content = extractor.extract_content(files_path)
file.create_temp(content)
lists_mods = extractor.extract_mods()

#différence
mods_difference = lists_mods[0] ^ lists_mods[1]
print(mods_difference)
