lines = open(r"C:\Users\Dimka\Desktop\groups science.json", 'r', encoding="utf_8_sig").readlines()

print(lines[10])

new_file = open("sample.json", "w", encoding="utf_8_sig")
stack = ""
# for line in lines:
#     if line[0] not in ['"', '}', '{', '[',']']:
#         stack = stack.replace("\n", "") + ' ' + line 
#     else: 
#         new_file.write(stack)
#         stack = line


for line in lines:
    if line[0] not in ['"', '}', '{', '[',']']:
        stack = stack.replace("\n", "") + ' ' + line 
    else: 
        new_file.write(stack)
        stack = line

