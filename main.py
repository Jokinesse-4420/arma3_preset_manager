from file import file_processing as file
from file import extractor as extractor
from file import writer as write

content = extractor.extract_content()
file.create_temp(content)
lists_mods = extractor.extract_mods()

#différence
mods_difference = lists_mods[0] ^ lists_mods[1]
write.write_new_preset(mods_difference)


